import math
import numpy as np

def main():
    x_values = np.linspace(0, 2, 1000)

    print("x \t sin(x)")

    for x in x_values:
        print(f"{x:.5f}\t {math.sin(x):.5f}")

if __name__ == "__main__":
    main()