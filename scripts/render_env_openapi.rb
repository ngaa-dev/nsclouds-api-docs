#!/usr/bin/env ruby

require "json"
require "fileutils"
require "yaml"

ROOT = File.expand_path("..", __dir__)
TEMPLATES_DIR = File.join(ROOT, "docs", "templates")
ENV_MODEL_FILES = {
  "cn" => File.join(ROOT, "scripts", "data", "cn_model_info.json"),
  "global" => File.join(ROOT, "scripts", "data", "global_model_info.json"),
}.freeze

BASE_SPECS = %w[openai anthropic google deepseek volcengine moonshotai minimax].freeze
BRAND_NAMES = {
  "anthropic" => "Anthropic",
  "dashscope" => "DashScope",
  "deepseek" => "DeepSeek",
  "google" => "Google",
  "minimax" => "MiniMax",
  "moonshotai" => "Moonshot AI",
  "openai" => "OpenAI",
  "volcengine" => "Volcengine",
  "xai" => "xAI",
  "xiaomi" => "Xiaomi",
  "zai" => "Z.AI",
}.freeze

CAPABILITY_CONFIG = {
  "chat" => {
    default_source: "openai",
    path: "/v1/chat/completions",
    tag_name: "chat_completions",
    x_parent: "chat_completions",
    icon: "brain",
  },
  "completions" => {
    default_source: "openai",
    path: "/v1/completions",
    tag_name: "completions",
    x_parent: "chat_completions",
    icon: "brain",
  },
  "messages" => {
    default_source: "anthropic",
    path: "/v1/messages",
    tag_name: "messages",
    x_parent: "chat_completions",
    icon: "brain",
  },
  "responses" => {
    default_source: "openai",
    path: "/v1/responses",
    tag_name: "responses",
    x_parent: "chat_completions",
    icon: "brain",
  },
  "image_generations" => {
    default_source: "openai",
    path: "/v1/images/generations",
    tag_name: "image_generations",
    x_parent: "image_generations",
    icon: "image",
  },
  "image_edits" => {
    default_source: "openai",
    path: "/v1/images/edits",
    tag_name: "image_edits",
    x_parent: "image_edits",
    icon: "image",
  },
  "audio_transcriptions" => {
    default_source: "openai",
    path: "/v1/audio/transcriptions",
    tag_name: "audio_transcriptions",
    x_parent: "audio_transcriptions",
    icon: "mic",
  },
  "gemini" => {
    default_source: "google",
    paths: [
      "/v1/models/{model}:generateContent",
      "/v1beta/models/{model}:generateContent",
      "/v1beta/models/{model}:streamGenerateContent",
    ],
    tag_name: "gemini_native",
    x_parent: "chat_completions",
    icon: "brain",
  },
}.freeze

GEMINI_NATIVE_ENDPOINTS = CAPABILITY_CONFIG.fetch("gemini").fetch(:paths).freeze
SHOW_TEXT_COMPLETIONS = false


def deep_copy(value)
  Marshal.load(Marshal.dump(value))
end


def load_yaml(path)
  YAML.load_file(path)
end


def load_json(path)
  JSON.parse(File.read(path))
end


def deep_transform_models!(value, example_model)
  case value
  when Hash
    value.each do |key, child|
      if %w[model modelVersion].include?(key.to_s) && child.is_a?(String)
        value[key] = example_model
      else
        deep_transform_models!(child, example_model)
      end
    end
  when Array
    value.each { |child| deep_transform_models!(child, example_model) }
  end
end


def top_tags(spec)
  deep_copy(spec.fetch("tags").first(5))
end


def source_specs(lang)
  @source_specs ||= {}
  @source_specs[lang] ||= BASE_SPECS.to_h do |vendor|
    [vendor, load_yaml(File.join(TEMPLATES_DIR, lang, "openapi", "#{vendor}.yaml"))]
  end
end


