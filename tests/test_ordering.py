import pytest

def setup_module():
    print "module setup"

def teardown_module():
    print "module teardown"


@pytest.yield_fixture(scope="session", autouse=True)
def print_session():
    print "session fixture"
    yield
    print "session fixture teardown"

@pytest.yield_fixture(scope="module", autouse=True)
def print_module():
    print "module fixture"
    yield
    print "module fixture teardown"

@pytest.yield_fixture(scope="class", autouse=True)
def print_class():
    print "class fixture"
    yield
    print "class fixture teardown"

@pytest.yield_fixture(autouse=True)
def teardown_only():
    yield
    print "tearing down only method"

@pytest.yield_fixture(autouse=True, params=["USD", "CAD"])
def print_method():
    print "method fixture"
    yield
    print "method fixture teardown"

class TestClass(object):

    def setup_method(self, method):
        print "method setup"

    def teardown_method(self, method):
        print "method teardown"

    def test_printer(self):
        print "test method"
