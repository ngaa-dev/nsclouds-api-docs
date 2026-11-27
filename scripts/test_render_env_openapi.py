"""Regression checks for provider-specific image documentation generation."""

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IMAGE_PATHS = ("/v1/images/generations", "/v1/images/edits")


def read_yaml(path):
    return json.loads(subprocess.check_output(
        ["ruby", "-r", "yaml", "-r", "json", "-e",
         "puts JSON.generate(YAML.load_file(ARGV.fetch(0)))", str(path)],
        text=True,
    ))


class ImageTemplateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        cls.specs = []
        for env in ("cn", "global"):
            output = Path(cls.temp.name) / env
            subprocess.run(
                ["ruby", str(ROOT / "scripts/render_env_openapi.rb"), env, str(output)],
                check=True,
            )
            for path in sorted(output.glob("*/openapi/*.yaml")):
                if path.stem != "_common":
                    cls.specs.append((env, path.parent.parent.name, path.stem, read_yaml(path)))

    def test_other_providers_do_not_inherit_gpt_image_parameters(self):
        covered = set()
        for env, lang, vendor, spec in self.specs:
            if vendor == "openai":
                continue
            for path in IMAGE_PATHS:
                if path not in spec["paths"]:
                    continue
                with self.subTest(env=env, lang=lang, vendor=vendor, path=path):
                    operation = spec["paths"][path]["post"]
                    self.assertNotIn("gpt-image-2", json.dumps(operation))
                    for content in operation["requestBody"]["content"].values():
                        self.assertIn("$ref", content["schema"])
                    if vendor in ("dashscope", "zai"):
                        self.assertNotIn("text/event-stream", operation["responses"]["200"]["content"])
                    covered.add((env, lang, vendor))
        self.assertTrue({(env, lang, vendor)
                         for env in ("cn", "global") for lang in ("en", "zh")
                         for vendor in ("dashscope", "zai")} <= covered)

    def test_openai_keeps_its_dedicated_image_operations(self):
        covered = set()
        for env, lang, vendor, spec in self.specs:
            if vendor != "openai":
                continue
            template = read_yaml(ROOT / "docs/templates" / lang / "openapi/openai.yaml")
            for path in IMAGE_PATHS:
                with self.subTest(env=env, lang=lang, path=path):
                    self.assertEqual(spec["paths"][path], template["paths"][path])
                    self.assertIn("gpt-image-2", json.dumps(spec["paths"][path]))
            covered.add(lang)
        self.assertEqual(covered, {"en", "zh"})


if __name__ == "__main__":
    unittest.main()
