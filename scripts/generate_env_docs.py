#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = ROOT / "docs" / "templates"
DOCS_DIR = ROOT / "docs"

ENV_MODEL_FILES = {
    "cn": ROOT / "scripts" / "data" / "cn_model_info.json",
    "global": ROOT / "scripts" / "data" / "global_model_info.json",
}

LANGS = ("zh", "en")
NEW_OPENAPI_VENDORS = {
    "dashscope": "DashScope",
    "zai": "Z.AI",
    "xai": "xAI",
    "xiaomi": "Xiaomi",
}
VENDOR_ORDER = {
    "cn": ["dashscope", "minimax", "deepseek", "volcengine", "zai", "xiaomi"],
    "global": [
        "anthropic",
        "openai",
        "google",
        "deepseek",
        "volcengine",
        "dashscope",
        "minimax",
        "zai",
        "moonshotai",
        "xai",
    ],
}
BRAND_NAMES = {
    "anthropic": "Anthropic",
    "dashscope": "DashScope",
    "deepseek": "DeepSeek",
    "google": "Google",
    "minimax": "MiniMax",
    "moonshotai": "Moonshot AI",
    "openai": "OpenAI",
    "volcengine": "Volcengine",
    "xai": "xAI",
    "xiaomi": "Xiaomi",
    "zai": "Z.AI",
}

# Keep legacy Text Completions pages out of generated docs unless explicitly enabled.
# Flip this to true if the /v1/completions docs and OpenAPI specs need to be exposed again.
SHOW_TEXT_COMPLETIONS = False

@dataclass(frozen=True)
class ModelRecord:
    vendor: str
    model_name: str
    mode: str
    endpoints: tuple[str, ...]


