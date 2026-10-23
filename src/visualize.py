"""Generate exploratory data-analysis charts as PNG image files."""
import argparse
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/power_plant.csv")
    parser.add_argument("--output-dir", default="outputs/charts")
    args = parser.parse_args()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.input)
    numeric = df.select_dtypes(include="number")
    if numeric.empty:
        raise ValueError("No numeric columns found for visualization.")

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(numeric.corr(), annot=True, fmt=".2f", cmap="vlag",
                center=0, square=True, ax=ax)
    ax.set_title("Feature Correlation — Synthetic Demo Data")
    fig.tight_layout()
    fig.savefig(out / "correlation_heatmap.png", dpi=180)
    plt.close(fig)

    target = "energy_output"
    if target in df.columns:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.hist(df[target], bins=24, edgecolor="black")
        ax.set(title="Energy Output Distribution (Synthetic Data)",
               xlabel="Energy output", ylabel="Number of rows")
        fig.tight_layout()
        fig.savefig(out / "energy_output_distribution.png", dpi=180)
        plt.close(fig)
    print(f"Charts saved to {out}")

if __name__ == "__main__":
    main()
