import logging
import io
import unittest

logging.basicConfig(
    format='%(asctime)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d'
)

logging.info('Это информационное сообщение')


# --- тесты ---
class TestLogging(unittest.TestCase):
    def test_logging_message(self):
        stream = io.StringIO()
        handler = logging.StreamHandler(stream)
        formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d')
        handler.setFormatter(formatter)

        logger = logging.getLogger("test_logger")
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)

        logger.info("Тестовое сообщение")
        output = stream.getvalue()

        self.assertIn("Тестовое сообщение", output)


if __name__ == "__main__":
    unittest.main()