LANG_CONFIG = {
    "zh": {
        "intro": "简介",
        "chat_root": "对话接口",
        "completions_root": "文本补全",
        "image_gen_root": "图像生成",
        "image_edit_root": "图像编辑",
        "audio_root": "音频转录",
        "chat_leaf": "Chat Completions",
        "messages_leaf": "Messages",
        "responses_leaf": "Responses",
        "gemini_leaf": "Gemini Native",
        "models_label": "模型列表",
        "capabilities_label": "支持能力",
        "supported_vendors_label": "支持的厂家",
        "none": "（暂无）",
        "summary_title": "# Table of contents",
        "readme_chat": "对话接口涵盖标准 Chat Completions，以及按厂家提供的扩展协议能力。",
        "readme_completions": "文本补全能力按公开支持聊天模型的厂家展示，便于按厂家查找兼容接口。",
        "readme_image_generations": "图像生成能力仅展示当前环境对外公开可用的厂家。",
        "readme_image_edits": "图像编辑能力仅展示当前环境对外公开可用的厂家。",
        "readme_audio": "音频转录能力仅展示当前环境对外公开可用的厂家。",
        "vendor_overview": "{vendor} 在当前环境下提供以下公开能力。",
        "hint_chat": "本接口提供与 OpenAI Chat Completions 兼容的请求路径。不同厂家和模型的实际参数支持范围可能不同。",
        "hint_completions": "本接口提供与 OpenAI Completions 兼容的请求路径。不同厂家和模型的实际参数支持范围可能不同。",
        "hint_messages": "本接口提供与 Anthropic Messages 协议兼容的请求路径。具体行为以当前支持能力为准。",
        "hint_responses": "本接口提供与 OpenAI Responses 兼容的请求路径。不同厂家和模型的实际参数支持范围可能不同。",
        "hint_gemini": "本接口提供与 Google Gemini 原生协议兼容的请求路径。",
        "hint_images": "本接口提供与 OpenAI Images 兼容的请求路径。不同厂家和模型的实际能力可能不同。",
        "hint_audio": "本接口提供与 OpenAI Audio Transcriptions 兼容的请求路径。不同厂家和模型的实际能力可能不同。",
        "overview_chat": "{vendor} 在当前环境中提供的对话生成能力。",
        "overview_completions": "{vendor} 在当前环境中提供的文本补全能力。",
        "overview_messages": "{vendor} 在当前环境中提供的 Messages 协议能力。",
        "overview_responses": "{vendor} 在当前环境中提供的 Responses 协议能力。",
        "overview_gemini": "{vendor} 在当前环境中提供的 Gemini 原生协议能力。",
        "overview_image_generations": "{vendor} 在当前环境中提供的图像生成能力。",
        "overview_image_edits": "{vendor} 在当前环境中提供的图像编辑能力。",
        "overview_audio_transcriptions": "{vendor} 在当前环境中提供的音频转写能力。",
        "openapi_section": "### 2. 接口详情",
        "openapi_section_after_extra": "### 3. 接口详情",
        "overview_section": "### 1. 概述",
    },
    "en": {
        "intro": "Introduction",
        "chat_root": "Conversation APIs",
        "completions_root": "Text Completions",
        "image_gen_root": "Image Generations",
        "image_edit_root": "Image Edits",
        "audio_root": "Audio Transcriptions",
        "chat_leaf": "Chat Completions",
        "messages_leaf": "Messages",
        "responses_leaf": "Responses",
        "gemini_leaf": "Gemini Native",
        "models_label": "Supported models",
        "capabilities_label": "Supported capabilities",
        "navigation_label": "Available pages",
        "supported_vendors_label": "Supported vendors",
        "none": "(None)",
        "summary_title": "# Table of contents",
        "readme_chat": "Conversation APIs cover standard Chat Completions and vendor-specific protocol variants.",
        "readme_completions": "Text completions are listed for every vendor that publicly exposes chat models in this environment.",
        "readme_image_generations": "Image generation only lists vendors that are publicly available in this environment.",
        "readme_image_edits": "Image edits only list vendors that are publicly available in this environment.",
        "readme_audio": "Audio transcriptions only list vendors that are publicly available in this environment.",
        "vendor_overview": "{vendor} exposes the following public capabilities in this environment.",
        "hint_chat": "This endpoint provides an OpenAI-compatible Chat Completions path. Actual parameter support may vary by vendor and model.",
        "hint_completions": "This endpoint provides an OpenAI-compatible Completions path. Actual parameter support may vary by vendor and model.",
        "hint_messages": "This endpoint provides an Anthropic Messages-compatible path. Actual behavior depends on current supported capabilities.",
        "hint_responses": "This endpoint provides an OpenAI-compatible Responses path. Actual parameter support may vary by vendor and model.",
        "hint_gemini": "This endpoint provides a Google Gemini native-compatible path.",
        "hint_images": "This endpoint provides an OpenAI-compatible Images path. Actual capabilities may vary by vendor and model.",
        "hint_audio": "This endpoint provides an OpenAI-compatible Audio Transcriptions path. Actual capabilities may vary by vendor and model.",
        "overview_chat": "{vendor} exposes conversation capabilities in this environment.",
        "overview_completions": "{vendor} exposes text completion capabilities in this environment.",
        "overview_messages": "{vendor} exposes Messages protocol capabilities in this environment.",
        "overview_responses": "{vendor} exposes Responses capabilities in this environment.",
        "overview_gemini": "{vendor} exposes Gemini native protocol capabilities in this environment.",
        "overview_image_generations": "{vendor} exposes image generation capabilities in this environment.",
        "overview_image_edits": "{vendor} exposes image edit capabilities in this environment.",
        "overview_audio_transcriptions": "{vendor} exposes audio transcription capabilities in this environment.",
        "openapi_section": "### 2. API Details",
        "openapi_section_after_extra": "### 3. API Details",
        "overview_section": "### 1. Overview",
    },
}

LANG_CONFIG["zh"]["navigation_label"] = "页面导航"
LANG_CONFIG["en"]["navigation_label"] = "Available pages"

