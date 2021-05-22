from typing import Dict, List, Sequence, Union

import cssutils
import lxml.etree as etree
import requests
from constants import PT_TEAMS_COLORS, PT_TEAMS_DATA
from utils import read_json, write_json


def process_styles(styles: Sequence[str]) -> List[str]:
    # Inline styles
    colors = [cssutils.parseStyle(style).getPropertyValue("fill") for style in styles]

    return colors


if __name__ == "__main__":
    cssutils.ser.prefs.minimizeColorHash = False

    teams = read_json(PT_TEAMS_DATA)
    teams_colors: List[Dict[str, Union[str, List[str]]]] = []

    with requests.Session() as s:
        for team in teams:
            r = s.get(team["logo_url"])

            tree = etree.fromstring(r.content)

            # `fill` attribute
            fill_colors = tree.xpath("//@fill")

            # `style` attribute
            inline_style_colors = tree.xpath("//@style")
            if inline_style_colors:
                inline_style_colors = process_styles(inline_style_colors)

            # Process colors
            all_colors = fill_colors + inline_style_colors
            unique_colors = list(set(map(str.lower, all_colors)))

            teams_colors.append({"name": team["name"], "colors": unique_colors})

    write_json(teams_colors, PT_TEAMS_COLORS)
