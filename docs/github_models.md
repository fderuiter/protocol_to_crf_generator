# GitHub Models Overview

GitHub Models is a suite of developer tools for experimenting with and evaluating large language models. It provides prompt management, side by side comparisons and structured metrics to help teams adopt AI responsibly.

## Capabilities

- **Prompt development** – Work with prompts in a structured editor supporting system instructions, test inputs and variables.
- **Model comparison** – Run identical prompts against multiple models and inspect the outputs side by side.
- **Evaluators** – Score similarity, relevance and groundedness to track performance over time.
- **Prompt configurations** – Save settings as `.prompt.yml` files in the repository for review and reproducibility.
- **Production integration** – Use saved configurations through SDKs or the REST API.

## Enabling GitHub Models

Individuals can enable GitHub Models from the repository settings under **Models**. For organizations, an enterprise owner first enables the feature so organization owners can configure allowed models.

## Prompts

Each prompt configuration lives as a `.prompt.yml` file defining the model, parameters and test inputs. Manage, edit and organize these files to support experimentation or production use.

## Comparisons

Use the Comparisons view to evaluate multiple configurations across rows of input data. The view displays evaluator scores, making it ideal for refining prompts and avoiding regressions.

## Playground

The Playground lets you quickly explore models and test prompt ideas in real time. Adjust parameters and compare responses interactively during early experimentation.

## Billing

See [About billing for GitHub Models](https://docs.github.com) for details on pricing.

## Community

Join the [GitHub Models discussion](https://github.com/github/community) to share feedback and learn how others use the tooling.

