import sqlite3

userFields = ["username","token", "tags", "friends", "followed"]
tagFields = ["id", "name", "description", "color", "creator", "bookmrks", "privacy"]
bookmarks = ["id", "link", "tags", "title"]


def getUser(username):
    connection = sqlite3.connect('marx.db')
    q = "select * from users where username=?"
    cursor = connection.execute(q, [username])
    results = [line for line in cursor]
    return results


def getTag(id):
    connection = sqlite3.connect('marx.db')
    q = "select * from tags where id=?"
    cursor = connection.execute(q, [id])
    results = [line for line in cursor]
    return results


def getBookmark(id):
    connection = sqlite3.connect('marx.db')
    q = "select * from bookmark where id=?"
    cursor = connection.execute(q, [id])
    results = [line for line in cursor]
    return results


def setUser(username, info):
    connection = sqlite3.connect('marx.db')
    q = "select * from users where username=?"
    cursor = connection.execute(q, [username])
    results = [line for line in cursor]
    for i in range(0,5):
        if results[i] != info[i]:
            q = "update users set ?=? where username=?"
            cursor = connection.execute(q, [userfields[i],info[i],username])
    connection.commit()


def setTag(id, info):
    connection = sqlite3.connect('marx.db')
    q = "select * from tags where id=?"
    cursor = connection.execute(q, [id])
    results = [line for line in cursor]
    for i in range(0,7):
        if results[i] != info[i]:
            q = "update tags set ?=? where id=?"
            cursor = connection.execute(q, [tagfields[i],info[i],id])
    connection.commit()


def setBookmark(id, info):
    connection = sqlite3.connect('marx.db')
    q = "select * from bookmarks where id=?"
    cursor = connection.execute(q, [id])
    results = [line for line in cursor]
    for i in range(0,4):
        if results[i] != info[i]:
            q = "update bookmarks set ?=? where id=?"
            cursor = connection.execute(q, [bookmarkfields[i],info[i],id])
    connection.commit()