def capability_paths(capability)
  cfg = CAPABILITY_CONFIG.fetch(capability)
  cfg.key?(:paths) ? cfg.fetch(:paths) : [cfg.fetch(:path)]
end


def capability_title(capability, lang)
  return "Gemini Native" if capability == "gemini"

  titles = {
    "zh" => {
      "chat" => "Chat Completions",
      "completions" => "Text Completions",
      "messages" => "Messages",
      "responses" => "Responses",
      "image_generations" => "Image Generations",
      "image_edits" => "Image Edits",
      "audio_transcriptions" => "Audio Transcriptions",
    },
    "en" => {
      "chat" => "Chat Completions",
      "completions" => "Text Completions",
      "messages" => "Messages",
      "responses" => "Responses",
      "image_generations" => "Image Generations",
      "image_edits" => "Image Edits",
      "audio_transcriptions" => "Audio Transcriptions",
    },
  }
  titles.fetch(lang).fetch(capability)
end


def capability_description(capability, vendor, lang)
  brand = BRAND_NAMES.fetch(vendor, vendor)
  if lang == "zh"
    {
      "chat" => "#{brand} 的对话生成 API",
      "completions" => "#{brand} 的文本补全 API",
      "messages" => "#{brand} 的 Messages 协议 API",
      "responses" => "#{brand} 的 Responses 协议 API",
      "image_generations" => "#{brand} 的图像生成 API",
      "image_edits" => "#{brand} 的图像编辑 API",
      "audio_transcriptions" => "#{brand} 的音频转录 API",
      "gemini" => "#{brand} 的 Gemini 原生协议 API",
    }.fetch(capability)
  else
    {
      "chat" => "#{brand}'s chat completions API",
      "completions" => "#{brand}'s text completions API",
      "messages" => "#{brand}'s Messages protocol API",
      "responses" => "#{brand}'s Responses API",
      "image_generations" => "#{brand}'s image generations API",
      "image_edits" => "#{brand}'s image edits API",
      "audio_transcriptions" => "#{brand}'s audio transcriptions API",
      "gemini" => "#{brand}'s Gemini native API",
    }.fetch(capability)
  end
end


def source_has_path?(lang, vendor, path)
  source_specs(lang).fetch(vendor).fetch("paths").key?(path)
end


def preferred_source_for(vendor, capability, lang)
  return "google" if capability == "gemini"
  return vendor if source_specs(lang).key?(vendor) && capability_paths(capability).all? { |path| source_has_path?(lang, vendor, path) }

  CAPABILITY_CONFIG.fetch(capability).fetch(:default_source)
end


def vendor_tag(capability, vendor, lang)
  cfg = CAPABILITY_CONFIG.fetch(capability)
  {
    "name" => "#{cfg.fetch(:tag_name)}_#{vendor}",
    "x-parent" => cfg.fetch(:x_parent),
    "x-page-title" => BRAND_NAMES.fetch(vendor, vendor),
    "x-page-icon" => cfg.fetch(:icon),
    "description" => capability_description(capability, vendor, lang),
  }
end


def deep_merge_hash!(target, source)
  source.each do |key, value|
    if target[key].is_a?(Hash) && value.is_a?(Hash)
      deep_merge_hash!(target[key], value)
    elsif !target.key?(key)
      target[key] = deep_copy(value)
    end
  end
end


def canonical_example_model(entries)
  entries
    .map { |entry| entry["model_name"] }
    .compact
    .uniq
    .sort
    .first
end


