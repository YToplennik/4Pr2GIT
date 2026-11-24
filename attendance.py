from datetime import datetime

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
    }
    records.append(record)
    return record

def register_exit(records, name, exit_time):
    for record in reversed(records):
        if record["name"] == name and record["exit"] is None:
            record["exit"] = exit_time
            return record
    raise ValueError("Запись для выхода не найдена")

def main():
    print("Программа запущена")
    records = []
    
    register_entry(records, "Олег", "09:00")
    register_exit(records, "Олег", "10:30")
    
    duration = calculate_duration(records, "Олег")
    print(f"Олег был на практике {duration} минут")

if __name__ == "__main__":
    main()