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
![Correlation heatmap](charts/correlation_heatmap.png)

### Energy Output Distribution
![Energy output distribution](charts/energy_output_distribution.png)

### Actual vs. Predicted Values
![Actual vs predicted regression results](charts/actual_vs_predicted.png)

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
