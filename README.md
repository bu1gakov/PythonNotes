# PythonNotes
***Промежуточная контрольная работа по блоку
специализация***
Место в программе
Дается после блока программирования и курсов “Знакомство с языком
программирования Python” и “Java: знакомство и как пользоваться
базовыми API”.
*Информация о работе*
Включает в себя два задания: “Приложение заметки” – Урок 1, которое
выполняется на ЯП Python и “Магазин игрушек” – Урок 2, которое
выполняется на ЯП “Java”.
Задание 1. Приложение заметки (Python)
Информация о проекте
Необходимо написать проект, содержащий функционал работы с заметками.
Программа должна уметь создавать заметку, сохранять её, читать список
заметок, редактировать заметку, удалять заметку.
*Как сдавать проект*
Для сдачи проекта необходимо создать отдельный общедоступный
репозиторий (Github, gitlub, или Bitbucket). Разработку вести в этом
репозитории, использовать пул реквесты на изменения. Программа должна
запускаться и работать, ошибок при выполнении программы быть не должно.
Задание
Реализовать консольное приложение заметки, с сохранением, чтением,
добавлением, редактированием и удалением заметок. Заметка должна
содержать идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки. Сохранение заметок необходимо сделать в
формате json или csv формат (разделение полей рекомендуется делать через
точку с запятой). Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента.Например:
python notes.py add --title "новая заметка" –msg "тело новой заметки"
Или так:
python note.py
Введите команду: add
Введите заголовок заметки: новая заметка
Введите тело заметки: тело новой заметки
Заметка успешно сохранена
Введите команду:
При чтении списка заметок реализовать фильтрацию по дате.

Код: 

```
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
```