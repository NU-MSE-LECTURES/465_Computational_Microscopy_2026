"""Create a simple project scope table and milestone chart."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


OUTPUT = Path(__file__).with_name("example_01_project_timeline_and_scope.png")


def main() -> None:
    milestones = pd.DataFrame(
        [
            ("Question definition", 1, 2, "Scope"),
            ("Data curation", 2, 4, "Data"),
            ("Baseline analysis", 4, 6, "Methods"),
            ("Validation", 6, 8, "Methods"),
            ("Figures and report", 8, 10, "Communication"),
        ],
        columns=["task", "start_week", "end_week", "group"],
    )

    print(milestones)

    fig, ax = plt.subplots(figsize=(10, 4.5))
    colors = {"Scope": "tab:blue", "Data": "tab:orange", "Methods": "tab:green", "Communication": "tab:red"}
    for row_index, row in milestones.iterrows():
        ax.barh(
            y=row_index,
            width=row["end_week"] - row["start_week"],
            left=row["start_week"],
            color=colors[row["group"]],
            alpha=0.85,
        )

    ax.set_yticks(range(len(milestones)), milestones["task"])
    ax.set_xlabel("Course week")
    ax.set_title("Example final-project timeline")
    ax.invert_yaxis()

    fig.tight_layout()
    fig.savefig(OUTPUT, dpi=200)
    print(f"Saved figure to {OUTPUT}")


if __name__ == "__main__":
    main()