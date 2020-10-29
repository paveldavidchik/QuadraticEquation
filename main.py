import sys


def quadratic():
    a, b, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    x1, x2 = None, None
    if a == 0:
        return 'Уравнение не является квадратным'
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
    elif D == 0:
        x1 = x2 = (-b) / (2 * a)
    return x1, x2


if __name__ == '__main__':
    print(quadratic())
