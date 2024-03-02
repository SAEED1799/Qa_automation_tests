# test_runner.py
import json
import unittest
from concurrent.futures import ThreadPoolExecutor
from infra.browser_wrapper import BrowserWrapper
from tests.HomePage_tests import HomePageTests
from tests.FlowPackages_tests import packageTests
from tests.RentalCar_tests import RentalCarTest
from tests.AreaPage_tsets import AreaTests
from tests.OrderPageComplete_tests import OrderCompleteTests

try:
    with open('../infra/config.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
    raise  # Raise the error to halt execution if the file is essential for the script to run

list_test_cases_runer = [HomePageTests, packageTests, RentalCarTest, AreaTests, OrderCompleteTests]


def test_brawser_runer(browser):
    for test_cases in list_test_cases_runer:
        test_cases.browser = browser
        test_suite = unittest.TestLoader().loadTestsFromTestCase(test_cases)
        print(test_suite, browser)
        unittest.TextTestRunner().run(test_suite)


if __name__ == "__main__":
    browser_wrapper = BrowserWrapper()
    parallel = data["parallel"]
    serial = data["serial"]
    get_browser = data["browser_name"]
    browsers = data["browser_types"]
    if parallel:
        with ThreadPoolExecutor(max_workers=len(browsers)) as executor:
            executor.map(test_brawser_runer, browsers)
    elif serial:
        for browser in browsers:
            test_brawser_runer(browser)
    else:
        test_brawser_runer(get_browser)

# import json
# import unittest
# from concurrent.futures import ThreadPoolExecutor
#
# from infra.browser_wrapper import BrowserWrapper
# from tests.HomePage_tests import HomePageTests
# from tests.FlowPackages_tests import packageTests
# from tests.RentalCar_tests import RentalCarTest
# from tests.AreaPage_tsets import AreaTests
# from tests.OrderPageComplete_tests import OrderCompleteTests
#
# try:
#     with open('../infra/config.json') as f:
#         data = json.load(f)
# except FileNotFoundError:
#     print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
#     raise  # Raise the error to halt execution if the file is essential for the script to run
#
# list_test_cases_runer = [HomePageTests, packageTests, RentalCarTest, AreaTests, OrderCompleteTests]
#
#
# def test_browser_runer(browser=None):
#     print("i am in test browser runer")
#     for test_cases in list_test_cases_runer:
#         test_cases.browser = browser
#         test_suite = unittest.TestLoader().loadTestsFromTestCase(test_cases)
#         print(test_suite, browser)
#         unittest.TextTestRunner().run(test_suite)
#
#
# if __name__ == "__main__":
#     browser_wrapper = BrowserWrapper()
#     parallel = data["parallel"]
#     serial = data["serial"]
#     get_browser = data["browser"]
#     browsers = data["browser_types"]
#     if parallel:
#         with ThreadPoolExecutor(max_workers=len(browsers)) as executor:
#             executor.map(test_browser_runer, browsers)
#     elif serial:
#         for browser in browsers:
#             test_browser_runer(browser)
#     else:
#         test_browser_runer(get_browser)
