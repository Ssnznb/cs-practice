def csv_to_records(text: str) -> list[dict]:
    if not text.strip():
        return []

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    headers = [item.strip() for item in lines[0].split(",")]
    records = []

    for line in lines[1:]:
        values = [item.strip() for item in line.split(",")]
        record = {}

        for i, header in enumerate(headers):
            record[header] = values[i] if i < len(values) else ""

        records.append(record)

    return records


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list = None

    def parse_value(value):
        value = value.strip()

        if value.isdigit() or (
            value.startswith("-") and value[1:].isdigit()
        ):
            return int(value)

        try:
            if "." in value:
                return float(value)
        except ValueError:
            pass

        if value.lower() in ("true", "yes"):
            return True

        if value.lower() in ("false", "no"):
            return False

        return value

    for line in lines:
        line = line.split("#", 1)[0].strip()

        if not line:
            continue

        if line.startswith("- ") and current_list is not None:
            result[current_list].append(parse_value(line[2:]))
            continue

        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()

            if value == "":
                result[key] = []
                current_list = key
            else:
                result[key] = parse_value(value)
                current_list = None

    return result


def merge_by_key(
    rows: list[dict],
    extra: dict,
    key: str = "id"
) -> list[dict]:
    result = []

    for row in rows:
        additional = extra.get(row.get(key), {})

        merged = dict(additional)
        merged.update(row)

        result.append(merged)

    return result


import json


def records_to_json(records: list[dict]) -> str:
    return json.dumps(
        records,
        ensure_ascii=False,
        indent=2,
        sort_keys=True
    )