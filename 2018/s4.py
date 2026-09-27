from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


OUTPUT_DIR = Path(__file__).parent


def main() -> None:
    a = np.linspace(0.0, 2.5, 1_200)
    b = np.linspace(-32, 3, 1_200)
    A, B = np.meshgrid(a, b)
    region = (A > 1) & (-2 * A**3 < B) & (B < 1 - 3 * A**2)

    fig, ax = plt.subplots(figsize=(6, 7))
    ax.contourf(A, B, region, levels=[0.5, 1], colors=["#8ecae6"], alpha=0.7)
    ax.plot(a, -2 * a**3, "k--", label=r"$b=-2a^3$")
    ax.plot(a, 1 - 3 * a**2, "k--", label=r"$b=1-3a^2$")
    ax.axvline(1, color="#666666", linestyle=":", label=r"$a=1$")
    ax.set_xlim(0.0, 2.5)
    ax.set_ylim(-32, 3)
    ax.set_xlabel(r"$a$")
    ax.set_ylabel(r"$b$")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "s4.svg")
    plt.close(fig)


if __name__ == "__main__":
    main()
