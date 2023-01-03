LOGGING_CONFIG = {
    "version": 1,
    "root": {
        "handlers": ["c_handler", "f_handler"],
        "filters": ["info_filter"],
        "level": "DEBUG"
    },
    "handlers": {
        "c_handler": {
            "formatter": "fmt",
            "class": "logging.StreamHandler",
            "level": "WARNING"
        },
        "f_handler": {
            "formatter": "fmt",
            "filters": ["info_filter"],
            "class": "logging_tools.MyTimedRotatingFileHandler",
            "filename": "logs/current_log.log",
            "when": "midnight",
            "interval": 1,
            "level": "DEBUG"
        }
    },
    "formatters": {
        "fmt": {
            "format": "%(asctime)s - %(levelname)s - %(message)s"
        }
    },
    "filters": {
        "info_filter": {
            "()": "logging_tools.InfoOnly"
        },
        "warning_filter": {
            "()": "logging_tools.WarningOnly"
        }
    }
}