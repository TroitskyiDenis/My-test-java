import json
import os
from datetime import datetime

# Проверка наличия файла для хранения заметок
if not os.path.exists('tasks.json'):
    with open('tasks.json', 'w') as file:
        json.dump([], file)

# Функция для чтения заметок из файла
def read_tasks():
    with open('tasks.json', 'r') as file:
        notes = json.load(file)
        return notes

# Функция для сохранения заметок в файл
def save_tasks(task):
    with open('tasks.json', 'w') as file:
        json.dump(task, file, indent=4)

# Функция для создания новой заметки
def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        'id': len(read_tasks()) + 1,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes = read_tasks()
    notes.append(note)
    save_tasks(notes)
    print("Заметка успешно создана.")

# Функция для вывода списка всех заметок
def display_all_tasks():
    notes = read_tasks()
    if notes:
        for note in notes:
            print(f"ID: {note['id']} - Заголовок: {note['title']} - Дата: {note['timestamp']}")
    else:
        print("Нет заметок.")

# Функция для поиска заметки по ID
def find_note_by_id(note_id):
    notes = read_tasks()
    for note in notes:
        if note['id'] == note_id:
            return note
    return None

# Функция для редактирования заметки
def edit_task():
    task_id = int(input("Введите ID заметки для редактирования: "))
    task = find_note_by_id(task_id)
    if task:
        print(f"Текущий заголовок: {task['title']}")
        new_title = input("Введите новый заголовок (или Enter для оставления без изменений): ")
        print(f"Текущий текст заметки: {task['body']}")
        new_body = input("Введите новый текст заметки (или Enter для оставления без изменений): ")
        if new_title:
            task['title'] = new_title
        if new_body:
            task['body'] = new_body
        task['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_tasks(read_tasks())
        print("Заметка успешно отредактирована.")
    else:
        print("Заметка с указанным ID не найдена.")

# Функция для удаления заметки
def delete_note():
    task_id = int(input("Введите ID заметки для удаления: "))
    tasks = read_tasks()
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Заметка успешно удалена.")
            return
    print("Заметка с указанным ID не найдена.")

# Главная функция для работы с приложением
def main():
    while True:
        print("\nВыберите действие:")
        print("1. Создать заметку")
        print("2. Показать список всех заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            create_note()
        elif choice == '2':
            display_all_tasks()
        if choice == '1':
            create_note()
        elif choice == '2':
            display_all_tasks()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
     


        


            
