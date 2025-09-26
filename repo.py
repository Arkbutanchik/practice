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
    pass
def remove_reader(connect, pr):
    pass