# Prototyping with AI Models

Find and experiment with AI models for free using GitHub Models.

## Finding AI models

1. Go to <https://github.com/marketplace/models>.
2. Click **Model: Select a Model** at the top left of the page and choose a model.
3. Alternatively, choose **View all models** from the dropdown, select a model in Marketplace, then click **Playground**.

The model opens in the playground with details in the sidebar.

## Experimenting in the playground

The playground lets you adjust parameters and submit prompts to see model responses. It supports side‑by‑side comparison and is rate limited during the public preview.

Use the **Parameters** tab to modify inference settings and switch to the **Code** tab to view example code.

## Comparing models

Click **Compare** to open a second chat window and evaluate two models at once. Any parameters you set apply to both models.

## Evaluating AI models

Use the Comparisons view to run evaluators such as similarity, relevance and groundedness across prompt configurations. You can also define custom evaluators. See [Evaluating outputs](https://docs.github.com).

## Experimenting using the API

Free API usage lets you call models from your own code. Open the **Code** tab in the playground to see example requests and SDK options. Authenticate with a personal access token that has `models:read` permission.

## Saving and sharing experiments

Create presets to save parameters and optional chat history. Load, edit, share or delete presets from the **Preset** dropdown.

## Using the prompt editor

The prompt editor provides a dedicated single-turn view for refining prompts. Access it from the **Prompt editor** button in the playground.

## Experimenting in Visual Studio Code

Install the pre-release **AI Toolkit** extension. Authorise it with GitHub, then open the Model Catalog under **My models**. Choose **Try in playground** for remote models or **Download** to run locally.

## Going to production

Free usage has request and token limits. When ready for production, opt in to paid usage or bring your own API keys.

## Rate limits

Limits depend on model type and Copilot plan. Requests per minute, tokens per request and concurrent requests vary. See [Azure AI Foundry Models quotas and limits](https://learn.microsoft.com) for production tiers.

## Leaving feedback

Join the [GitHub Models discussion](https://github.com/github/community/discussions/55083) to share feedback and learn how others are using Models.