CHAT_LEAF_ORDER = ("chat", "messages", "responses", "gemini")
GEMINI_NATIVE_DOC_PATHS = (
    "/v1/models/{model}:generateContent",
    "/v1beta/models/{model}:generateContent",
    "/v1beta/models/{model}:streamGenerateContent",
)
GEMINI_NATIVE_ENDPOINTS = GEMINI_NATIVE_DOC_PATHS


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return
    path.write_text(content, encoding="utf-8")


def sync_openapi_templates() -> None:
    replace_pairs = {
        "zh": [("OpenAI 的", "{display} 的"), ("OpenAI 厂家标签", "{display} 厂家标签"), ("OpenAI", "{display}")],
        "en": [("OpenAI's", "{display}'s"), ("OpenAI Vendor Tags", "{display} Vendor Tags"), ("OpenAI", "{display}")],
    }
    for lang in LANGS:
        base_path = TEMPLATES_DIR / lang / "openapi" / "openai.yaml"
        base_content = read_text(base_path)
        for vendor, display in NEW_OPENAPI_VENDORS.items():
            content = base_content.replace("_openai", f"_{vendor}")
            for before, after in replace_pairs[lang]:
                content = content.replace(before, after.format(display=display))
            write_text(TEMPLATES_DIR / lang / "openapi" / f"{vendor}.yaml", content)


def load_model_records(env: str) -> list[ModelRecord]:
    payload = json.loads(read_text(ENV_MODEL_FILES[env]))
    records: list[ModelRecord] = []
    for item in payload.get("data", []):
        info = item.get("model_info") or {}
        vendor = (info.get("original_provider") or "").strip().lower()
        if not vendor:
            continue
        records.append(
            ModelRecord(
                vendor=vendor,
                model_name=item.get("model_name", ""),
                mode=info.get("mode") or "",
                endpoints=tuple(info.get("supported_endpoints") or []),
            )
        )
    return records


def unique_model_names(records: Iterable[ModelRecord]) -> list[str]:
    return sorted({record.model_name for record in records if record.model_name})


def order_vendors(env: str, vendors: Iterable[str]) -> list[str]:
    wanted = list(vendors)
    ordered = [vendor for vendor in VENDOR_ORDER[env] if vendor in wanted]
    extras = sorted(set(wanted) - set(ordered))
    return ordered + extras


def has_endpoint(record: ModelRecord, endpoint: str) -> bool:
    return endpoint in record.endpoints


def supports_chat_completion(records: Iterable[ModelRecord]) -> bool:
    return any(has_endpoint(record, "/v1/chat/completions") for record in records)


def supports_gemini_native(records: Iterable[ModelRecord]) -> bool:
    return any(any(endpoint in record.endpoints for endpoint in GEMINI_NATIVE_ENDPOINTS) for record in records)


