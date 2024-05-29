from random import randint
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    results = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for _ in range(10000):
        head_count = 0
        for i in range(10):
            if randint(0, 1):
                head_count += 1
        results[head_count] += 1 / 100
    return results


def draw_gaussian_distribution_graph() -> None:
    ls = sorted(flip_coin().items())
    x, y = zip(*ls)
    plt.plot(x, y)
    plt.show()
