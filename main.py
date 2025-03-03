import random
import json
from datetime import datetime

cities = ["Уфа", "Москва", "Санкт-Петербург"]
positions = ["Младший специалист", "Старший специалист"]
names = ["Артур", "Владимир", "Иван"]
lastnames = ["Иванов", "Петров", "Попов"]
middle_names = ["Иванович", "Петрович"]
status = ["Закрыт", "Ждёт ответа", "Отложен"]
CSAT = [1, 2, 3, 4, 5]
messages_history = [
    "Здравствуйте!",
    "Здравствуйте! Ваш запрос принят, ожидайте ответа.",
    "Проблема решена. Спасибо за обращение!",
    "Мне нужна помощь",
    "Ожидайте ответа от нашего специалиста."
]


class User:
    def __init__(self, user_id, name, lastname, middlename, birthday, city):
        self.name = name
        self.lastname = lastname
        self.middlename = middlename
        self.birthday = birthday
        self.city = city
        self.user_id = user_id

    def __str__(self):
        return f"{self.user_id} {self.lastname} {self.name} {self.middlename} {self.city} {self.birthday}"

    def to_dict(self):
        return {
            'ID': self.user_id,
            'Имя': self.name,
            'Фамилия': self.lastname,
            'Отчество': self.middlename,
            'Город': self.city,
            'Дата рождения': self.birthday
        }


class Operator:
    def __init__(self, operator_id, first_name, last_name, middle_name, city, birth_date, position, experience):
        self.operator_id = operator_id
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.city = city
        self.birth_date = birth_date
        self.position = position
        self.experience = experience

    def __str__(self):
        return f"{self.operator_id} {self.last_name} {self.first_name} {self.middle_name} {self.city}, {self.birth_date} {self.position} {self.experience} лет"

    def to_dict(self):
        return {
            'ID': self.operator_id,
            'Имя': self.first_name,
            'Фамилия': self.last_name,
            'Отчество': self.middle_name,
            'Город': self.city,
            'Дата рождения': self.birth_date,
            'Позиция': self.position,
            'Опыт': self.experience
        }


class Chat:
    def __init__(self, chat_id, status_chat, operator, user, csat, history, date):
        self.chat_id = chat_id
        self.status_chat = status_chat
        self.operator = operator
        self.user = user
        self.csat = csat
        self.history = history
        self.date = date

    def update_status(self, new_status):
        self.status_chat = new_status

    def update_csat(self, new_csat):
        self.csat = new_csat

    def __str__(self):
        return f"Чат ID: {self.chat_id}, Статус: {self.status_chat}, Оператор: {self.operator.first_name} {self.operator.last_name}, Пользователь: {self.user.name} {self.user.lastname}, CSAT: {self.csat}, История: {self.history}, Дата: {self.date}"

    def to_dict(self):
        return {
            'ID чата': self.chat_id,
            'Статус': self.status_chat,
            'Оператор': self.operator.to_dict(),
            'Пользователь': self.user.to_dict(),
            'CSAT': self.csat,
            'История чата': self.history,
            'Дата': self.date
        }


#генерация случайных данных для пользователя и оператора
def generate_random_user(user_id):
    return User(user_id, random.choice(names), random.choice(lastnames), random.choice(middle_names),
                f"{random.randint(1, 31)}.{random.randint(1, 12)}.{random.randint(1950, 2005)}", random.choice(cities))


def generate_random_operator(operator_id):
    return Operator(operator_id, random.choice(names), random.choice(lastnames), random.choice(middle_names),
                    random.choice(cities),
                    f"{random.randint(1, 31)}.{random.randint(1, 12)}.{random.randint(1990, 2005)}",
                    random.choice(positions), random.randint(1, 3))

#эскпорт в json
def export_data(chats=None, users=None, operators=None, filename='platform_data.json'):
    data = {}
    if chats:
        data['chats'] = [chat.to_dict() for chat in chats]
    if users:
        data['users'] = [user.to_dict() for user in users]
    if operators:
        data['operators'] = [operator.to_dict() for operator in operators]

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f'Файл {filename} успешно создан!')

def export_chats_by_operator(operator_id, chats):
    filtered_chats = [chat.to_dict() for chat in chats if chat.operator.operator_id == operator_id]
    data = {'Фильтрация по оператору': filtered_chats}

    filename = f'chats_operator_{operator_id}.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f'Файл {filename} успешно создан!')


def export_chats_by_user(user_id, chats):
    filtered_chats = [chat.to_dict() for chat in chats if chat.user.user_id == user_id]
    data = {'Фильтрация по пользователю': filtered_chats}

    filename = f'chats_user_{user_id}.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f'Файл {filename} успешно создан!')



#генерация чата
def generate_random_chat(chat_id, operator, user):
    status_chat = random.choice(status)
    csat = None if status_chat != 'Закрыт' else random.choice(CSAT)
    history = "\n".join(
        [f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {random.choice(messages_history)}" for _ in range(2)]
    )
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return Chat(chat_id, status_chat, operator, user, csat, history, date)

#генерация id чата пользователя и оператора
def generate_num_chats(num_chats):
    users = [generate_random_user(i) for i in range(1, num_chats + 1)]
    operators = [generate_random_operator(i) for i in range(1, num_chats + 1)]
    chats = [generate_random_chat(i, random.choice(operators), random.choice(users)) for i in range(1, num_chats + 1)]
    return chats, users, operators


chats, users, operators = generate_num_chats(100)

for chat in chats:
 print(chat)

for user in users:
 print(user)

for operator in operators:
    print(operator)

export_chats_by_operator(1, chats)  # Выгрузит чаты оператора с ID = 1
export_chats_by_user(5, chats)  # Выгрузит чаты пользователя с ID = 5
export_data(chats=chats, filename='all_chats.json')
export_data(users=users, filename='users.json')
export_data(operators=operators, filename='operators.json')


#operator = Operator(1, "Иван", "Иванов", "Иванович", "19-09-2001", "Москва", "Москва", "Москва",)
#print(operator)
###user = User(1, "Иван", "Иванов", "Иванович", "19-09-2001", "Москва")
#print(user)
#print(random_user)
#print(random_operator)

#random_user = generate_random_user(1)
#random_operator = generate_random_operator(1)

#random_chat = generate_random_caht(1, random_operator, random_user)