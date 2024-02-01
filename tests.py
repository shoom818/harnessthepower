from hello_world import add
from hello_world import multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def multiply():
    assert multiply(4, 5) == 20
    assert multiply(2, -1) == -2
    assert multiply(-3, -3) == 9
