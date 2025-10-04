import logging
from datetime import datetime

logging.basicConfig(
    format='%(asctime)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d'
)

logging.info('Это информационное сообщение')