import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log",
                    filemode="a",
                    format="Наша ошибка: %(asctime)s:%(levelname)s:%(message)s"
                    )
try:
    print(name)
except Exception:
    logging.exception("Exception")
try:
    print("2" - 3)
except Exception:
    logging.exception("Exception")
