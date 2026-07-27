from pathlib import Path
import subprocess


PROJECT_ROOT = Path.cwd()


def remove_example_resource() -> None:
    if "{{ cookiecutter.include_example_resource }}" == "yes":
        return
    for relative_path in (
        "app/models/item.py",
        "app/schemas/item.py",
        "app/routes/item_routes.py",
        "alembic/versions/0001_create_items.py",
    ):
        (PROJECT_ROOT / relative_path).unlink(missing_ok=True)


def remove_api_key_auth() -> None:
    if "{{ cookiecutter.include_api_key_auth }}" == "yes":
        return
    (PROJECT_ROOT / "app/core/auth.py").unlink(missing_ok=True)


def remove_postgres() -> None:
    if "{{ cookiecutter.include_postgres }}" == "yes":
        return
    (PROJECT_ROOT / "docker-compose.yml").unlink(missing_ok=True)


def initialize_git() -> None:
    if "{{ cookiecutter.initialize_git }}" != "yes":
        return
    subprocess.run(["git", "init"], cwd=PROJECT_ROOT, check=True)


if __name__ == "__main__":
    remove_example_resource()
    remove_api_key_auth()
    remove_postgres()
    initialize_git()
