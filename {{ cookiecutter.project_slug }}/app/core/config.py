from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "{{ cookiecutter.project_name }}"
    DATABASE_URL: str = "{% if cookiecutter.include_postgres == 'yes' %}postgresql://{{ cookiecutter.postgres_user }}:{{ cookiecutter.postgres_password }}@localhost:5432/{{ cookiecutter.postgres_database }}{% else %}sqlite:///./app.db{% endif %}"
    ALLOWED_ORIGINS: str = "http://localhost:3000"
    API_KEY: str = ""

    model_config = {"env_file": ".env", "extra": "ignore"}


settings = Settings()
