import json
from pathlib import Path
from typing import Dict, List, Union

from constants import HEX_COLOR_RE


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


def normalize_hex(hex_value: str, raise_error: bool = True) -> str:
    match = HEX_COLOR_RE.match(hex_value)

    if match is None:
        if raise_error:
            raise ValueError(f"{repr(hex_value)} is not a valid hexadecimal color.")
        else:
            return hex_value

    hex_digits = match.group(1)

    if len(hex_digits) == 3:
        hex_digits = "".join(2 * s for s in hex_digits)

    return f"#{hex_digits}"
