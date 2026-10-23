"""Generate deterministic synthetic text, web-log, and power-plant datasets."""
from pathlib import Path
import csv
import random
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

def main():
    DATA.mkdir(parents=True, exist_ok=True)
    random.seed(4651)
    np.random.seed(4651)

    text = [
        "spark scales data processing across a cluster",
        "cloud systems process data with distributed computing",
        "machine learning learns patterns from prepared data",
        "spark supports scalable analytics and machine learning",
        "reliable data pipelines validate inputs and outputs",
    ]
    (DATA / "sample_text.txt").write_text("\n".join(text) + "\n", encoding="utf-8")

    with (DATA / "access.log").open("w", encoding="utf-8") as f:
        paths = ["/", "/products", "/search", "/login", "/health"]
        codes = [200, 200, 200, 302, 404, 500]
        for i in range(250):
            ip = f"192.0.2.{random.randint(1, 200)}"
            path = random.choice(paths)
            code = random.choice(codes)
            size = random.randint(120, 6000)
            f.write(f'{ip} - - [23/Oct/2026:09:{i%60:02d}:00 +0000] "GET {path} HTTP/1.1" {code} {size}\n')

    # Synthetic features with a stable, plausible relationship to output.
    n = 500
    temperature = np.random.uniform(2, 38, n)
    ambient_pressure = np.random.uniform(990, 1035, n)
    relative_humidity = np.random.uniform(25, 100, n)
    exhaust_vacuum = np.random.uniform(25, 80, n)
    noise = np.random.normal(0, 3.0, n)
    energy_output = (480 - 2.2 * temperature + 0.12 * ambient_pressure
                     - 0.35 * relative_humidity - 0.55 * exhaust_vacuum + noise)
    with (DATA / "power_plant.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["temperature", "ambient_pressure", "relative_humidity",
                         "exhaust_vacuum", "energy_output"])
        for row in zip(temperature, ambient_pressure, relative_humidity,
                       exhaust_vacuum, energy_output):
            writer.writerow([round(float(v), 3) for v in row])
    print(f"Sample datasets generated in {DATA}")

if __name__ == "__main__":
    main()