def build_env_index(env: str) -> dict:
    records = load_model_records(env)
    by_vendor: dict[str, list[ModelRecord]] = defaultdict(list)
    for record in records:
        by_vendor[record.vendor].append(record)

    chat_vendors = order_vendors(
        env,
        {
            vendor
            for vendor, vendor_records in by_vendor.items()
            if supports_chat_completion(vendor_records)
            or any(has_endpoint(r, "/v1/messages") for r in vendor_records)
            or any(has_endpoint(r, "/v1/responses") for r in vendor_records)
            or supports_gemini_native(vendor_records)
        },
    )
    image_gen_vendors = order_vendors(
        env, {vendor for vendor, vendor_records in by_vendor.items() if any(has_endpoint(r, "/v1/images/generations") for r in vendor_records)}
    )
    image_edit_vendors = order_vendors(
        env, {vendor for vendor, vendor_records in by_vendor.items() if any(has_endpoint(r, "/v1/images/edits") for r in vendor_records)}
    )
    audio_vendors = order_vendors(
        env, {vendor for vendor, vendor_records in by_vendor.items() if any(has_endpoint(r, "/v1/audio/transcriptions") for r in vendor_records)}
    )

    chat_capabilities: dict[str, list[str]] = {}
    for vendor in chat_vendors:
        vendor_records = by_vendor[vendor]
        children = []
        if supports_chat_completion(vendor_records):
            children.append("chat")
        if any(has_endpoint(record, "/v1/messages") for record in vendor_records):
            children.append("messages")
        if any(has_endpoint(record, "/v1/responses") for record in vendor_records):
            children.append("responses")
        if supports_gemini_native(vendor_records):
            children.append("gemini")
        chat_capabilities[vendor] = [cap for cap in CHAT_LEAF_ORDER if cap in children]

    return {
        "records": records,
        "by_vendor": by_vendor,
        "chat_vendors": chat_vendors,
        "chat_capabilities": chat_capabilities,
        "completion_vendors": order_vendors(
            env, {vendor for vendor, vendor_records in by_vendor.items() if supports_chat_completion(vendor_records)}
        ),
        "image_gen_vendors": image_gen_vendors,
        "image_edit_vendors": image_edit_vendors,
        "audio_vendors": audio_vendors,
    }


def vendor_name(vendor: str) -> str:
    return BRAND_NAMES.get(vendor, vendor)


def models_for_capability(env_index: dict, vendor: str, capability: str) -> list[str]:
    records = env_index["by_vendor"][vendor]
    if capability in {"chat", "completions"}:
        return unique_model_names(record for record in records if has_endpoint(record, "/v1/chat/completions"))
    if capability == "gemini":
        return unique_model_names(record for record in records if any(endpoint in record.endpoints for endpoint in GEMINI_NATIVE_ENDPOINTS))
    endpoint_map = {
        "messages": "/v1/messages",
        "responses": "/v1/responses",
        "image_generations": "/v1/images/generations",
        "image_edits": "/v1/images/edits",
        "audio_transcriptions": "/v1/audio/transcriptions",
    }
    endpoint = endpoint_map[capability]
    return unique_model_names(record for record in records if has_endpoint(record, endpoint))


def build_openapi_block(spec_vendor: str, env: str, lang: str, path: str, label: str) -> str:
    spec_name = f"{spec_vendor}-{lang}-{env}"
    raw_url = f"https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/{env}/{lang}/{spec_vendor}.bundled.yaml"
    return (
        f'{{% openapi-operation spec="{spec_name}" path="{path}" method="post" %}}\n'
        f"[OpenAPI {label}]({raw_url})\n"
        "{% endopenapi-operation %}\n"
    )


def models_section(models: list[str], lang: str) -> str:
    cfg = LANG_CONFIG[lang]
    if not models:
        return f"**{cfg['models_label']}：**\n\n{cfg['none']}\n"
    bullets = "\n".join(f"* `{model}`" for model in models)
    return f"**{cfg['models_label']}：**\n\n{bullets}\n"


def success_hint(text: str) -> str:
    return f'{{% hint style="success" %}}\n{text}\n{{% endhint %}}\n'


def hidden_frontmatter(content: str) -> str:
    return f"---\nhidden: true\n---\n\n{content}"


def capability_title(capability: str, lang: str) -> str:
    cfg = LANG_CONFIG[lang]
    return {
        "chat": cfg["chat_leaf"],
        "messages": cfg["messages_leaf"],
        "responses": cfg["responses_leaf"],
        "gemini": cfg["gemini_leaf"],
        "completions": cfg["completions_root"],
        "image_generations": cfg["image_gen_root"],
        "image_edits": cfg["image_edit_root"],
        "audio_transcriptions": cfg["audio_root"],
    }[capability]


def capability_filename(capability: str) -> str:
    return {
        "chat": "chat-completions.md",
        "messages": "messages.md",
        "responses": "responses.md",
        "gemini": "gemini-native.md",
    }[capability]


