#Pytest file names should always start with test_ or end with _test
#Fucntion names should always start with test_
#Any code should be wrapped in a method
#Method name should have sense
#-k is a flag used for execution by method names (uses regular expression), -s logs in output,
#-v is for more info metadata
#run any specific file by mentioning filename e.g. py.test <filepath>
#Tag or mark testcases with @pytest.mark.smoke
#Run marked test cases with py.test -m <mark name> e.g - py.test -m smoke -v -s
#Skip testcases with @pytest.mark.skip
#Run the test without capturing it's status in report - @pytest.mark.xfail
#Fixtures are used as setup and teardown methods for test cases
#conftest file to generalize fixture and make it available to all test cases
#For optimization, wrap all the test cases in a class to avoid calling the fixture in each test case separately
#Above class - @pytest.mark.usefixtures("fixturename")
#If the fixture is to be called only once at the class initialization, then add the scope level to class
#@pytest.fixture(scope='class')
#Data driven and parameterization can be done in fixtures with return statements in list format
#

import pytest

@pytest.mark.smoke
def test_firstprogram(setup):
    print("Hello, this is first pytest program.")

@pytest.mark.xfail
def test_creditcard():
    print("Hello")

def test_crossbrowser(crossbrowser):
    print(crossbrowser[1])