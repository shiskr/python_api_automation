import unittest
import logging


logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class Requests_Manager(unittest.TestCase):
    def setUp(self):
        logging.info("## SETUP METHOD ##")

    def teardown(self):
        logging.info("## TEARDOWN METHOD ##")


if __name__ == '__main__':
    unittest.main()