def capability_overview(capability: str, vendor: str, lang: str) -> str:
    cfg = LANG_CONFIG[lang]
    key = {
        "chat": "overview_chat",
        "messages": "overview_messages",
        "responses": "overview_responses",
        "gemini": "overview_gemini",
        "completions": "overview_completions",
        "image_generations": "overview_image_generations",
        "image_edits": "overview_image_edits",
        "audio_transcriptions": "overview_audio_transcriptions",
    }[capability]
    return cfg[key].format(vendor=vendor_name(vendor))


def capability_hint(capability: str, lang: str) -> str:
    cfg = LANG_CONFIG[lang]
    key = {
        "chat": "hint_chat",
        "messages": "hint_messages",
        "responses": "hint_responses",
        "gemini": "hint_gemini",
        "completions": "hint_completions",
        "image_generations": "hint_images",
        "image_edits": "hint_images",
        "audio_transcriptions": "hint_audio",
    }[capability]
    return cfg[key]


def info_hint(text: str) -> str:
    return f'{{% hint style="info" %}}\n{text}\n{{% endhint %}}\n'


def file_input_notes(lang: str, vendor: str, capability: str) -> str:
    if vendor != "openai" or capability not in {"chat", "responses"}:
        return ""
    if lang == "zh" and capability == "chat":
        return (
            "### 2. 文件输入说明\n\n"
            + info_hint(
                "`/v1/chat/completions` 支持通过 `file_data` 传入 base64 文件内容，也兼容 OpenAI 的 `file_id` 字段；不支持 `file_url`。如需通过 URL 传入文件，请使用 Responses API。"
            )
            + "\n"
            "| 字段 | 支持情况 | 建议 |\n"
            "| --- | --- | --- |\n"
            "| `file_data` | 支持 | 当前推荐，适合直接以内联 base64 传入文件内容 |\n"
            "| `file_id` | OpenAI 兼容字段，适配中 | 来源于 Files API 上传后返回的文件 ID，实际可用性取决于文件托管和模型侧支持 |\n"
            "| `file_url` | 不支持 | 请改用 `/v1/responses` 的 `input_file.file_url` |\n"
        )
    if lang == "zh" and capability == "responses":
        return (
            "### 2. 文件与图片输入说明\n\n"
            + info_hint(
                "`/v1/responses` 支持通过 URL 或 data URL 传入图片和文件，也兼容 OpenAI 的 `file_id`。当前建议优先使用 `image_url`、`file_url` 或 `file_data`；图片和文件的 `file_id` 均依赖 Files API 上传、文件托管和模型侧映射能力。"
            )
            + "\n"
            "| 字段 | 适用类型 | 支持情况 | 建议 |\n"
            "| --- | --- | --- | --- |\n"
            "| `image_url` | `input_image` | 支持 | 当前推荐，适合图片 URL 或图片 data URL |\n"
            "| `file_url` | `input_file` | 支持 | 当前推荐，适合可公开访问的文件 URL |\n"
            "| `file_data` | `input_file` | 支持 | 当前推荐，适合以内联 base64 传入文件内容 |\n"
            "| `file_id` | `input_image` / `input_file` | OpenAI 兼容字段，适配中 | 来源于 Files API 上传后返回的文件 ID，实际可用性取决于文件托管和模型侧支持 |\n"
        )
    if lang == "en" and capability == "chat":
        return (
            "### 2. File Input Notes\n\n"
            + info_hint(
                "`/v1/chat/completions` supports base64 file input through `file_data` and keeps OpenAI-compatible `file_id`; it does not support `file_url`. Use the Responses API when you need to pass files by URL."
            )
            + "\n"
            "| Field | Support | Recommendation |\n"
            "| --- | --- | --- |\n"
            "| `file_data` | Supported | Recommended today for inline base64 file content |\n"
            "| `file_id` | OpenAI-compatible field, in adaptation | Comes from a Files API upload; actual availability depends on file hosting and model-side support |\n"
            "| `file_url` | Not supported | Use `/v1/responses` with `input_file.file_url` instead |\n"
        )
    if lang == "en" and capability == "responses":
        return (
            "### 2. File And Image Input Notes\n\n"
            + info_hint(
                "`/v1/responses` supports image and file inputs by URL or data URL, and keeps OpenAI-compatible `file_id`. Prefer `image_url`, `file_url`, or `file_data` today; image and file `file_id` both depend on Files API upload, file hosting, and model-side mapping support."
            )
            + "\n"
            "| Field | Applies to | Support | Recommendation |\n"
            "| --- | --- | --- | --- |\n"
            "| `image_url` | `input_image` | Supported | Recommended today for image URLs or image data URLs |\n"
            "| `file_url` | `input_file` | Supported | Recommended today for publicly accessible file URLs |\n"
            "| `file_data` | `input_file` | Supported | Recommended today for inline base64 file content |\n"
            "| `file_id` | `input_image` / `input_file` | OpenAI-compatible field, in adaptation | Comes from a Files API upload; actual availability depends on file hosting and model-side support |\n"
        )
    return ""


