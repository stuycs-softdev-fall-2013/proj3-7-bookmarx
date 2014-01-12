import sqlite3

userFields = ["username","token", "tags", "friends", "followed"]
tagFields = ["id", "name", "description", "color", "creator", "bookmarks", "privacy"]
bookmarkFields = ["id", "link", "tags", "title"]

################################ GET FUNCTIONS #################################
#Get functions return 0 if the entry doesn't exist

def getUser(username):
    connection = sqlite3.connect('marx.db')
    q = "select * from users where username=?"
    cursor = connection.execute(q, [username])
    results = [line for line in cursor]
    if len(results) == 1:
        return results[0]
    else:
        return 0 


def getTag(id):
    connection = sqlite3.connect('marx.db')
    q = "select * from tags where id=?"
    cursor = connection.execute(q, [id])
    results = [line for line in cursor]
    if len(results) == 1:
        return results[0]
    else:
        return 0


def getBookmark(id):
    connection = sqlite3.connect('marx.db')
    q = "select * from bookmarks where id=?"
    cursor = connection.execute(q, [id])
    results = [line for line in cursor]
    if len(results) == 1:
        return results[0]
    else:
        return 0


############################### SET FUNCTIONS ##################################
#Set functions return 0 if entry doesn't exist, 1 if the number of fields
#provided in info is incorrect, and 2 if there is no problem

def setUser(username, info):
    if len(info) != len(userFields):
        return 1
    connection = sqlite3.connect('marx.db')
    q = "select * from users where username=?"
    cursor = connection.execute(q, [username])
    results = [line for line in cursor]
    if len(results) == 0:
        return 0
    for i in range(0,len(userFields) ):
        if results[0][i] != info[i]:
            q = "update users set %s=? where username=?"%(userFields[i])
            cursor = connection.execute(q, [info[i],username])
            connection.commit()
    return 2


def setTag(id, info):
    if len(info) != len(tagFields):
        return 1
    connection = sqlite3.connect('marx.db')
    q = "select * from tags where id=?"
    cursor = connection.execute(q, [id])
    results = [line for line in cursor]
    if len(results) == 0:
        return 0
    for i in range(0,len(tagFields) ):
        if results[0][i] != info[i]:
            q = "update tags set %s=? where id=?"%(tagFields[i])
            cursor = connection.execute(q, [info[i],id])
            connection.commit()
    return 2


def setBookmark(id, info):
    if len(info) != len(bookmarkFields):
        return 1
    connection = sqlite3.connect('marx.db')
    q = "select * from bookmarks where id=?"
    cursor = connection.execute(q, [id])
    results = [line for line in cursor]
    if len(results) == 0:
        return 0
    for i in range(0,len(bookmarkFields) ):
        if results[0][i] != info[i]:
            q = "update bookmarks set %s=? where id=?"%(bookmarkFields[i])
            cursor = connection.execute(q, [info[i],id])
            connection.commit()
    return 2
