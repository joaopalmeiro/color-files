import re
from pathlib import Path
from typing import Pattern

ROOT: Path = Path(__file__).resolve().parent.parent

PT_TEAMS_DATA: Path = ROOT / "data/pt_teams.json"
PT_TEAMS_COLORS: Path = ROOT / "data/pt_teams_colors.json"

# Source: https://github.com/ubernostrum/webcolors
HEX_COLOR_RE: Pattern[str] = re.compile(r"^#([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$")
