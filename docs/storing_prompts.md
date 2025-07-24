# Storing prompts in GitHub repositories

Store prompts directly in your GitHub repositories to leverage automated text summarisation and other AI-driven features.

## Benefits

- Easy integration with GitHub's suite of AI development tools.
- Simple and scalable for a range of use cases.
- Uses a widely supported format compatible with existing tooling.

## Supported file format

Prompts are stored as YAML files anywhere in the repository using the `.prompt.yml` or `.prompt.yaml` extension.

Example:

```yaml
name: Text Summarizer
description: Summarises input text concisely
model: gpt-4o-mini
modelParameters:
  temperature: 0.5
messages:
  - role: system
    content: You are a text summariser. Your only job is to summarise text given to you.
  - role: user
    content: |
      Summarise the given text, beginning with "Summary -":
      <text>
      {{input}}
      </text>
testData:
  - input: |
      The quick brown fox jumped over the lazy dog.
      The dog was too tired to react.
    expected: Summary - A fox jumped over a lazy, unresponsive dog.
evaluators:
  - name: Output should start with 'Summary -'
    string:
      startsWith: 'Summary -'
```

## Prompt structure

Prompts include:

- **Runtime information** such as system and user templates with `{{variable}}` placeholders.
- **Development information** like a human-readable name, description, model settings, sample data and evaluator details.

## Limitations

Prompts cannot be stored in proprietary or complex formats and do not support advanced templating languages.
