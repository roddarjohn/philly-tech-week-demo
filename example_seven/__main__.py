from example_seven.main import RFPFlow
from utils import read_brief, read_company, write_response


def main() -> None:
    name, brief = read_brief()
    flow = RFPFlow()
    flow.kickoff(inputs={
        "name": name,
        "brief": brief,
        "company": read_company(),
    })
    output = write_response(f"example_seven-{name}", flow.state.draft)
    print(f"\nWrote {output}")


if __name__ == "__main__":
    main()
