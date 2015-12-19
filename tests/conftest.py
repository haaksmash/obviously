import pytest


@pytest.yield_fixture(autouse=True)
def another_print_method():
    print "another method fixture"
    yield
    print "another method fixture teardown"

@pytest.yield_fixture(autouse=True)
def aanother_print_method():
    print "aanother method fixture"
    yield
    print "aanother method fixture teardown"

