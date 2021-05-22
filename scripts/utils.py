import json
from pathlib import Path
from typing import Dict, List


def read_txt(path: Path) -> List[str]:
    with open(path) as file:
        lines = file.read().splitlines()

    return lines


def read_json(path: Path) -> List[Dict[str, str]]:
    with open(path) as file:
        data = json.load(file)

    return data
