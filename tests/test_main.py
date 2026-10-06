from src.main import solve_quadratic

def test_two_roots():
    assert solve_quadratic(1, -3, 2) == (2.0, 1.0)

def test_no_roots():
    assert solve_quadratic(1, 0, 1) is None