def openapi_spec_vendor(vendor: str, capability: str) -> str:
    if capability == "gemini":
        return "google"
    return vendor


def openapi_path(capability: str) -> list[str]:
    if capability == "gemini":
        return list(GEMINI_NATIVE_DOC_PATHS)
    return [
        {
            "chat": "/v1/chat/completions",
            "messages": "/v1/messages",
            "responses": "/v1/responses",
            "completions": "/v1/completions",
            "image_generations": "/v1/images/generations",
            "image_edits": "/v1/images/edits",
            "audio_transcriptions": "/v1/audio/transcriptions",
        }[capability]
    ]


def build_capability_page(env: str, lang: str, vendor: str, capability: str, models: list[str]) -> str:
    cfg = LANG_CONFIG[lang]
    title = f"# {vendor_name(vendor)} - {capability_title(capability, lang)}"
    overview = capability_overview(capability, vendor, lang)
    hint = capability_hint(capability, lang)
    spec_vendor = openapi_spec_vendor(vendor, capability)
    blocks = "\n".join(
        build_openapi_block(spec_vendor, env, lang, path, vendor_name(vendor)) for path in openapi_path(capability)
    )
    extra_section = file_input_notes(lang, vendor, capability)
    extra_block = f"{extra_section}\n" if extra_section else ""
    openapi_section = cfg["openapi_section_after_extra"] if extra_section else cfg["openapi_section"]
    return (
        f"{title}\n\n"
        f"{cfg['overview_section']}\n\n"
        f"{overview}\n\n"
        f"{success_hint(hint)}\n"
        f"{models_section(models, lang)}\n\n"
        f"{extra_block}"
        f"{openapi_section}\n\n"
        f"{blocks}"
    )


def chat_vendor_summary_target(vendor: str) -> str:
    return f"{vendor}/readme.md"


def chat_capability_filename(capability: str) -> str:
    return {
        "chat": "chat",
        "messages": "messages",
        "responses": "responses",
        "gemini": "gemini-native",
    }[capability] + ".md"


def build_vendor_landing(lang: str, vendor: str, capabilities: list[str]) -> str:
    title = f"# {vendor_name(vendor)}"
    capability_lines = "\n".join(
        f"- [{capability_title(capability, lang)}]({chat_capability_filename(capability)})"
        for capability in capabilities
    )
    return f"{title}\n\n{capability_lines}\n"


def category_vendor_target(category_key: str, vendor: str) -> str:
    if category_key == "chat":
        return f"conversation/{chat_vendor_summary_target(vendor)}"
    if category_key == "completions":
        return f"completions/{vendor}.md"
    if category_key == "image_generations":
        return f"image-generations/{vendor}.md"
    if category_key == "image_edits":
        return f"image-edits/{vendor}.md"
    if category_key == "audio_transcriptions":
        return f"audio-transcriptions/{vendor}.md"
    return f"{vendor}.md"


