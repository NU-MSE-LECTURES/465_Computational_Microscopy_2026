"""Cluster synthetic diffraction patterns with simple radial features.

This example is intentionally lightweight. It builds a small synthetic dataset,
extracts radial intensity profiles, reduces them with PCA, and groups them with
k-means. The figure is saved next to the script.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


OUTPUT = Path(__file__).with_name("example_01_diffraction_feature_clustering.png")


def synthetic_pattern(size: int, family: str, rng: np.random.Generator) -> np.ndarray:
    axis = np.linspace(-1.0, 1.0, size)
    grid_x, grid_y = np.meshgrid(axis, axis)
    radius = np.sqrt(grid_x**2 + grid_y**2)
    angle = np.arctan2(grid_y, grid_x)

    ring_center = rng.uniform(0.18, 0.6)
    ring_width = rng.uniform(0.03, 0.07)
    ring = np.exp(-((radius - ring_center) ** 2) / (2.0 * ring_width**2))

    if family == "polycrystal":
        pattern = ring
    elif family == "single_crystal":
        pattern = ring * (1.0 + 0.75 * np.cos(6.0 * angle) ** 8)
    elif family == "distorted":
        elliptical_radius = np.sqrt((1.3 * grid_x) ** 2 + (0.8 * grid_y) ** 2)
        pattern = np.exp(-((elliptical_radius - ring_center) ** 2) / (2.0 * ring_width**2))
    else:
        raise ValueError(f"Unknown family: {family}")

    background = 0.1 * np.exp(-(radius**2) / 0.35)
    noise = rng.normal(0.0, 0.03, size=(size, size))
    image = np.clip(pattern + background + noise, 0.0, None)
    return image / image.max()


def radial_profile(image: np.ndarray, bins: int = 24) -> np.ndarray:
    rows, cols = image.shape
    center_y = (rows - 1) / 2.0
    center_x = (cols - 1) / 2.0
    grid_y, grid_x = np.indices(image.shape)
    radius = np.sqrt((grid_x - center_x) ** 2 + (grid_y - center_y) ** 2)
    scaled_radius = radius / radius.max()
    edges = np.linspace(0.0, 1.0, bins + 1)

    profile = np.zeros(bins, dtype=float)
    for index in range(bins):
        mask = (scaled_radius >= edges[index]) & (scaled_radius < edges[index + 1])
        profile[index] = image[mask].mean() if np.any(mask) else 0.0
    return profile


def main() -> None:
    rng = np.random.default_rng(7)
    families = ["polycrystal", "single_crystal", "distorted"]
    images = []
    labels = []
    features = []

    for family in families:
        for _ in range(10):
            image = synthetic_pattern(128, family, rng)
            images.append(image)
            labels.append(family)
            features.append(radial_profile(image))

    feature_matrix = np.vstack(features)
    embedding = PCA(n_components=2, random_state=7).fit_transform(feature_matrix)
    clusters = KMeans(n_clusters=3, random_state=7, n_init=10).fit_predict(feature_matrix)

    fig, axes = plt.subplots(2, 3, figsize=(12, 7))
    for column, family in enumerate(families):
        example_index = labels.index(family)
        axes[0, column].imshow(images[example_index], cmap="magma")
        axes[0, column].set_title(family.replace("_", " "))
        axes[0, column].axis("off")

    color_map = {"polycrystal": "tab:blue", "single_crystal": "tab:orange", "distorted": "tab:green"}
    for family in families:
        mask = np.array(labels) == family
        axes[1, 0].scatter(
            embedding[mask, 0],
            embedding[mask, 1],
            label=family.replace("_", " "),
            alpha=0.8,
            color=color_map[family],
        )
    axes[1, 0].set_title("PCA embedding")
    axes[1, 0].set_xlabel("PC1")
    axes[1, 0].set_ylabel("PC2")
    axes[1, 0].legend(frameon=False)

    axes[1, 1].scatter(embedding[:, 0], embedding[:, 1], c=clusters, cmap="viridis", s=45)
    axes[1, 1].set_title("k-means clusters")
    axes[1, 1].set_xlabel("PC1")
    axes[1, 1].set_ylabel("PC2")

    for family in families:
        mean_profile = feature_matrix[np.array(labels) == family].mean(axis=0)
        axes[1, 2].plot(mean_profile, label=family.replace("_", " "))
    axes[1, 2].set_title("Mean radial profiles")
    axes[1, 2].set_xlabel("Radial bin")
    axes[1, 2].set_ylabel("Normalized intensity")
    axes[1, 2].legend(frameon=False)

    fig.tight_layout()
    fig.savefig(OUTPUT, dpi=200)
    print(f"Saved figure to {OUTPUT}")


if __name__ == "__main__":
    main()