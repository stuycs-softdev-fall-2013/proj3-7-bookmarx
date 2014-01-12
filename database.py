import sqlite3

userFields = ["username","token", "tags", "friends", "followed"]
tagFields = ["id", "name", "description", "color", "creator", "bookmarks", "privacy"]
bookmarkFields = ["id", "link", "tags", "title"]


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
    q = "select * from bookmarks where id=?"
    cursor = connection.execute(q, [id])
    results = [line for line in cursor]
    return results


def setUser(username, info):
    connection = sqlite3.connect('marx.db')
    q = "select * from users where username=?"
    cursor = connection.execute(q, [username])
    results = [line for line in cursor]
    for i in range(0,5):
        if results[0][i] != info[i]:
            q = "update users set %s=? where username=?"%(userFields[i])
            cursor = connection.execute(q, [info[i],username])
            connection.commit()


def setTag(id, info):
    connection = sqlite3.connect('marx.db')
    q = "select * from tags where id=?"
    cursor = connection.execute(q, [id])
    results = [line for line in cursor]
    for i in range(0,7):
        if results[0][i] != info[i]:
            q = "update tags set %s=? where id=?"%(tagFields[i])
            cursor = connection.execute(q, [info[i],id])
            connection.commit()


def setBookmark(id, info):
    connection = sqlite3.connect('marx.db')
    q = "select * from bookmarks where id=?"
    cursor = connection.execute(q, [id])
    results = [line for line in cursor]
    for i in range(0,4):
        if results[0][i] != info[i]:
            q = "update bookmarks set %s=? where id=?"%(bookmarkFields[i])
            cursor = connection.execute(q, [info[i],id])
            connection.commit()
