from fastapi import {% if cookiecutter.include_api_key_auth == "yes" %}Depends, {% endif %}FastAPI
from fastapi.middleware.cors import CORSMiddleware

{% if cookiecutter.include_api_key_auth == "yes" %}from app.core.auth import require_api_key
{% endif %}
from app.core.config import settings
from app.routes.health_routes import router as health_router
{% if cookiecutter.include_example_resource == "yes" %}from app.routes.item_routes import router as item_router
{% endif %}

app = FastAPI(title=settings.APP_NAME, description="{{ cookiecutter.project_description }}", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS.split(","),
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["*"],
)

app.include_router(health_router)
{% if cookiecutter.include_example_resource == "yes" %}
app.include_router(
    item_router{% if cookiecutter.include_api_key_auth == "yes" %},
    dependencies=[Depends(require_api_key)]{% endif %}
)
{% endif %}
