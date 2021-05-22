import lxml.etree as etree
import requests

if __name__ == "__main__":
    with requests.Session() as s:
        r = s.get(
            "https://upload.wikimedia.org/wikipedia/en/e/e1/Sporting_Clube_de_Portugal_%28Logo%29.svg"
        )

        tree = etree.fromstring(r.content)

        print(tree.xpath("//@fill"))
