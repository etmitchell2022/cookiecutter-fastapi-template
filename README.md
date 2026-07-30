# FastAPI Cookiecutter Template

Cookiecutter template for creating a FastAPI service with SQLAlchemy, Alembic,
Pydantic Settings, and optional Postgres, API-key authentication, and example
CRUD resources.

## Requirements

- Python 3.11 or newer
- [Cookiecutter](https://cookiecutter.readthedocs.io/)
- [Poetry](https://python-poetry.org/) for a local, non-Docker setup
- Docker and Docker Compose if Postgres is enabled

Install Cookiecutter with pipx, pip, or another preferred Python package
manager:

```bash
pipx install cookiecutter
```

## Create a project

Run Cookiecutter from the directory where you want the generated project to be
created:

```bash
cookiecutter /path/to/fastapi-template
```

When developing from this repository, run:

```bash
cookiecutter .
```

Cookiecutter prompts for the values in `cookiecutter.json` and creates a
directory named after the project slug. The default project name is `My
FastAPI Service`, which generates a directory named `my-fastapi-service`.

To accept all defaults without prompts:

```bash
cookiecutter --no-input /path/to/fastapi-template
```

Use `--output-dir` to choose the destination explicitly:

```bash
cookiecutter --output-dir ~/code /path/to/fastapi-template
```

## Template options

During generation, you can configure:

| Option | Effect |
| --- | --- |
| `project_name` and `project_slug` | Set the display name and generated directory/package name. |
| `project_description` | Set the project metadata and generated README description. |
| `author_name` and `author_email` | Set the Poetry package author. |
| `python_version` | Set the Python version constraint in `pyproject.toml`. |
| `include_postgres` | Adds the Postgres dependency and Docker Compose database. Choose `no` for SQLite. |
| `include_api_key_auth` | Keeps optional `X-API-Key` protection in the generated app. |
| `include_example_resource` | Keeps the example `items` model, schema, routes, and migration. |
| `initialize_git` | Runs `git init` in the generated project. |

The Postgres credentials, database name, and API port can also be customized
when prompted.

## Run the generated project

After generation, change into the new project and create its environment file:

```bash
cd my-fastapi-service
cp .env.example .env
```

With Postgres enabled, start the API and database with Docker:

```bash
docker compose up --build
docker compose exec api alembic upgrade head
```

With Postgres disabled, install dependencies and run migrations locally:

```bash
poetry install
poetry run alembic upgrade head
poetry run uvicorn app.app:app --reload --port 8000
```

The interactive API documentation is available at
`http://localhost:8000/docs` (or the custom API port you selected).

If API-key authentication was enabled, set `API_KEY` in `.env` and send it in
the `X-API-Key` header. Leave it blank for local development.

## Customize the generated service

Routes live in `app/routes`, request and response schemas in `app/schemas`,
and SQLAlchemy models in `app/models`. When adding a model, import it from
`alembic/env.py`, then create and apply a migration:

```bash
poetry run alembic revision --autogenerate -m "describe change"
poetry run alembic upgrade head
```

The generated project includes a health endpoint at `GET /health`. If the
example resource is enabled, it also includes CRUD endpoints under `/items`.

