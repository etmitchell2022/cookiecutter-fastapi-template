# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Quick start

{% if cookiecutter.include_postgres == "yes" %}```bash
cp .env.example .env
docker compose up --build
docker compose exec api alembic upgrade head
{% else %}```bash
cp .env.example .env
poetry install
poetry run alembic upgrade head
{% endif %}
```

Open the interactive API docs at http://localhost:{{ cookiecutter.api_port }}/docs.

## Starter endpoints

- `GET /health` — public health check
{% if cookiecutter.include_example_resource == "yes" %}- `GET /items` — list items
- `GET /items/{item_id}` — get an item
- `POST /items` — create an item with `{ "name": "Example", "description": "..." }`
- `PATCH /items/{item_id}` — update an item
- `DELETE /items/{item_id}` — delete an item
{% endif %}

{% if cookiecutter.include_api_key_auth == "yes" %}Set `API_KEY` in `.env` to protect API routes with the `X-API-Key` header. Leave it blank for local development.
{% endif %}

## Structure

```text
fastapi-template/
├── app/
│   ├── app.py
│   ├── core/       # settings, database, authentication
│   ├── models/     # SQLAlchemy models
│   ├── schemas/    # Pydantic request/response schemas
│   ├── routes/     # API routers
│   └── services/   # business logic as the project grows
├── alembic/        # database migrations
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── .env.example
```

To add a resource, create matching files in `models`, `schemas`, and `routes`, register the router in `app/app.py`, import the model in `alembic/env.py`, and generate a migration with `poetry run alembic revision --autogenerate -m "describe change"`.
