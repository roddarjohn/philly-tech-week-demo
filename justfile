default:
    @just --list

# Install dependencies into a uv-managed venv
install:
    uv sync

# Run example one (sequential research → draft → review)
one DIR="":
    uv run python example_one.py {{DIR}}

# Run example two (research → draft → review → revise loop)
two DIR="":
    uv run python example_two.py {{DIR}}

# Run example three (research → draft → human review → optional revise)
three DIR="":
    uv run python example_three.py {{DIR}}

# Run example four (agency-research tool → research → draft)
four DIR="":
    uv run python example_four.py {{DIR}}

# Run example five (research → 3 parallel section writers → assemble)
five DIR="":
    uv run python example_five.py {{DIR}}

# Run example six (composed: top-level flow calls ResearchFlow then WriteFlow)
six DIR="":
    uv run python example_six.py {{DIR}}

# Run example seven (production: package combining everything)
seven DIR="":
    uv run python -m example_seven {{DIR}}

# List available briefs
briefs:
    @ls briefs

# Render the flow graph for example NAME (one/two/three) to dist/example_<NAME>.html
plot NAME="one":
    @uv run python plot.py example_{{NAME}}.py
