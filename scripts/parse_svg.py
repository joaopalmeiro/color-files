import lxml.etree as etree
import requests
from constants import PT_TEAMS_DATA
from utils import read_json

if __name__ == "__main__":
    teams = read_json(PT_TEAMS_DATA)

    with requests.Session() as s:
        for team in teams:
            r = s.get(team["logo_url"])

            tree = etree.fromstring(r.content)

            print(tree.xpath("//@fill"))