def category_landing_filename(category_key: str) -> str:
    return {
        "chat": "conversation.md",
        "completions": "completions.md",
        "image_generations": "image-generations.md",
        "image_edits": "image-edits.md",
        "audio_transcriptions": "audio-transcriptions.md",
    }[category_key]


def category_summary_target(category_key: str) -> str:
    return {
        "chat": "conversation/readme.md",
        "completions": "completions/readme.md",
        "image_generations": "image-generations/readme.md",
        "image_edits": "image-edits/readme.md",
        "audio_transcriptions": "audio-transcriptions/readme.md",
    }[category_key]


def build_category_landing(lang: str, category_key: str, vendors: list[str]) -> str:
    cfg = LANG_CONFIG[lang]
    title_map = {
        "chat": cfg["chat_root"],
        "completions": cfg["completions_root"],
        "image_generations": cfg["image_gen_root"],
        "image_edits": cfg["image_edit_root"],
        "audio_transcriptions": cfg["audio_root"],
    }
    vendor_lines = (
        "\n".join(f"- [{vendor_name(vendor)}]({category_vendor_target(category_key, vendor)})" for vendor in vendors)
        if vendors
        else cfg["none"]
    )
    return f"# {title_map[category_key]}\n\n{vendor_lines}\n"


def build_chat_directory_summary(lang: str, vendors: list[str]) -> str:
    cfg = LANG_CONFIG[lang]
    vendor_lines = "\n".join(f"- [{vendor_name(vendor)}]({chat_vendor_summary_target(vendor)})" for vendor in vendors) if vendors else cfg["none"]
    return f"# {cfg['chat_root']}\n\n{vendor_lines}\n"


def build_category_directory_summary(lang: str, category_key: str, vendors: list[str]) -> str:
    cfg = LANG_CONFIG[lang]
    title_map = {
        "completions": cfg["completions_root"],
        "image_generations": cfg["image_gen_root"],
        "image_edits": cfg["image_edit_root"],
        "audio_transcriptions": cfg["audio_root"],
    }
    vendor_lines = "\n".join(f"- [{vendor_name(vendor)}]({vendor}.md)" for vendor in vendors) if vendors else cfg["none"]
    return f"# {title_map[category_key]}\n\n{vendor_lines}\n"


