# RFP Writer — CrewAI Flow Demo

Five small examples that build up CrewAI's `Flow` primitives, from a simple
sequential chain to parallel branches.

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
   - `ANTHROPIC_API_KEY` — required for all examples
   - `OPENAI_API_KEY` — required for example one (review step uses GPT)

## Running an example

Each example takes an optional path to a brief directory (defaults to
`briefs/philly-portal`):

```sh
just one                      # default brief
just one briefs/data-warehouse
just two
just three
just four
just five
```

Outputs land in `responses/example_<n>-<brief>[-<step>].md`.

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

## Layout

```
example_one.py      # sequential chain, multi-provider
example_two.py      # router + revise loop
example_three.py    # human-in-the-loop
example_four.py     # web_search + MCP via Agent
example_five.py     # parallel fan-out, and_ join
plot.py             # render any flow's graph
utils.py            # read_brief / write_response
briefs/             # input briefs (committed)
responses/          # generated outputs (gitignored)
dist/               # rendered flow graphs (gitignored)
```
