import json
import os
import time
from datetime import datetime
from pathlib import Path

NOTES_FILE = "Zametki.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as f:
        return json.load(f)

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

def add_note(note):
    notes = load_notes()
    notes.append({"time": int(time.time()), "note": note})
    save_notes(notes)

def edit_note(index, new_note):
    notes = load_notes()
    if 0 <= index < len(notes):
        notes[index]["note"] = new_note
        save_notes(notes)

def read_notes():
    notes = load_notes()
    sorted_notes = sorted(notes, key=lambda x: x["time"])
    for note in sorted_notes:
        print(datetime.fromtimestamp(note["time"]).strftime("%H:%M:%S"), note["note"])

def delete_note(index):
    notes = load_notes()
    if 0 <= index < len(notes):
        del notes[index]
        save_notes(notes)

def main():
    while True:
        print("1. Добавить заметку")
        print("2. Редактировать заметку")
        print("3. Просмотр заметок")
        print("4. Удалить заметку")
        print("5. Выход")

        choice = int(input("Выбор команды: "))
        if choice == 1:
            note = input("Введите заметку: ")
            add_note(note)
        elif choice == 2:
            index = int(input("Введите индекс заметки для изменения: "))
            new_note = input("Введите новую заметку: ")
            edit_note(index, new_note)
        elif choice == 3:
            read_notes()
        elif choice == 4:
            index = int(input("Введите индекс заметки для удаления: "))
            delete_note(index)
        elif choice == 5:
            break
        else:
            print("Ошибка ввода, попробуйте ещё раз.")

if __name__ == "__main__":
    main()