import logging
import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


logger = logging.getLogger("reconize.request")


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        started_at = time.perf_counter()

        try:
            response = await call_next(request)
        except Exception:
            duration = time.perf_counter() - started_at
            logger.exception(
                "%s %s failed after %.3fs",
                request.method,
                request.url.path,
                duration,
            )
            raise

        duration = time.perf_counter() - started_at
        logger.info(
            "%s %s -> %s in %.3fs",
            request.method,
            request.url.path,
            response.status_code,
            duration,
        )

        return response
