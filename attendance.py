from datetime import datetime
LATE_MINUTES = 7
START_TIME = "09:00"

def parse_time(time_str):
    return datetime.strptime(time_str, "%H:%M")
    
def calculate_duration(records, name):
    for record in reversed(records):
        if record["name"] == name and record["exit"] is not None:
            start = parse_time(record["entry"])
            end = parse_time(record["exit"])
            delta = end - start
            record["duration_minutes"] = int(delta.total_seconds() // 60)
            return record["duration_minutes"]
    raise ValueError("Закрытая запись не найдена")

def register_entry(records, name, entry_time):
    record = {
        "name": name,
        "entry": entry_time,
        "exit": None,
        "duration_minutes": None,
        "late": is_late(entry_time)
    }
    records.append(record)
    return record

def register_exit(records, name, exit_time):
    for record in reversed(records):
        if record["name"] == name and record["exit"] is None:
            record["exit"] = exit_time
            return record
    raise ValueError("Запись для выхода не найдена")

def is_late(entry_time, start_time=START_TIME, late_minutes=LATE_MINUTES):
    entry_dt = parse_time(entry_time)
    start_dt = parse_time(start_time)
    delta = entry_dt - start_dt
    return int(delta.total_seconds() // 60) >= late_minutes

def main():
    print("Программа запущена")
    records = []
    
    register_entry(records, "Олег", "09:00")
    register_entry(records, "Василий", "09:15")
    register_exit(records, "Олег", "10:30")
    register_exit(records, "Василий", "11:00")
    
    print("Список посещений:")
    for r in records:
        print(r)

if __name__ == "__main__":
    main()