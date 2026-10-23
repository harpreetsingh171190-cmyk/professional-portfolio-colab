install:
	python -m pip install -r requirements.txt
data:
	python -m src.generate_data
charts: data
	python -m src.visualize
model: data
	python -m src.ml_pipeline
test:
	pytest -q
