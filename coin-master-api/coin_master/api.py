from fastapi import FastAPI
from structlog.stdlib import get_logger

from .config import CoinMasterSettings
from .logging_config import configure_logger
from .middleware import add_log_context
from .router import router

logger = get_logger()


def startup_event():
    settings = CoinMasterSettings()
    logger.info("Application starting", api_url=settings.exchange_base_url)


def shutdown_event():
    logger.info("Application shutting down")


def create_app() -> FastAPI:
    settings = CoinMasterSettings()
    configure_logger(level=settings.log_level, json_format=settings.json_logging)
    app = FastAPI()
    app.on_event("startup")(startup_event)
    app.on_event("shutdown")(shutdown_event)
    app.middleware("http")(add_log_context)
    app.include_router(router=router)

    return app
