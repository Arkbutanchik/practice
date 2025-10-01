import sqlite3
connect = sqlite3.connect("db.db")
cursor = connect.cursor()

def hold_book(connect, pr, title, author):

    cursor.execute(f"SELECT free from holds")
    fetched = cursor.fetchall()
    free = fetched[0]

    cursor.execute(f"SELECT book_id from books JOIN readers ON loans.pr == readers.pr")
    fetched = cursor.fetchall()
    user_count = len(fetched) - 1

    if free <= 0:
        return False
    elif user_count >= 5:
        return False
    else:
        
        
    
    
def remove_hold(connect, pr, title, author):
    cursor.execute("DELETE FROM holds")
def take_book(connect, pr, title, author):
    pass
def give_back(connect, pr, title, author):
    pass
