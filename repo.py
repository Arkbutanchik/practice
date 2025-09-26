import db

def add_book(connect, title, author, genre, n):
    cursor = connect.cursor()
    cursor.execute(f"""INSERT INTO books (title, author, genre, total)
                   VALUES ({title}, {author}, {genre}, {n})""")
    connect.commit()
    
def remove_book(connect, title, author):
    cursor = connect.cursor()
    cursor.execute(f"""DELETE FROM books WHERE title = {title} AND author = {author}""")
    connect.commit()
    
def add_reader(connect, full_name, phone, age):
    cursor = connect.cursor()
    name = full_name.split()[0]
    surname = full_name.split()[1]
    pr = f"{name[0]}{surname[0]}{len(name)}{len(surname)}{phone[-4:]}"
    cursor.execute(f"""INSERT INTO readers (pr, full_name, phone, age)
                   VALUES ({pr}, {full_name}, {phone}, {age})""")    
    connect.commit()
    
def remove_reader(connect, pr):
    cursor = connect.cursor()
    cursor.execute(f"""DELETE FROM readers WHERE pr = {pr}""")
    connect.commit()
    