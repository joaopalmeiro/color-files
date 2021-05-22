import json
from pathlib import Path
from typing import Dict, List, Union


def read_txt(path: Path) -> List[str]:
    with open(path) as file:
        lines = file.read().splitlines()

    return lines


def read_json(path: Path) -> List[Dict[str, str]]:
    with open(path) as file:
        data = json.load(file)

    return data


def write_json(data: List[Dict[str, Union[str, List[str]]]], output_path: Path) -> None:
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
