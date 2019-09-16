import unittest
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from test.test_Login import *
import HtmlTestRunner


example_tests = TestLoader().loadTestsFromTestCase(TestLogin)

suite = TestSuite([example_tests])

runner = HTMLTestRunner(output='example_suite')

h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="MyReport", add_timestamp=False).run(suite)


# Suite runner
# testmodules = [
#     'test.test_Login',
#     ]
#
# suite = unittest.TestSuite()
#
# for t in testmodules:
#     try:
#         # If the module defines a suite() function, call it to get the suite.
#         mod = __import__(t, globals(), locals(), ['suite'])
#         suitefn = getattr(mod, 'suite')
#         suite.addTest(suitefn())
#     except (ImportError, AttributeError):
#         # else, just load all the test cases from the module.
#         suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))
#
# unittest.TextTestRunner().run(suite)