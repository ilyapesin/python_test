import pytest

@pytest.fixture()
def before_after():
    print("Before the test")
    yield
    print("\nAfter the test")

def test_demo1():
    assert 1==1

def test_demo2(before_after):
     assert 2==2
     