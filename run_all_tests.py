#Nake sure that this file name does NOT begin with 'test', otherwise pycharm gets confused and thinks
#it is a test file and will complain that it did not collect any tests
#So, call it something like run_all_tests.py and not test_runner.py

import pytest

exit_code = pytest.main(["test_ecommerce.py",
                         "test_shopping_page.py",
                         "--gherkin-terminal-reporter",
                         "-v"
            ])

print(f"Pytest finished with exit code= {exit_code}")