def example_models_for_env(env)
  payload = load_json(ENV_MODEL_FILES.fetch(env))
  by_vendor = Hash.new { |hash, key| hash[key] = [] }
  payload.fetch("data", []).each do |item|
    info = item.fetch("model_info", {})
    vendor = info["original_provider"].to_s.strip.downcase
    next if vendor.empty?

    by_vendor[vendor] << {
      "model_name" => item["model_name"],
      "mode" => info["mode"],
      "endpoints" => info["supported_endpoints"] || [],
    }
  end

  by_vendor.transform_values do |entries|
    {
      "chat" => canonical_example_model(entries.select { |entry| entry["endpoints"].include?("/v1/chat/completions") }),
      "completions" => canonical_example_model(entries.select { |entry| entry["endpoints"].include?("/v1/chat/completions") }),
      "messages" => canonical_example_model(entries.select { |entry| entry["endpoints"].include?("/v1/messages") }),
      "responses" => canonical_example_model(entries.select { |entry| entry["endpoints"].include?("/v1/responses") }),
      "image_generations" => canonical_example_model(entries.select { |entry| entry["endpoints"].include?("/v1/images/generations") }),
      "image_edits" => canonical_example_model(entries.select { |entry| entry["endpoints"].include?("/v1/images/edits") }),
      "audio_transcriptions" => canonical_example_model(entries.select { |entry| entry["endpoints"].include?("/v1/audio/transcriptions") }),
      "gemini" => canonical_example_model(entries.select { |entry| (entry["endpoints"] & GEMINI_NATIVE_ENDPOINTS).any? }),
    }
  end
end


def apply_example_model!(operation, example_model)
  return if example_model.nil? || example_model.empty?

  content_nodes = []
  request_content = operation.dig("requestBody", "content")
  content_nodes.concat(request_content.values) if request_content.is_a?(Hash)

  responses = operation["responses"]
  if responses.is_a?(Hash)
    responses.each_value do |response|
      response_content = response["content"]
      content_nodes.concat(response_content.values) if response_content.is_a?(Hash)
    end
  end

  content_nodes.each do |content|
    examples = content["examples"]
    next unless examples.is_a?(Hash)

    examples.each_value do |example|
      next unless example.is_a?(Hash)

      value = example["value"]
      if value.is_a?(String)
        example["value"] = value.gsub(/"model":"[^"]+"/, "\"model\":\"#{example_model}\"")
      else
        deep_transform_models!(value, example_model)
      end
    end
  end
end


def rewrite_operation(operation, capability, vendor, example_model)
  new_operation = deep_copy(operation)
  new_operation["tags"] = ["#{CAPABILITY_CONFIG.fetch(capability).fetch(:tag_name)}_#{vendor}"]
  if new_operation["operationId"]
    new_operation["operationId"] = new_operation["operationId"].gsub(/_(openai|anthropic|google|deepseek|volcengine|minimax|moonshotai)\z/, "_#{vendor}")
  end
  apply_example_model!(new_operation, example_model)
  if capability == "chat" && vendor != "openai"
    request_examples = new_operation.dig("requestBody", "content", "application/json", "examples")
    request_examples&.delete("image_data_url_input")
  end
  if capability == "responses" && vendor != "openai"
    request_examples = new_operation.dig("requestBody", "content", "application/json", "examples")
    %w[image_input image_data_url_input file_input file_url_input file_data_input].each { |key| request_examples&.delete(key) }
    new_operation.dig("responses", "200", "content", "application/json", "examples")&.delete("image-input-response")
    new_operation.dig("responses", "200", "content", "application/json", "examples")&.delete("file-input-response")
  end
  new_operation
end


def extract_path_object(lang, source_vendor, path, capability, vendor, example_model)
  source_path = source_specs(lang).fetch(source_vendor).fetch("paths").fetch(path)
  rewritten = {}
  source_path.each do |method, operation|
    rewritten[method] = rewrite_operation(operation, capability, vendor, example_model)
  end
  rewritten
end


