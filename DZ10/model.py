import controller as con


def add(text):
    db = con.open_db()
    max_id = max(db)
    db[max_id + 1] = text
    con.save_db(db)
    con.open_db()
    return db


def del_value(text):
    id = int(text)
    db = con.open_db()
    del db[id]
    con.save_db(db)
    con.open_db()
    return db


def edit_value(text):
    db = con.open_db()
    list = text.split('-')
    id = int(list[0])
    value = list[1]
    db[id] = value
    con.save_db(db)
    con.open_db()
    return db


def print_db(db):
    for k, v in db.items():
        print(k, v)
