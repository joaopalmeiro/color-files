# color-files

Set of files with the colors relevant to a given topic.

## References

- [webcolors](https://github.com/ubernostrum/webcolors) package.
- [Partidos Políticos (CNE)](https://www.cne.pt/content/partidos-politicos-1).
- [Eleições para a Assembleia da República 2022 (CNE)](https://www.cne.pt/content/eleicoes-para-assembleia-da-republica-2022).
- [List of political parties in Portugal](https://en.wikipedia.org/wiki/List_of_political_parties_in_Portugal) Wikipedia page.
- [Quadro III - Partidos Inscritos no Tribunal Constitucional e Partidos Extintos](https://www.cne.pt/content/quadro-iii-partidos-inscritos-no-tribunal-constitucional-e-partidos-extintos).
- [Partidos registados e suas denominações, siglas e símbolos](https://www.tribunalconstitucional.pt/tc/partidos.html).

## Colors

- [Santa Clara](https://cdsantaclara.com/) website:
  - Red: `#e20226`.

## Files

- Colors:
  - `colors`: All colors (typically defined in brand guidelines and/or design systems).
    - `logo_colors`: Only the colors used in the (default) logo.
    - The other names/keys are based on the respective section titles (or similar).

## Development

- `pipenv install --dev --python 3.8`.
- `pipenv shell`.
- `make format`.

## Notes

- [Sublime Text](https://www.sublimetext.com/):
  - To configure the [CLI](https://www.sublimetext.com/docs/command_line.html), add `export PATH="/Applications/Sublime Text.app/Contents/SharedSupport/bin:$PATH"` to the `.zshrc` file.
  - [EditorConfig plugin](https://github.com/sindresorhus/editorconfig-sublime).
  - [JsPrettier plugin](https://packagecontrol.io/packages/JsPrettier) (Prettier).
- `pipenv install --dev black isort`.
- [lxml API Reference](https://lxml.de/apidoc/index.html).
- [XPath Syntax](https://www.w3schools.com/xml/xpath_syntax.asp).
- [Team Colors](https://teamcolors.jim-nielsen.com/) website.
- {[teamcolors](https://github.com/beanumber/teamcolors)} package.
- [SecretColors](https://github.com/secretBiology/SecretColors) package.
- [cssutils](https://cssutils.readthedocs.io/en/latest/) documentation:
  - [Parsers](https://cssutils.readthedocs.io/en/latest/parse.html).
  - [`parseStyle()` output](https://cssutils.readthedocs.io/en/latest/css.html#cssutils.css.CSSStyleDeclaration).
- [Full names](https://www.ligaportugal.pt/pt/liga/clube/20202021/liganos).
- [snippet generator](https://snippet-generator.app/) website.
- [Sort JSON objects](https://marketplace.visualstudio.com/items?itemName=richie5um2.vscode-sort-json):
  - It only rearranges keys, not array positions ([source](https://github.com/richie5um/vscode-sort-json/issues/40#issuecomment-713880886) issue). Alternative: [Sort JSON array](https://marketplace.visualstudio.com/items?itemName=fvclaus.sort-json-array).
- Regular expression for hexadecimal colors (can be used in VS Code): `#(?:[0-9a-fA-F]{3}){1,2}` ([source](https://stackoverflow.com/a/1636354)). Select All Occurrences of Find Match (`editor.action.selectHighlights`): `shift+cmd+l`.
- `date "+%A, %B %d, %Y" | tr -d "\n" | pbcopy`. The middle part is for removing newline characters (more info in [this answer](https://stackoverflow.com/a/3482322) on Stack Overflow).
- [remark-lint-link-text](https://github.com/mapbox/remark-lint-link-text):
  - `npm install --save-dev remark-cli @mapbox/remark-lint-link-text`.
  - [remark-cli](https://www.npmjs.com/package/remark-cli).
- [Variables for code snippets in VS Code](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_variables).
- `package-lock.json binary` to facilitate `git diff` ([source](https://twitter.com/okonetchnikov)).
- [npm-check](https://www.npmjs.com/package/npm-check) package (check for outdated, incorrect, and unused dependencies).
- [copy-text-to-clipboard](https://www.npmjs.com/package/copy-text-to-clipboard) package (lightweight).
- [mousetrap](https://www.npmjs.com/package/mousetrap) package (to handle keyboard shortcuts).
- [number-abbreviate](https://www.npmjs.com/package/number-abbreviate) package.
- [TinyColor](https://www.npmjs.com/package/tinycolor2) package (`npm i tinycolor2`).
- CNE: Comissão Nacional de Eleições.
