import unittest
import logging
import HtmlTestRunner

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class Requests_Manager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info("## SETUP METHOD ##")

    @classmethod
    def tearDownClass(cls):
        logging.info("## TEARDOWN METHOD ##")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())

    # HTML Test Runner
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/kumar.shishir/PycharmProjects/python_api_automation/reports/"))

    # for xml reporting
    # unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
    #     # these make sure that some options that are not applicable
    #     # remain hidden from the help menu.
    #     failfast=False, buffer=False, catchbreak=False)