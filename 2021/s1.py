from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


OUTPUT_DIR = Path(__file__).parent


def plot_ab_region() -> None:
    a = np.linspace(-3, 3, 1_000)
    b = np.linspace(-3, 1, 1_000)
    A, B = np.meshgrid(a, b)
    region = (-A + B + 2 > 0) & (B < 0) & (A + B + 2 > 0)

    fig, ax = plt.subplots(figsize=(6, 5))
    ax.contourf(A, B, region, levels=[0.5, 1], colors=["#8ecae6"], alpha=0.7)
    ax.plot(a, a - 2, "k--", label=r"$b=a-2$")
    ax.plot(a, -a - 2, "k--", label=r"$b=-a-2$")
    ax.axhline(0, color="k", linestyle="--", label=r"$b=0$")
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 1)
    ax.set_xlabel(r"$a$")
    ax.set_ylabel(r"$b$")
    ax.set_aspect("equal")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "s1-1.svg")
    plt.close(fig)


def plot_xy_region() -> None:
    x = np.linspace(-4, 4, 1_200)
    y = np.linspace(-4, 12, 1_200)
    X, Y = np.meshgrid(x, y)
    abs_x = np.abs(X)
    lower = np.where(abs_x <= 1, X**2 - 2, X**2 - 2 * abs_x)
    upper = X**2 + 2 * abs_x
    region = (lower < Y) & (Y < upper)

    fig, ax = plt.subplots(figsize=(7, 6))
    ax.contourf(X, Y, region, levels=[0.5, 1], colors=["#8ecae6"], alpha=0.7)
    ax.plot(x, np.where(np.abs(x) <= 1, x**2 - 2, x**2 - 2 * np.abs(x)), "k--")
    ax.plot(x, x**2 + 2 * np.abs(x), "k--")
    ax.axvline(-1, color="#666666", linestyle=":")
    ax.axvline(1, color="#666666", linestyle=":")
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 12)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.set_aspect("equal")
    ax.grid(True)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "s1-2.svg")
    plt.close(fig)


def main() -> None:
    plot_ab_region()
    plot_xy_region()


if __name__ == "__main__":
    main()
