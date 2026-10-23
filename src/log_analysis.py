"""Summarize Apache-style access logs with Python for a portable small-data demo."""
import argparse
import csv
import re
from collections import Counter
from pathlib import Path

LOG_PATTERN = re.compile(r'"[A-Z]+ ([^ ]+) [^"]+" (\d{3}) (\d+|-)$')

def parse_log_line(line):
    match = LOG_PATTERN.search(line.strip())
    if not match:
        return None
    path, status, size = match.groups()
    return path, int(status), 0 if size == "-" else int(size)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/access.log")
    parser.add_argument("--output", default="outputs/log_summary.csv")
    args = parser.parse_args()
    path_counts, status_counts, bytes_by_path = Counter(), Counter(), Counter()
    total, invalid = 0, 0
    with open(args.input, encoding="utf-8") as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed is None:
                invalid += 1
                continue
            path, status, size = parsed
            path_counts[path] += 1
            status_counts[status] += 1
            bytes_by_path[path] += size
            total += 1
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["metric", "key", "value"])
        for key, value in sorted(path_counts.items()):
            writer.writerow(["requests_by_path", key, value])
        for key, value in sorted(status_counts.items()):
            writer.writerow(["responses_by_status", key, value])
        for key, value in sorted(bytes_by_path.items()):
            writer.writerow(["bytes_by_path", key, value])
        writer.writerow(["total_valid_requests", "all", total])
        writer.writerow(["invalid_lines", "all", invalid])
    print(f"Log summary saved to {out} ({total} valid rows, {invalid} invalid rows)")

if __name__ == "__main__":
    main()
