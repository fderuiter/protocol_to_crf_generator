# Integrating AI models into your development workflow

Call AI models in the tools you use every day.

## Using AI models in Copilot Chat

With GitHub Models extensions, you can ask specific models for help directly in Copilot Chat.

### Using the GitHub Models Copilot Extension

> **Note**
> The extension is in public preview and may change.

1. Install the GitHub Models Copilot Extension.
   - Copilot Pro users can install it personally.
   - Copilot Business or Enterprise users need an owner to enable Copilot Extensions and install the extension for the organisation.
2. Open any Copilot Chat implementation that supports extensions.
3. In the chat window, type `@models YOUR-PROMPT` and send your prompt.
   - Get model recommendations based on your criteria.
   - Execute prompts using a specific model.
   - List models available through GitHub Models.

### Using multiple model support in Copilot Chat

You can also choose a model for a conversation using multi-model Copilot Chat. See the official docs for details.

## Using AI models with GitHub Actions

Call models from your CI pipelines using the GitHub Actions token.

### Setting permissions

Enable the `models` permission in your workflow so that jobs can access the inference API.

### Writing your workflow file

```yaml
name: Use GitHub Models

on:
  workflow_dispatch:

permissions:
  models: read

jobs:
  call-model:
    runs-on: ubuntu-latest
    steps:
      - name: Call AI model
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          curl "https://models.github.ai/inference/chat/completions" \
             -H "Content-Type: application/json" \
             -H "Authorization: Bearer $GITHUB_TOKEN" \
             -d '{
              "messages": [
                  {
                     "role": "user",
                     "content": "Explain the concept of recursion."
                  }
               ],
               "model": "openai/gpt-4o"
            }'
```

## Using AI models from the command line

> **Note**
> The GitHub Models CLI extension is in public preview and may change.

Install the extension and prompt models from your terminal.

### Prerequisites

Install [GitHub CLI](https://github.com/cli/cli) and authenticate with `gh auth login`.

### Installing the extension

```shell
gh extension install https://github.com/github/gh-models
```

### Using the extension

- Run `gh models` to list commands.
- Start a chat: `gh models run` and select a model.
- Ask a single question: `gh models run MODEL "QUESTION"`.
- Pipe command output as context: `cat README.md | gh models run openai/gpt-4.1 "summarise this text"`.

