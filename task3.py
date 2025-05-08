phonebook = [
    {"ім'я": "Іван", "прізвище": "Петренко", "телефон": "123456789", "місто": "Київ"},
    {"ім'я": "Олена", "прізвище": "Іванова", "телефон": "987654321", "місто": "Львів"},
    {"ім'я": "Марія", "прізвище": "Коваль", "телефон": "111222333", "місто": "Київ"},
    {"ім'я": "Анна", "прізвище": "Мельник", "телефон": "444555666", "місто": "Одеса"}
]

# Оновлення або видалення
name = input("Введіть ім'я контакту для оновлення або видалення: ").strip()
found = None
for contact in phonebook:
    if contact["ім'я"].lower() == name.lower():
        found = contact
        break

if not found:
    print("Контакт не знайдено.")
else:
    action = input("Введіть 'оновити' або 'видалити': ").strip().lower()
    if action == "оновити":
        new_phone = input("Новий номер телефону: ")
        found["телефон"] = new_phone
        print("Контакт оновлено.")
    elif action == "видалити":
        confirm = input("Ви впевнені? Введіть 'так' для підтвердження: ")
        if confirm.lower() == "так":
            phonebook.remove(found)
            print("Контакт видалено.")
        else:
            print("Операцію скасовано.")

# Аналітика
cities = set()
city_counts = {}

for contact in phonebook:
    city = contact["місто"]
    cities.add(city)
    city_counts[city] = city_counts.get(city, 0) + 1

print("\nУнікальні міста:", cities)
print("Кількість контактів по містах:")
for city, count in city_counts.items():
    print(f"{city}: {count}")

if city_counts:
    max_city = max(city_counts, key=city_counts.get)
    print("Місто з найбільшою кількістю контактів:", max_city)
