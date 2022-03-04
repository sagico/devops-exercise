import time
from http import HTTPStatus

from fastapi import Request, Response
from starlette.middleware.base import RequestResponseEndpoint
from structlog.stdlib import get_logger
from structlog.threadlocal import bound_threadlocal

logger = get_logger()


def _log_request(request: Request, response: Response, duration: float):
    overall_status = HTTPStatus(response.status_code).phrase
    http_version = request.scope["http_version"]
    logger.info(
        f"{request.method} {request.url.path} {response.status_code}"
        f" {overall_status} HTTP/{http_version}",
        status=response.status_code,
        duration=duration,
    )


async def add_log_context(request: Request, call_next: RequestResponseEndpoint):
    with bound_threadlocal(
        client=f"{request.client.host}:{request.client.port}",
        method=request.method,
        url=request.url.path,
    ):
        start_time = time.perf_counter()
        response = await call_next(request)
        finish_time = time.perf_counter()

        _log_request(request, response, finish_time - start_time)

    return response
