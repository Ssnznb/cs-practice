#Разбирает строку «город;температура;дата» в словарь. Негодная строка — ValueError.
def parse_record(line: str) -> dict:
    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError("Неверное количество полей")

    city, temp, date = (p.strip() for p in parts)

    if not city:
        raise ValueError("Пустой город")

    if not date:
        raise ValueError("Пустая дата")

    try:
        temperature = float(temp)
    except ValueError:
        raise ValueError("Температура должна быть числом")

    return {
        "city": city,
        "temperature": temperature,
        "date": date,
    }


#Разбирает строки журнала, пропуская пустые и негодные.
def read_valid(lines: list[str]) -> list[dict]:
    records = []

    for line in lines:
        if not line:
            continue

        try:
            record = parse_record(line)
        except ValueError:
            continue

        records.append(record)

    return records


#Средняя температура по каждому городу, округлённая до десятых.
def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        temperature = record["temperature"]

        totals[city] = totals.get(city, 0) + temperature
        counts[city] = counts.get(city, 0) + 1

    return {
        city: round(totals[city] / counts[city], 1)
        for city in totals
    }


#Город с наибольшей средней температурой. При равенстве — первый по алфавиту.
def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)

    if not averages:
        return ""

    return min(averages, key=lambda city: (-averages[city], city))