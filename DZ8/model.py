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
    db.pop(id)
    con.save_db(db)
    

def print_db(db):
    for k, v in db.items():
        print(k, v)