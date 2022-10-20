import controller as con

def add (db):
    value = str(input('Введите информацию = '))
    max_id = max(db)
    db[max_id+1] = value
    con.save_db(db)
    con.open_db
    return db

def del_value (id):
    db = con.open_db()
    db.discard(id)
    con.save_db(db)

def edit_value ():
    db = con.open_db()
    print_db(db)
    id = int(input('Введите ИД записи которую надо редактировать - '))
    print(db[id])
    value = input('Введите новое значение - ')
    db[id] = value
    con.save_db(db)
    print_db(db)
    

def print_db(db):
    for k, v in db.items():
        print(k, v)