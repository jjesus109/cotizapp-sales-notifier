import logging

from app.config import Config


def configure_logger():
    conf = Config()
    logger = logging.getLogger()
    logger.setLevel(conf.log_level)
    ch = logging.StreamHandler()
    ch.setLevel(conf.log_level)
    formatter = logging.Formatter(
        "[%(levelname)s] %(asctime)s: %(name)s: %(message)s"
    )

    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger = logging.getLogger("databases")
    logger.setLevel(logging.ERROR)
