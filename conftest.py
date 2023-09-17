import pytest

@pytest.fixture
def set_up():
    print("Start new test")
    yield
    print("Finish this test")
