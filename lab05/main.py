from pathlib import Path
from logstats import count_levels, top_errors, format_report, parse_event


def main():
    folder = Path(__file__).resolve().parent
    filename = input().strip()
    log_path = Path(filename)

    if not log_path.is_absolute():
        log_path = folder / log_path

    total = 0
    errors_count = 0
    broken_count = 0

    with open(log_path, encoding="utf-8") as log:
        for line in log:
            if not line.strip():
                continue

            total += 1
            try:
                event = parse_event(line)
                if event["level"] == "ERROR":
                    errors_count += 1
            except ValueError:
                broken_count += 1

    print(total)
    print(errors_count)
    print(broken_count)

    with open(log_path, encoding="utf-8") as log:
        counts = count_levels(log)

    with open(log_path, encoding="utf-8") as log:
        errors = top_errors(log, 3)

    report = format_report(counts, errors)

    with open(folder / "report.txt", "w", encoding="utf-8") as output:
        output.write(report)


if __name__ == "__main__":
    main()