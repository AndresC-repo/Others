import json
from typing import List

from Configuration.pydantic_base import Config_file


def main() -> None:
    """Main function."""

    # Read data from a JSON file -> multiple configurations in one json file
    with open("./data.json") as file:
        data = json.load(file)
        Config_file: List[Config_file] = [Config_file(**item) for item in data]
        print(Config_file[0])
        # Config_file = Config_file(**data)  # One config


if __name__ == "__main__":
    main()