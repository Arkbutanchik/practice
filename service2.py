def fetch_given_books(connect, pr):
    cursor = connect.cursor()
    cursor.execute(f"""SELECT b.title FROM books b JOIN loans l on b.id = l.book_id WHERE l.pr = {pr}""")
    return cursor.fetchall()

def fetch_booked_books(connect, pr):
    cursor = connect.cursor()
    cursor.execute(f"""SELECT b.title FROM books b JOIN holds h on b.id = h.book_id WHERE h.pr = {pr}""")
    return cursor.fetchall()

# def fetch_expired_books(connect):
#     import datetime
#     cursor = connect.cursor()
#     cursor.execute(f"""SELECT book_id, date FROM loans""")
#     for i in cursor.fetchall():

def auto_remove_booked(connect):
    cursor = connect.cursor()
    cursor.execute("""SELECT """)
    
def search(connect, title = None, author = None, genre = None):
    cursor = connect.cursor()
    cursor.execute(f"""SELECT * FROM books 
                   WHERE title = {f'{title} OR \'1\'=1' if bool(title) else title} AND
                   WHERE title = {f'{author} OR \'1\'=1' if bool(author) else author} AND
                   WHERE title = {f'{genre} OR \'1\'=1' if bool(genre) else genre}""")
    