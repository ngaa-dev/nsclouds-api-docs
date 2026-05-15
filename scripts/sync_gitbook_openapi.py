#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUNDLED_ROOT = ROOT / "docs" / "bundled"
DEFAULT_RAW_BASE = "https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled"
API_BASE = "https://api.gitbook.com/v1"


@dataclass(frozen=True)
class SpecEntry:
    env: str
    lang: str
    vendor: str
    slug: str
    local_path: Path
    source_url: str


def request_json(
    method: str,
    url: str,
    token: str,
    payload: dict | None = None,
) -> tuple[int, dict | list | None]:
    data = None
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read().decode("utf-8")
            return resp.status, json.loads(body) if body else None
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8")
        parsed = None
        if body:
            try:
                parsed = json.loads(body)
            except json.JSONDecodeError:
                parsed = {"raw": body}
        return exc.code, parsed


def list_orgs(token: str) -> list[dict]:
    status, payload = request_json("GET", f"{API_BASE}/orgs", token)
    if status != 200 or not isinstance(payload, dict):
        raise RuntimeError(f"Failed to list GitBook organizations: status={status} payload={payload}")
    items = payload.get("items") or []
    return [item for item in items if isinstance(item, dict)]


def resolve_org_id(token: str, org_id: str | None) -> str:
    if org_id:
        return org_id

    orgs = list_orgs(token)
    if len(orgs) == 1:
        resolved = orgs[0]["id"]
        print(f"Using the only available GitBook organization: {orgs[0].get('title')} ({resolved})")
        return resolved

    print("Multiple GitBook organizations found. Set GITBOOK_ORG_ID or pass --org-id.", file=sys.stderr)
    for org in orgs:
        print(f"- {org.get('title')} ({org.get('id')})", file=sys.stderr)
    raise SystemExit(2)


def discover_specs(raw_base: str) -> list[SpecEntry]:
    entries: list[SpecEntry] = []
    for env_dir in sorted(BUNDLED_ROOT.iterdir()):
        if not env_dir.is_dir():
            continue
        env = env_dir.name
        for lang_dir in sorted(env_dir.iterdir()):
            if not lang_dir.is_dir():
                continue
            lang = lang_dir.name
            for spec_path in sorted(lang_dir.glob("*.bundled.yaml")):
                vendor = spec_path.name.removesuffix(".bundled.yaml")
                slug = f"{vendor}-{lang}-{env}"
                source_url = f"{raw_base.rstrip('/')}/{env}/{lang}/{spec_path.name}"
                entries.append(
                    SpecEntry(
                        env=env,
                        lang=lang,
                        vendor=vendor,
                        slug=slug,
                        local_path=spec_path,
                        source_url=source_url,
                    )
                )
    return entries


def filter_specs(entries: list[SpecEntry], envs: set[str], langs: set[str], vendors: set[str]) -> list[SpecEntry]:
    result = []
    for entry in entries:
        if envs and entry.env not in envs:
            continue
        if langs and entry.lang not in langs:
            continue
        if vendors and entry.vendor not in vendors:
            continue
        result.append(entry)
    return result


def ensure_spec(token: str, org_id: str, entry: SpecEntry) -> tuple[int, dict | list | None]:
    url = f"{API_BASE}/orgs/{org_id}/openapi/{entry.slug}"
    payload = {
        "source": {
            "type": "url",
            "url": entry.source_url,
        }
    }
    return request_json("PUT", url, token, payload)


def set_visibility(token: str, org_id: str, slug: str, visibility: str) -> tuple[int, dict | list | None]:
    url = f"{API_BASE}/orgs/{org_id}/openapi/{slug}"
    return request_json("PATCH", url, token, {"visibility": visibility})


def wait_until_complete(token: str, org_id: str, slug: str, timeout_seconds: int) -> dict | list | None:
    deadline = time.time() + timeout_seconds
    url = f"{API_BASE}/orgs/{org_id}/openapi/{slug}"
    while True:
        status, payload = request_json("GET", url, token)
        if status != 200:
            raise RuntimeError(f"Failed to fetch OpenAPI spec status for {slug}: status={status} payload={payload}")
        if isinstance(payload, dict) and payload.get("processingState") == "complete":
            return payload
        if time.time() >= deadline:
            raise TimeoutError(f"Timed out waiting for {slug} to finish processing")
        time.sleep(3)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create or update GitBook OpenAPI specs from docs/bundled/*.yaml")
    parser.add_argument("--org-id", help="GitBook organization ID. Falls back to GITBOOK_ORG_ID or auto-detect if only one org is visible.")
    parser.add_argument("--token", help="GitBook developer token. Falls back to GITBOOK_TOKEN.")
    parser.add_argument("--raw-base", default=os.getenv("GITBOOK_RAW_BASE", DEFAULT_RAW_BASE), help="Raw GitHub base URL for docs/bundled")
    parser.add_argument("--env", action="append", choices=["cn", "global"], default=[], help="Only sync selected environment(s)")
    parser.add_argument("--lang", action="append", choices=["en", "zh"], default=[], help="Only sync selected language(s)")
    parser.add_argument("--vendor", action="append", default=[], help="Only sync selected vendor(s), e.g. dashscope")
    parser.add_argument("--visibility", choices=["public", "private"], help="Optionally patch spec visibility after upload")
    parser.add_argument("--wait", action="store_true", help="Wait until each spec finishes processing")
    parser.add_argument("--timeout-seconds", type=int, default=180, help="Timeout used with --wait")
    parser.add_argument("--dry-run", action="store_true", help="Print planned operations without calling GitBook API")
    args = parser.parse_args()

    token = args.token or os.getenv("GITBOOK_TOKEN")
    if not token:
        print("Missing GitBook token. Set GITBOOK_TOKEN or pass --token.", file=sys.stderr)
        raise SystemExit(2)

    org_id = resolve_org_id(token, args.org_id or os.getenv("GITBOOK_ORG_ID"))

    entries = discover_specs(args.raw_base)
    entries = filter_specs(entries, set(args.env), set(args.lang), set(args.vendor))
    if not entries:
        print("No OpenAPI specs matched the requested filters.", file=sys.stderr)
        raise SystemExit(2)

    print(f"GitBook organization: {org_id}")
    print(f"Specs to sync: {len(entries)}")

    for entry in entries:
        print(f"- {entry.slug} -> {entry.source_url}")

    if args.dry_run:
        return

    for entry in entries:
        status, payload = ensure_spec(token, org_id, entry)
        if status not in {200, 201}:
            raise RuntimeError(f"Failed to sync {entry.slug}: status={status} payload={payload}")
        print(f"Synced {entry.slug} ({status})")

        if args.visibility:
            vis_status, vis_payload = set_visibility(token, org_id, entry.slug, args.visibility)
            if vis_status != 200:
                raise RuntimeError(f"Failed to set visibility for {entry.slug}: status={vis_status} payload={vis_payload}")
            print(f"  visibility={args.visibility}")

        if args.wait:
            spec = wait_until_complete(token, org_id, entry.slug, args.timeout_seconds)
            state = spec.get("processingState") if isinstance(spec, dict) else "unknown"
            print(f"  processingState={state}")


if __name__ == "__main__":
    main()
