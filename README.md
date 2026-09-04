# ZEN

ZEN is a modular project manager and project generator. It creates, copies,
moves, and deletes project directories, and generates projects from validated
YAML templates. ZEN is not a code editor; generated files remain yours to edit
with your preferred editor.

## Features

- UI-independent `ZenEngine` for project lifecycle and generation workflows.
- `ZenKit` filesystem abstraction with consistent errors.
- Typed template model, YAML loader, Jinja rendering, and safe conditions.
- Boolean, integer, string, and choice inputs with defaults and validation.
- Conditional directories/files and argument-list external commands.
- CLI commands: `create`, `templates`, `list`, `init`, `delete`, `copy`, `move`.

## Installation and usage

Requires Python 3.10 or newer.

```powershell
python -m pip install -e .
zen templates
zen create --template python-cli --destination .\workspace
```

`zen create` interactively collects inputs. For automation, provide values:

```powershell
zen create -t python-cli -d .\workspace --var project_name=demo `
  --var description="Example application" --var include_tests=true
```

The bundled `python-cli` template creates a project directory beneath the
destination. The destination must be empty unless `--overwrite` is supplied.

## Template format

Each template is a directory containing `template.yaml`. The manifest schema
currently uses `template_version: 1`:

```yaml
template_version: 1
name: my-template
description: Example
inputs:
  - name: project_name
    type: string
    required: true
structure:
  - type: directory
    path: "{{ project_name }}/src"
  - type: file
    path: "{{ project_name }}/README.md"
    content: "# {{ project_name }}"
  - type: file
    path: "{{ project_name }}/Dockerfile"
    source: files/Dockerfile
    if: include_docker
commands:
  - command: [python, -m, venv, "{{ project_name }}/.venv"]
    if: include_venv
```

Inputs support `string`, `integer`, `boolean`, and `choice`; choices are
declared with `choices: [one, two]`. Optional `pattern` applies to strings.
Conditions support `==`, `!=`, boolean values, `and`, `or`, `not`, parentheses,
and structured `all`, `any`, `not`, `equals`, and `not_equals` mappings. Commands
are never passed through a shell, which avoids shell interpolation and injection.

For large file contents, use `source` with a path relative to the template
directory. All paths are required to be relative and cannot escape the
template or generated project root.

## Architecture

The CLI is an adapter around `ZenEngine`. The engine uses the typed internal
model from `TemplateLoader`, `TemplateRenderer`, and `ConditionEvaluator`, and
delegates filesystem work to `ZenKit`. A future GUI can call the same engine
without changing generation logic.

## Development

```powershell
python -m pip install -e .
python -m pytest
python -m zen --help
```

Tests use temporary directories and do not modify a user's projects.
