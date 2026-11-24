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

if __name__ == "__main__":
    main()