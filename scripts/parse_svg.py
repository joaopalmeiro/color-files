from typing import Dict, List, Union

import lxml.etree as etree
import requests
from constants import PT_TEAMS_COLORS, PT_TEAMS_DATA
from utils import read_json, write_json

if __name__ == "__main__":
    teams = read_json(PT_TEAMS_DATA)
    teams_colors: List[Dict[str, Union[str, List[str]]]] = []

    with requests.Session() as s:
        for team in teams:
            r = s.get(team["logo_url"])

            tree = etree.fromstring(r.content)

            colors = tree.xpath("//@fill")

            unique_colors = list(set(map(str.lower, colors)))

            teams_colors.append({"name": team["name"], "colors": unique_colors})

    write_json(teams_colors, PT_TEAMS_COLORS)
