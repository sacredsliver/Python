def open_db():
    with open('db.txt', 'r', encoding='utf-8') as data:
        onstring = data.read().split("\n")[:-1]
    db = dict()
    key = 1
    for item in onstring:
        value = item[3:]
        db[key] = value
        key += 1
    return db


def save_db(db):
    with open('db.txt', 'w', encoding='utf-8') as file:
        for key, value in db.items():
            file.write(f'{key}, {value}\n')
