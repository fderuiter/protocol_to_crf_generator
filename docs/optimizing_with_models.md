# Optimizing your AI-powered app with Models

Learn how to test models and refine prompts using GitHub Models to build a better AI-powered application.

## Testing a prompt

The Comparisons view lets you tweak model parameters and prompts to observe how models respond.

1. **Create a sample repository** named `models-playground` and open the **Models** tab.
1. **Create a new prompt** from the *Prompts* section and choose a model.
1. **Write a system prompt** that instructs the model how to behave. For example:

```text
You are an expert at using the Git version control system. I will ask questions looking for guidance on the best way to perform tasks using Git, and you will give clear, step-by-step answers that explain each step you are recommending.
```

1. **Write a user prompt** with an input placeholder:

```text
I want to learn how to use Git from the command line.
```

1. **Enter sample input** using the `{{input}}` variable, e.g. `When should I use rebase or merge?`.
1. **Run the sample prompt** with the *Play* button and experiment with changes.

## Testing different models against a prompt

Use the **Comparisons** view to duplicate your prompt and select different models. Add rows of input such as:

- `How do I modify the most recent commit message in my current branch?`
- `How do I move a specific commit from one branch to a different branch?`
- `How do I find the author of a specific commit in a repository's history?`

Run the prompts to compare latency and token usage across models.

## Testing prompt variations with a specific model

If you have chosen a model, vary the user prompt to see how wording affects the output. Examples:

- `I want to learn how to use Git from the command line, but explain it to me like I am five years old.`
- `I want to learn how to use Git from the command line. Give me instructions in the form of a haiku.`

Run the prompts again and compare the responses.

## Evaluating model output

Track token usage and latency to manage cost and performance. Use **Evaluators** such as *String check* to verify that outputs contain required strings. For example, add an evaluator named "Amend check" with value `git commit --amend` and run the prompts to see which responses pass.

## Next steps

Store your chosen prompt configuration as a `.prompt.yml` file in the repository to enable version control and collaboration.

Join the [GitHub Models discussion](https://github.com/github/community/discussions/55083) to learn how others are using Models.
