# pyalign

[![Netlify Status](https://api.netlify.com/api/v1/badges/26ab67b9-6305-4776-829c-977042ec9d96/deploy-status)](https://app.netlify.com/sites/pyalign/deploys)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![main.yml](https://github.com/winstxnhdw/pyalign/actions/workflows/main.yml/badge.svg)](https://github.com/winstxnhdw/pyalign/actions/workflows/main.yml)
[![formatter.yml](https://github.com/winstxnhdw/pyalign/actions/workflows/formatter.yml/badge.svg)](https://github.com/winstxnhdw/pyalign/actions/workflows/formatter.yml)
[![dependabot.yml](https://github.com/winstxnhdw/pyalign/actions/workflows/dependabot.yml/badge.svg)](https://github.com/winstxnhdw/pyalign/actions/workflows/dependabot.yml)

> [!TIP]\
> This project was made before I found out about [table-magic](https://stevecat.net/table-magic/). Use that instead.

Aligns your multiline strings to a common character with [PyScript](https://pyscript.net/).

```text
| Action  | Command |                    | Action      | Command         |
| ------- | ------- |                    | -------     | -------         |
| Hello | `World` |             ---->    | Hello       | `World`         |
| This | `is an example` |               | This        | `is an example` |
| of terrible | `alignment` |            | of terrible | `alignment`     |
```

## Development

Install the following dependenci(es).

```bash
uv sync
```

Run the development server.

```bash
python -m http.server
```
