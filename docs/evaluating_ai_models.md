# Evaluating AI models

Test and compare AI model outputs using evaluators and scoring metrics in GitHub Models.

## Overview

GitHub Models provides a simple evaluation workflow that helps developers compare large language models (LLMs), refine prompts, and make data-driven decisions within the GitHub platform. You can use GitHub Models to experiment with new features or validate model changes by analyzing performance, accuracy, and cost through structured evaluation tools.

> **Tip**
> You can run evaluations directly from the command line using the `gh models eval` command. It uses the same evaluators as the UI so you can test your `.prompt.yml` file locally or in CI.

## Use cases for GitHub Models

Model behavior can vary widely based on the prompt, input, or configuration. GitHub Models helps you:

- Test and compare multiple LLMs across realistic use cases.
- Optimize prompt phrasing, temperature, and other parameters.
- Evaluate model outputs using structured, repeatable metrics.
- Make AI development integrated into your development workflow.

## Example scenario

Suppose you're building a feature to summarise customer feedback submitted through support tickets. These summaries will be used for internal reports, so the output must be clear and concise.

You want to:

- Experiment with different models and prompt configurations.
- Evaluate the best-performing configuration based on quality, consistency, and efficiency.
- Save the configuration to your repository for reuse and collaboration.

## Prompt testing in the Playground

To get started, open the Playground and configure a model. Define a system prompt like:

```text
You are a helpful assistant that summarises support ticket responses into concise summaries.
```

Enter a sample user prompt describing an issue, then run the model to see the generated summary. Refine the prompt until the output is concise and relevant.

### Using variables in prompts

At the bottom of the parameters settings, click **Create prompt.yml file** to open the Prompt view. Use variables in your prompt text wrapped in double curly braces, for example:

```text
Travel or shopping assistants using {{city}}, {{intent}}, and {{budget}} to tailor recommendations.
```

The variables will become parameters in compare mode so that you can reuse the prompt with different inputs.

## Adding test inputs

Switch to the Comparisons view to run structured tests. Each row represents an input and expected output. Add rows with realistic support messages and their ideal summaries.

## Adjusting model parameters

Create additional prompt configurations to compare models or parameter sets. For example, choose **PHI-4** from the model dropdown and set parameters like `max_tokens: 128` and `temperature: 0.3` to keep responses short and deterministic.

## Evaluating outputs

Apply evaluators such as **similarity**, **relevance**, and **groundedness** to measure how well each output matches your expectations. You can also define a custom prompt evaluator for specialised checks. Click **Run** to generate outputs and scores.

### Test case: PDF upload crash

Input: *The app crashes every time I try to upload a PDF from my phone. It works on desktop but not on mobile.*

Compare each model's output and evaluator scores to determine which configuration best summarises the issue.

### Test case: Dark mode request

Input: *Please add dark mode. It's very hard to use at night. My eyes hurt after prolonged use.*

Review the outputs and evaluator scores to judge which model captures the user's intent most effectively without unnecessary commentary.

## Save the configuration

After completing your evaluations, choose the best-performing model and prompt configuration. Add a descriptive name to the prompt file and commit the changes. This stores the model, parameters, and dataset as a reusable configuration file in your repository.

## Further reading

- [Prototyping with AI Models](prototyping_with_ai_models.md)
- [Optimizing your AI-powered app with Models](optimizing_with_models.md)
- [GitHub Models Overview](github_models.md)
