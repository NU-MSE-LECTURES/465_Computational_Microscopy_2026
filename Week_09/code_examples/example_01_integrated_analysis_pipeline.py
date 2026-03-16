"""Run a compact microscopy-style analysis pipeline on a synthetic image."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import ndimage as ndi
from skimage import filters, measure, morphology


OUTPUT = Path(__file__).with_name("example_01_integrated_analysis_pipeline.png")


def make_image(size: int = 256, particles: int = 18, seed: int = 3) -> np.ndarray:
    rng = np.random.default_rng(seed)
    image = np.zeros((size, size), dtype=float)
    grid_y, grid_x = np.indices(image.shape)

    for _ in range(particles):
        center_y = rng.uniform(20, size - 20)
        center_x = rng.uniform(20, size - 20)
        sigma = rng.uniform(3.0, 9.0)
        amplitude = rng.uniform(0.6, 1.2)
        image += amplitude * np.exp(-((grid_x - center_x) ** 2 + (grid_y - center_y) ** 2) / (2.0 * sigma**2))

    noise = rng.normal(0.0, 0.08, size=image.shape)
    background = 0.15 * (grid_x / size)
    image = np.clip(image + noise + background, 0.0, None)
    return image / image.max()


def main() -> None:
    raw = make_image()
    denoised = ndi.gaussian_filter(raw, sigma=1.2)
    threshold = filters.threshold_otsu(denoised)
    mask = denoised > threshold
    cleaned = morphology.remove_small_objects(mask, min_size=40)
    labels = measure.label(cleaned)
    regions = measure.regionprops_table(labels, intensity_image=denoised, properties=("label", "area", "eccentricity", "mean_intensity"))
    table = pd.DataFrame(regions)

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes[0, 0].imshow(raw, cmap="gray")
    axes[0, 0].set_title("Raw synthetic image")
    axes[0, 0].axis("off")

    axes[0, 1].imshow(denoised, cmap="gray")
    axes[0, 1].set_title("Gaussian denoised")
    axes[0, 1].axis("off")

    axes[1, 0].imshow(cleaned, cmap="viridis")
    axes[1, 0].set_title(f"Segmented mask\nThreshold = {threshold:.2f}")
    axes[1, 0].axis("off")

    axes[1, 1].scatter(table["area"], table["mean_intensity"], c=table["eccentricity"], cmap="magma", s=60)
    axes[1, 1].set_title("Region summary")
    axes[1, 1].set_xlabel("Area (pixels)")
    axes[1, 1].set_ylabel("Mean intensity")

    fig.tight_layout()
    fig.savefig(OUTPUT, dpi=200)
    print(table.round(3).head())
    print(f"Saved figure to {OUTPUT}")


if __name__ == "__main__":
    main()