def render_env(env: str) -> None:
    env_index = build_env_index(env)
    for lang in LANGS:
        cfg = LANG_CONFIG[lang]
        base = DOCS_DIR / env / lang
        for rel in (
            "conversation",
            "chat-completion",
            "completions",
            "image-generations",
            "image-edits",
            "audio-transcriptions",
            "embeddings",
            "messages",
            "responses",
            "gemini-native",
        ):
            path = base / rel
            if path.exists():
                subprocess.run(["rm", "-rf", str(path)], check=True)
        summary_path = base / "SUMMARY.md"
        if summary_path.exists():
            summary_path.unlink()
        for stale_readme in base.rglob("README.md"):
            if stale_readme != base / "README.md":
                stale_readme.unlink()
        for landing_file in (
            "conversation.md",
            "chat-completion.md",
            "completions.md",
            "image-generations.md",
            "image-edits.md",
            "audio-transcriptions.md",
        ):
            stale_landing = base / landing_file
            if stale_landing.exists():
                stale_landing.unlink()

        write_text(base / "conversation" / "SUMMARY.md", build_chat_directory_summary(lang, env_index["chat_vendors"]))
        if SHOW_TEXT_COMPLETIONS:
            write_text(base / "completions" / "SUMMARY.md", build_category_directory_summary(lang, "completions", env_index["completion_vendors"]))
        write_text(
            base / "image-generations" / "SUMMARY.md",
            build_category_directory_summary(lang, "image_generations", env_index["image_gen_vendors"]),
        )
        write_text(
            base / "image-edits" / "SUMMARY.md",
            build_category_directory_summary(lang, "image_edits", env_index["image_edit_vendors"]),
        )
        write_text(
            base / "audio-transcriptions" / "SUMMARY.md",
            build_category_directory_summary(lang, "audio_transcriptions", env_index["audio_vendors"]),
        )

        summary_lines = [cfg["summary_title"], "", f"* [{cfg['intro']}](README.md)"]

        summary_lines.append(f"* [{cfg['chat_root']}]({category_summary_target('chat')})")
        for vendor in env_index["chat_vendors"]:
            summary_lines.append(f"  * [{vendor_name(vendor)}](conversation/{chat_vendor_summary_target(vendor)})")
            write_text(
                base / "conversation" / vendor / "SUMMARY.md",
                build_vendor_landing(lang, vendor, env_index["chat_capabilities"][vendor]),
            )
            for capability in env_index["chat_capabilities"][vendor]:
                filename = chat_capability_filename(capability)
                summary_lines.append(
                    f"    * [{capability_title(capability, lang)}](conversation/{vendor}/{filename})"
                )
                write_text(
                    base / "conversation" / vendor / filename,
                    build_capability_page(env, lang, vendor, capability, models_for_capability(env_index, vendor, capability)),
                )

        if SHOW_TEXT_COMPLETIONS:
            summary_lines.append(f"* [{cfg['completions_root']}]({category_summary_target('completions')})")
            for vendor in env_index["completion_vendors"]:
                page = build_capability_page(env, lang, vendor, "completions", models_for_capability(env_index, vendor, "completions"))
                summary_lines.append(f"  * [{vendor_name(vendor)}](completions/{vendor}.md)")
                write_text(base / "completions" / f"{vendor}.md", page)

        summary_lines.append(f"* [{cfg['image_gen_root']}]({category_summary_target('image_generations')})")
        for vendor in env_index["image_gen_vendors"]:
            summary_lines.append(f"  * [{vendor_name(vendor)}](image-generations/{vendor}.md)")
            write_text(
                base / "image-generations" / f"{vendor}.md",
                build_capability_page(
                    env,
                    lang,
                    vendor,
                    "image_generations",
                    models_for_capability(env_index, vendor, "image_generations"),
                ),
            )

        if env_index["image_edit_vendors"]:
            summary_lines.append(f"* [{cfg['image_edit_root']}]({category_summary_target('image_edits')})")
            for vendor in env_index["image_edit_vendors"]:
                summary_lines.append(f"  * [{vendor_name(vendor)}](image-edits/{vendor}.md)")
                write_text(
                    base / "image-edits" / f"{vendor}.md",
                    build_capability_page(
                        env,
                        lang,
                        vendor,
                        "image_edits",
                        models_for_capability(env_index, vendor, "image_edits"),
                    ),
                )

        if env_index["audio_vendors"]:
            summary_lines.append(f"* [{cfg['audio_root']}]({category_summary_target('audio_transcriptions')})")
            for vendor in env_index["audio_vendors"]:
                summary_lines.append(f"  * [{vendor_name(vendor)}](audio-transcriptions/{vendor}.md)")
                write_text(
                    base / "audio-transcriptions" / f"{vendor}.md",
                    build_capability_page(
                        env,
                        lang,
                        vendor,
                        "audio_transcriptions",
                        models_for_capability(env_index, vendor, "audio_transcriptions"),
                    ),
                )

        write_text(base / "SUMMARY.md", "\n".join(summary_lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("sync-openapi")
    render = subparsers.add_parser("render-env")
    render.add_argument("env", choices=sorted(ENV_MODEL_FILES))
    args = parser.parse_args()

    if args.command == "sync-openapi":
        sync_openapi_templates()
    elif args.command == "render-env":
        render_env(args.env)


if __name__ == "__main__":
    main()
