"""Train and evaluate a reproducible regression model on the demo power-plant data."""
import argparse
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

FEATURES = ["temperature", "ambient_pressure", "relative_humidity", "exhaust_vacuum"]
TARGET = "energy_output"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/power_plant.csv")
    parser.add_argument("--output-dir", default="outputs/ml")
    args = parser.parse_args()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.input)
    required = set(FEATURES + [TARGET])
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    df = df.dropna(subset=FEATURES + [TARGET])
    X, y = df[FEATURES], df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=4651
    )
    model = make_pipeline(
        StandardScaler(),
        RandomForestRegressor(n_estimators=160, random_state=4651, n_jobs=-1)
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    metrics = {
        "rows_used": int(len(df)),
        "train_rows": int(len(X_train)),
        "test_rows": int(len(X_test)),
        "mae": float(mean_absolute_error(y_test, predictions)),
        "rmse": float(mean_squared_error(y_test, predictions) ** 0.5),
        "r2": float(r2_score(y_test, predictions)),
        "note": "Synthetic demonstration data; metrics are not industrial performance claims."
    }
    (out / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    fig, ax = plt.subplots(figsize=(7, 6))
    ax.scatter(y_test, predictions, alpha=0.7)
    low = min(float(y_test.min()), float(predictions.min()))
    high = max(float(y_test.max()), float(predictions.max()))
    ax.plot([low, high], [low, high], linestyle="--")
    ax.set(title="Actual vs Predicted Energy Output (Synthetic Data)",
           xlabel="Actual output", ylabel="Predicted output")
    fig.tight_layout()
    fig.savefig(out / "actual_vs_predicted.png", dpi=160)
    plt.close(fig)
    print(json.dumps(metrics, indent=2))
    print(f"Model metrics and chart saved to {out}")

if __name__ == "__main__":
    main()
