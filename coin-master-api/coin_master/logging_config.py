import logging
import logging.config

import structlog


def configure_logger(level: str = "INFO", json_format=False):
    processors = [
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.UnicodeDecoder(),
        structlog.processors.CallsiteParameterAdder(
            [
                structlog.processors.CallsiteParameter.FILENAME,
                structlog.processors.CallsiteParameter.FUNC_NAME,
                structlog.processors.CallsiteParameter.LINENO,
            ]
        ),
        structlog.threadlocal.merge_threadlocal,
    ]

    if json_format:
        processors.extend(
            [
                structlog.processors.format_exc_info,
                structlog.processors.JSONRenderer(sort_keys=True),
            ]
        )
    else:
        processors.extend(
            [
                structlog.dev.ConsoleRenderer(sort_keys=True),
            ]
        )

    structlog.configure(
        processors=processors,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
    )

    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "plain": {
                    "format": "%(message)s",
                },
            },
            "handlers": {
                "default": {
                    "level": level,
                    "formatter": "plain",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                },
            },
            "loggers": {
                "": {
                    "handlers": ["default"],
                    "level": level,
                    "propagate": True,
                },
                "uvicorn": {
                    "handlers": [],
                    "level": "CRITICAL",
                    "propagate": True,
                },
            },
        }
    )