def capabilities_for_env(env)
  payload = load_json(ENV_MODEL_FILES.fetch(env))
  by_vendor = Hash.new { |hash, key| hash[key] = [] }
  payload.fetch("data", []).each do |item|
    info = item.fetch("model_info", {})
    vendor = info["original_provider"].to_s.strip.downcase
    next if vendor.empty?

    by_vendor[vendor] << {
      "model_name" => item["model_name"],
      "mode" => info["mode"],
      "endpoints" => info["supported_endpoints"] || [],
    }
  end

  public_caps = {}
  by_vendor.each do |vendor, entries|
    caps = []
    has_chat_completion = entries.any? { |entry| entry["endpoints"].include?("/v1/chat/completions") }
    caps << "chat" if has_chat_completion
    caps << "completions" if SHOW_TEXT_COMPLETIONS && has_chat_completion
    caps << "messages" if entries.any? { |entry| entry["endpoints"].include?("/v1/messages") }
    caps << "responses" if entries.any? { |entry| entry["endpoints"].include?("/v1/responses") }
    caps << "image_generations" if entries.any? { |entry| entry["endpoints"].include?("/v1/images/generations") }
    caps << "image_edits" if entries.any? { |entry| entry["endpoints"].include?("/v1/images/edits") }
    caps << "audio_transcriptions" if entries.any? { |entry| entry["endpoints"].include?("/v1/audio/transcriptions") }
    caps << "gemini" if entries.any? { |entry| (entry["endpoints"] & GEMINI_NATIVE_ENDPOINTS).any? }
    public_caps[vendor] = caps.uniq if caps.any?
  end
  public_caps
end


def build_vendor_spec(lang, vendor, capabilities, example_models)
  base_spec = deep_copy(source_specs(lang).fetch("openai"))
  spec = {
    "openapi" => base_spec.fetch("openapi"),
    "info" => deep_copy(base_spec.fetch("info")),
    "servers" => deep_copy(base_spec.fetch("servers")),
    "tags" => top_tags(base_spec),
    "paths" => {},
    "components" => {},
  }

  used_sources = []
  capabilities.each do |capability|
    source_vendor = preferred_source_for(vendor, capability, lang)
    used_sources << source_vendor
    spec["tags"] << vendor_tag(capability, vendor, lang)
    example_model = example_models.dig(vendor, capability)
    capability_paths(capability).each do |path|
      spec["paths"][path] = extract_path_object(lang, source_vendor, path, capability, vendor, example_model)
    end
  end

  used_sources.uniq.each do |source_vendor|
    deep_merge_hash!(spec["components"], source_specs(lang).fetch(source_vendor).fetch("components"))
  end
  unless SHOW_TEXT_COMPLETIONS
    schemas = spec.dig("components", "schemas")
    %w[CreateCompletionRequest CompletionChoice CompletionResponse].each { |schema| schemas&.delete(schema) }
  end

  spec
end

def prune_hidden_common_openapi!(path)
  return if SHOW_TEXT_COMPLETIONS

  common = load_yaml(path)
  schemas = common.dig("components", "schemas")
  %w[CreateCompletionRequest CompletionChoice CompletionResponse].each { |schema| schemas&.delete(schema) }
  File.write(path, YAML.dump(common))
end


def render_openapi(env, output_root)
  public_caps = capabilities_for_env(env)
  example_models = example_models_for_env(env)
  %w[zh en].each do |lang|
    lang_root = File.join(output_root, lang, "openapi")
    FileUtils.rm_rf(lang_root)
    FileUtils.mkdir_p(lang_root)
    common_path = File.join(lang_root, "_common.yaml")
    FileUtils.cp(File.join(TEMPLATES_DIR, lang, "openapi", "_common.yaml"), common_path)
    prune_hidden_common_openapi!(common_path)
    public_caps.each do |vendor, capabilities|
      next if capabilities.empty?

      spec = build_vendor_spec(lang, vendor, capabilities, example_models)
      File.write(File.join(lang_root, "#{vendor}.yaml"), YAML.dump(spec))
    end
  end
end


if ARGV.length != 2
  warn "usage: ruby scripts/render_env_openapi.rb <cn|global> <output_root>"
  exit 1
end

render_openapi(ARGV[0], ARGV[1])
