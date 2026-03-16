"""Build a compact dashboard for final-project style metrics."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


OUTPUT = Path(__file__).with_name("example_02_results_summary_dashboard.png")


def main() -> None:
    results = pd.DataFrame(
        {
            "model": ["baseline", "physics_guided", "hybrid_ml"],
            "accuracy": [0.71, 0.81, 0.88],
            "runtime_s": [1.2, 2.8, 3.6],
            "mae": [0.23, 0.17, 0.12],
        }
    )

    rng = np.random.default_rng(2)
    residuals = {
        name: rng.normal(loc=0.0, scale=scale, size=200)
        for name, scale in zip(results["model"], [0.24, 0.18, 0.12], strict=True)
    }

    fig, axes = plt.subplots(2, 2, figsize=(10, 7))
    axes[0, 0].bar(results["model"], results["accuracy"], color="tab:blue")
    axes[0, 0].set_ylim(0.0, 1.0)
    axes[0, 0].set_title("Accuracy")

    axes[0, 1].bar(results["model"], results["runtime_s"], color="tab:orange")
    axes[0, 1].set_title("Runtime")
    axes[0, 1].set_ylabel("Seconds")

    axes[1, 0].bar(results["model"], results["mae"], color="tab:green")
    axes[1, 0].set_title("Mean absolute error")

    for name, values in residuals.items():
        axes[1, 1].hist(values, bins=20, alpha=0.5, label=name)
    axes[1, 1].set_title("Residual distributions")
    axes[1, 1].set_xlabel("Prediction error")
    axes[1, 1].legend(frameon=False)

    fig.tight_layout()
    fig.savefig(OUTPUT, dpi=200)
    print(results)
    print(f"Saved figure to {OUTPUT}")


if __name__ == "__main__":
    main()