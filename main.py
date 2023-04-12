# Импортируем необходимые библиотеки
import requests
import random
import time

# Открываем файл с логинами и паролями
with open("logins.txt", "r") as f:
    logins = f.readlines()

# Создаем сессию для отправки запросов
session = requests.Session()

# Перебираем логины и пароли по одному
for login in logins:
    # Разделяем логин и пароль по пробелу
    login = login.strip()
    username, password = login.split()

    # Генерируем случайные данные для регистрации
    first_name = random.choice(["Алексей", "Иван", "Петр", "Сергей", "Дмитрий"])
    last_name = random.choice(["Иванов", "Петров", "Сидоров", "Смирнов", "Новиков"])
    sex = random.choice(["2", "1"]) # 2 - мужской, 1 - женский
    bday = random.randint(1, 28) # День рождения
    bmonth = random.randint(1, 12) # Месяц рождения
    byear = random.randint(1980, 2005) # Год рождения

    # Формируем параметры для запроса регистрации
    params = {
        "act": "join",
        "al": "1",
        "bday": bday,
        "bmonth": bmonth,
        "byear": byear,
        "email": username,
        "first_name": first_name,
        "from_host": "vk.com",
        "from_protocol": "https",
        "ip_h": "", # Здесь нужно вставить значение ip_h из куки или скрытого поля формы регистрации
        "last_name": last_name,
        "lg_h": "", # Здесь нужно вставить значение lg_h из куки или скрытого поля формы регистрации
        "password": password,
        "regmode": "",
        "sex": sex,
        "to_host": "vk.com",
        "_origin": "https://vk.com"
    }

    # Отправляем запрос на регистрацию
    response = session.post("https://login.vk.com/?act=join", params=params)

    # Проверяем, что регистрация прошла успешно
    if response.status_code == 200 and response.text.startswith("<!>0<!>"):
        print(f"Успешно зарегистрирован аккаунт {username}")
    else:
        print(f"Не удалось зарегистрировать аккаунт {username}")

    # Ждем случайное время от 5 до 10 секунд перед следующим запросом
    time.sleep(random.randint(5, 10))
