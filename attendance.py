def register_entry(records, name, entry_time):
    record = {
        "name": name,
        "entry": entry_time,
        "exit": None,
        "duration_minutes": None,
    }
    records.append(record)
    return record

def main():
    print("Программа запущена")

if __name__ == "__main__":
    main()