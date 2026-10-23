# Professional Portfolio — Big Data & Machine Learning

A reproducible portfolio project demonstrating synthetic data generation, distributed processing with PySpark, server access-log analysis, regression modelling, and chart generation.

> **Data disclaimer:** The power-plant-like dataset is synthetic and created for educational demonstrations. Model metrics describe only this generated sample and must not be interpreted as real industrial performance.

## Project Highlights

- **Synthetic data generation** — create reproducible sample datasets.
- **Distributed computing** — perform a word-count task with PySpark.
- **Log analytics** — aggregate access logs and handle malformed rows.
- **Machine learning** — train and evaluate a regression model on held-out data.
- **Data visualization** — generate PNG charts for exploratory analysis and model evaluation.
- **Quality and reproducibility** — use fixed random seeds, automated tests, and documented setup steps.

## Technology Stack

`Python` · `PySpark` · `Pandas` · `NumPy` · `Matplotlib` · `Seaborn` · `scikit-learn` · `pytest` · `Google Colab`

## Visualizations

### Correlation Heatmap
![Correlation heatmap](outputs/charts/correlation_heatmap.png)

### Energy Output Distribution
![Energy output distribution](outputs/charts/energy_output_distribution.png)

### Actual vs. Predicted Values
![Actual vs predicted regression results](outputs/ml/actual_vs_predicted.png)

## Project Structure

```text
professional-portfolio-colab/
├── data/                   # Synthetic input datasets and sample access logs
├── docs/                   # Platform setup and project documentation
├── outputs/
│   ├── charts/             # Exploratory data analysis charts
│   ├── ml/                 # Model metrics and evaluation chart
│   └── word_count/         # PySpark word-count output
├── prompts/                # Prompts for optional AI-generated illustrations
├── src/                    # Data, Spark, log analysis, ML, and plotting scripts
├── tests/                  # Automated tests
├── Makefile
├── requirements.txt
└── README.md
```

## Run in Google Colab

1. Upload the project ZIP to Google Colab and extract it, or clone this repository.
2. Change into the project directory.
3. Install the dependencies:

   ```python
   %pip install -r requirements.txt
   ```

4. Run the project modules from a notebook cell:

   ```python
   !python -m src.generate_data
   !python -m src.word_count --input data/sample_text.txt --output outputs/word_count
   !python -m src.log_analysis --input data/access.log --output outputs/log_summary.csv
   !python -m src.ml_pipeline --input data/power_plant.csv --output-dir outputs/ml
   !python -m src.visualize --input data/power_plant.csv --output-dir outputs/charts
   !pytest -q
   ```

   **Note:** PySpark may require a compatible Java runtime. Cloud notebook environments can require additional Java or Spark configuration. See [`docs/PLATFORM_SETUP.md`](docs/PLATFORM_SETUP.md).

## Run Locally

Recommended: Python 3.10–3.12. For local Spark, Java 11 or 17 is recommended.

```bash
python -m venv .venv
python -m pip install --upgrade pip
pip install -r requirements.txt

python -m src.generate_data
python -m src.word_count --input data/sample_text.txt --output outputs/word_count
python -m src.log_analysis --input data/access.log --output outputs/log_summary.csv
python -m src.ml_pipeline --input data/power_plant.csv --output-dir outputs/ml
python -m src.visualize --input data/power_plant.csv --output-dir outputs/charts
pytest -q
```

For Windows 11 and Kali Linux instructions, see [`docs/PLATFORM_SETUP.md`](docs/PLATFORM_SETUP.md).

## Model Evaluation

The included example metrics file reports results from a generated sample:

| Metric | Example value |
|---|---:|
| Rows used | 500 |
| Training rows | 400 |
| Test rows | 100 |
| MAE | 4.076 |
| RMSE | 5.067 |
| R² | 0.963 |

These values are reproducible only for the included data and implementation. They are **not** claims about a real power plant or a production forecasting system. See [`outputs/ml/metrics.json`](outputs/ml/metrics.json).

## AI Illustration Prompts

The repository includes optional prompts for creating a project banner or supporting illustrations. The notebook/scripts do **not** generate AI artwork automatically; that requires a separate image-generation tool or API. See [`prompts/AI_IMAGE_PROMPTS.md`](prompts/AI_IMAGE_PROMPTS.md).

## Limitations

- Datasets are synthetic and intended for learning.
- Regression metrics depend on the generated sample.
- The regression model is a demonstration, not a validated production system.
- Local Spark requires a compatible Java runtime; cloud setup may vary by provider.

## License

No license is specified yet. Add a `LICENSE` file before presenting this repository as open source.
