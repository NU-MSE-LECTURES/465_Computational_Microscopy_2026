"""Compare serial and parallel execution for a simple parameter sweep."""

from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from time import perf_counter

import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage as ndi


OUTPUT = Path(__file__).with_name("example_02_parallel_parameter_sweep.png")


def synthetic_image(size: int = 768, seed: int = 5) -> np.ndarray:
    rng = np.random.default_rng(seed)
    image = rng.normal(0.0, 0.05, size=(size, size))
    grid_y, grid_x = np.indices(image.shape)
    for sigma in (8, 14, 20, 26):
        image += np.exp(-((grid_x - (size * 0.35)) ** 2 + (grid_y - (size * 0.55)) ** 2) / (2.0 * sigma**2))
    return image


def evaluate_sigma(sigma: float) -> tuple[float, float]:
    image = synthetic_image()
    blurred = ndi.gaussian_filter(image, sigma=sigma)
    gradient_x = ndi.sobel(blurred, axis=0)
    gradient_y = ndi.sobel(blurred, axis=1)
    edge_strength = np.mean(np.hypot(gradient_x, gradient_y))
    return sigma, edge_strength


def main() -> None:
    sigmas = np.linspace(0.5, 4.0, 8)

    start = perf_counter()
    serial_results = [evaluate_sigma(sigma) for sigma in sigmas]
    serial_time = perf_counter() - start

    start = perf_counter()
    with ProcessPoolExecutor() as pool:
        parallel_results = list(pool.map(evaluate_sigma, sigmas))
    parallel_time = perf_counter() - start

    serial_sigmas, serial_scores = np.array(serial_results).T
    parallel_sigmas, parallel_scores = np.array(parallel_results).T

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))
    axes[0].plot(serial_sigmas, serial_scores, marker="o", label="serial")
    axes[0].plot(parallel_sigmas, parallel_scores, marker="s", linestyle="--", label="parallel")
    axes[0].set_xlabel("Gaussian sigma")
    axes[0].set_ylabel("Mean edge strength")
    axes[0].set_title("Sweep output")
    axes[0].legend(frameon=False)

    axes[1].bar(["serial", "parallel"], [serial_time, parallel_time], color=["tab:blue", "tab:orange"])
    axes[1].set_ylabel("Runtime (s)")
    axes[1].set_title("Execution time")

    fig.tight_layout()
    fig.savefig(OUTPUT, dpi=200)
    print(f"Serial runtime:   {serial_time:.3f} s")
    print(f"Parallel runtime: {parallel_time:.3f} s")
    print(f"Saved figure to {OUTPUT}")


if __name__ == "__main__":
    main()