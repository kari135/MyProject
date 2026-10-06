import math

def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return None
    if d == 0:
        return (-b / (2*a),)
    return ((-b + math.sqrt(d)) / (2*a), (-b - math.sqrt(d)) / (2*a))

if __name__ == "__main__":
    print(solve_quadratic(1, -3, 2))
