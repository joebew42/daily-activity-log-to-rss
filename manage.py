#!/usr/bin/env python

import sys
import unittest

import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))


def run(tests):
    unittest.TextTestRunner(verbosity=2).run(tests)


def unit_tests():
    from rest.rest_app_tests import RestTest
    from actions_tests import GetRssFromDailyUrlTest
    from utils_tests import DailyToRssTest

    return unittest.TestSuite([
        __load_test(RestTest),
        __load_test(GetRssFromDailyUrlTest),
        __load_test(DailyToRssTest),
    ])


def integration_tests():
    from infrastructure_tests import HTTPDailyRepositoryTest

    return unittest.TestSuite([
        __load_test(HTTPDailyRepositoryTest)
    ])


def __load_test(test_case_class):
    return unittest.TestLoader().loadTestsFromTestCase(test_case_class)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        exit()

    if 'test' == sys.argv[1]:
        run(unit_tests())

    if 'integration-test' == sys.argv[1]:
        run(integration_tests())

    if 'server' == sys.argv[1]:
        from rest.rest_app import app

        app.run(host='0.0.0.0')
