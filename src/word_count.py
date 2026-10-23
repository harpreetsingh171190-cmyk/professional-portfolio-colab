"""Count words with PySpark; supports local Spark or a configured Spark cluster."""
import argparse
from pathlib import Path
from pyspark.sql import SparkSession
from pyspark import SparkConf

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/sample_text.txt")
    parser.add_argument("--output", default="outputs/word_count")
    parser.add_argument("--master", default="local[*]")
    args = parser.parse_args()

    input_path = str(Path(args.input).resolve())
    output_path = str(Path(args.output).resolve())
    spark = (SparkSession.builder.appName("PortfolioWordCount")
             .master(args.master).getOrCreate())
    try:
        counts = (spark.sparkContext.textFile(input_path)
                  .flatMap(lambda line: line.lower().split())
                  .map(lambda word: (word.strip(".,!?;:\"'()[]{}"), 1))
                  .filter(lambda pair: bool(pair[0]))
                  .reduceByKey(lambda a, b: a + b)
                  .sortBy(lambda pair: (-pair[1], pair[0])))
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        counts.map(lambda pair: f"{pair[0]}\t{pair[1]}").saveAsTextFile(output_path)
        print(f"Word counts saved to {output_path}")
    finally:
        spark.stop()

if __name__ == "__main__":
    main()
