#to run the test "parent folder>pytest -s test_case.py" where -s is use to see printed output 
#run single test=== parent folder> pytest -s test_case.py::test_initial_check
import pytest
@pytest.fixture(scope="module") #fixture has a scope with function/module == runs beofre every testfunc/runs once for that file
def prework():
    print("Anything")
    return True   #check by changing it to "False" it will gives error 
@pytest.fixture(scope="module")
def yield_test():    
    print("check if yield is working properly")
    yield           #yield is used to pouse the execution and it resumes after all other executions
    print("yield is working properly    ")
    '''Anything
check if yield is working properly
started with testing
.yield is working properly          #yield is run after the method run if we use function scope it will run after every method else it run once
testing if the conftest.py is working
check if yield is working properly
working on testing
.yield is working properly'''

def test_initial_check(prework,yield_test):  #if we are using fixture make sure the argument of the ficture function is given in test function
    print("started with testing")
    assert prework==True
def test_initial_check2(newprework,yield_test):  
    print("working on testing")

    '''
    fixture: scope="Module
    output: 
            test_case.py Anything      #it will run the fixture function only once
            started with testing
            .working on testing

    fixture: scope="function"
    output: 
            test_case.py Anything   #it will run the ficture function before every test function
            started with testing
            .Anything               #it will run the ficture function before every test function
            working on testing
    
    #if we ave a class and want to run fixture for entire class 
    fixture: scope=" class"  #class and module are almost same

    '''