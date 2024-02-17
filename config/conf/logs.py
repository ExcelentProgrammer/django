import logging

logging.basicConfig(
    filename=f"./logs/django.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
