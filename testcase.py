import calculator  # Assuming your calculator code is in a file named calculator.py

def add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(-1, 1) == -2
    assert calculator.subtract(0, 0) == 0

def multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, 1) == -1
    assert calculator.multiply(0, 5) == 0
