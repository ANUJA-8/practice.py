import pytest
@pytest.fixture(scope="session") #also run by using "session" it runs once
def newprework():   #this function is used in test_case2.py as argument 
    print("testing if the conftest.py is working")