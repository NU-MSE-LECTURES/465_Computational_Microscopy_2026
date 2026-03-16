"""Classify synthetic diffraction patterns with nearest-template matching."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT = Path(__file__).with_name("example_02_diffraction_nearest_template.png")


def make_pattern(size: int, template: str, rng: np.random.Generator) -> np.ndarray:
    axis = np.linspace(-1.0, 1.0, size)
    grid_x, grid_y = np.meshgrid(axis, axis)
    radius = np.sqrt(grid_x**2 + grid_y**2)
    angle = np.arctan2(grid_y, grid_x)

    base = np.exp(-((radius - 0.35) ** 2) / (2.0 * 0.05**2))
    if template == "ring":
        signal = base
    elif template == "sixfold":
        signal = base * (1.0 + 0.6 * np.cos(6.0 * angle) ** 10)
    elif template == "streaked":
        signal = base + 0.35 * np.exp(-(grid_y**2) / 0.015)
    else:
        raise ValueError(template)

    perturbation = rng.normal(0.0, 0.04, size=(size, size))
    image = np.clip(signal + perturbation, 0.0, None)
    return image / image.max()


def summarize(image: np.ndarray) -> np.ndarray:
    rows, cols = image.shape
    center = np.array([(rows - 1) / 2.0, (cols - 1) / 2.0])
    grid_y, grid_x = np.indices(image.shape)
    shifted_y = grid_y - center[0]
    shifted_x = grid_x - center[1]
    radius = np.sqrt(shifted_x**2 + shifted_y**2)
    angle = np.arctan2(shifted_y, shifted_x)

    return np.array(
        [
            image.mean(),
            image.std(),
            (image * radius).sum() / image.sum(),
            (image * np.cos(6.0 * angle)).mean(),
            (image * np.abs(shifted_y)).mean(),
        ]
    )


def main() -> None:
    rng = np.random.default_rng(12)
    templates = ["ring", "sixfold", "streaked"]
    template_images = {name: make_pattern(128, name, rng) for name in templates}
    template_features = {name: summarize(image) for name, image in template_images.items()}

    test_images = [make_pattern(128, name, rng) for name in templates for _ in range(4)]
    predicted_labels = []
    true_labels = [name for name in templates for _ in range(4)]

    for image in test_images:
        feature = summarize(image)
        distances = {name: np.linalg.norm(feature - template_features[name]) for name in templates}
        predicted_labels.append(min(distances, key=distances.get))

    fig, axes = plt.subplots(2, 3, figsize=(11, 7))
    for column, name in enumerate(templates):
        axes[0, column].imshow(template_images[name], cmap="magma")
        axes[0, column].set_title(f"Template: {name}")
        axes[0, column].axis("off")

    confusion = np.zeros((len(templates), len(templates)), dtype=int)
    for truth, prediction in zip(true_labels, predicted_labels):
        confusion[templates.index(truth), templates.index(prediction)] += 1

    axes[1, 0].imshow(confusion, cmap="Blues")
    axes[1, 0].set_title("Confusion matrix")
    axes[1, 0].set_xticks(range(len(templates)), templates, rotation=20)
    axes[1, 0].set_yticks(range(len(templates)), templates)
    for row in range(confusion.shape[0]):
        for col in range(confusion.shape[1]):
            axes[1, 0].text(col, row, confusion[row, col], ha="center", va="center")

    for name in templates:
        axes[1, 1].plot(template_features[name], marker="o", label=name)
    axes[1, 1].set_title("Template feature vectors")
    axes[1, 1].set_xlabel("Feature index")
    axes[1, 1].legend(frameon=False)

    accuracy = np.mean(np.array(true_labels) == np.array(predicted_labels))
    axes[1, 2].bar(templates, [np.mean(np.array(predicted_labels)[np.array(true_labels) == name] == name) for name in templates])
    axes[1, 2].set_ylim(0.0, 1.05)
    axes[1, 2].set_ylabel("Accuracy")
    axes[1, 2].set_title(f"Per-template accuracy\nOverall = {accuracy:.2f}")

    fig.tight_layout()
    fig.savefig(OUTPUT, dpi=200)
    print(f"Saved figure to {OUTPUT}")


if __name__ == "__main__":
    main()