# CrewAI Flow Demo - RFP Writer

Developed for Philly Tech Week.

Distributed under no license.

## Examples

| # | What it shows |
|---|---|
| `one`   | Three steps; Crew AI has a graph; observe OpenAI "revising" Claude |
| `two`   | Introduces a review flow |
| `three` | Introduces a human review step |
| `four`  | Introduces a custom tool + MCP; introduces full subagents |
| `five`  | In parallel |
| `six`   | Composability |
| `seven` | What this may look like in production |

## Setup

1. Install [uv](https://docs.astral.sh/uv/) and [just](https://github.com/casey/just).
2. Install dependencies:
   ```sh
   just install
   ```
3. Copy `.env.example` to `.env` and fill in your keys:
   ```sh
   cp .env.example .env
   ```
   
   To make all examples work, please update `.env` to include:
   - `ANTHROPIC_API_KEY` — required for all examples
   - `OPENAI_API_KEY` — required for example one (review step uses GPT)

## Running an example

Each example takes an optional path to a brief directory (defaults to
`briefs/philly-portal`):

```sh
just one
just two
just three
just four
just five
```

Outputs land in `responses/example_<n>/<brief>[-<step>].md`.

| | What it shows |
|---|---|
| `one`   | Sequential `@listen` chain across two providers (Claude → Claude → GPT polish) |
| `two`   | `@router` + `or_` revision loop with typed Pydantic state |
| `three` | `@human_feedback` decorator — human approves or describes revisions |
| `four`  | Anthropic `web_search` server tool + `Agent` with an MCP server (`mcp-server-time`) |
| `five`  | Three parallel section writers converged with `and_` |

## Plotting a flow

Renders an interactive HTML graph to `dist/` and opens it in your browser:

```sh
just plot one
just plot two
just plot three
just plot four
just plot five
```

## Adding a brief

Drop a directory into `briefs/`:

```
briefs/
  my-rfp/
    brief.md
```

Then run any example with `just <num> briefs/my-rfp`.


