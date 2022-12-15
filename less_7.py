import logging

logging.basicConfig(level=logging.DEBUG, filename="test.log", filemode="w",
                    format="We have new msg:%(asctime)s:%(levelname)s - %(message)s")
logging.debug("debug text")
logging.info("info text")
logging.warning("warning text")
logging.error("error text")
logging.critical("critical text")

try:
    print(10/0)
except Exception:
    logging.exception("Exception text")
