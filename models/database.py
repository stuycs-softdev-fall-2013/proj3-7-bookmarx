import sqlite3

userFields = ["username","token"]
tagFields = ["id", "name", "description", "color", "creator", "privacy"]
bookmarkFields = ["id", "link", "title"]

################################ GET FUNCTIONS #################################
#Get functions return 0 if the entry doesn't exist

def getUser(username):
    connection = sqlite3.connect('marx.db')
    q = "select * from users where username=?"
    cursor = connection.execute(q, [username])
    results = [line for line in cursor]
    q = "select * from tags where creator=?"
    cursor = connection.execute(q, [username])
    tags = [line for line in cursor]
    results.append(tags)
    q = "select user2 from friendships where user1=?"
    cursor = connection.execute(q, [username])
    friends = [line for line in cursor]
    results.append(friends)
    q = "select tags.* from tags,followings where followings.user=? and tags.id=followings.tag"
    cursor = connection.execute(q, [username])
    followed = [line for line in cursor]
    results.append(followed)
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
#Set functions return 0 if the number of fields provided in info is incorrect, 
#and 1 if there is no problem

def setUser(info):
    if len(info) != len(userFields):
        return 1
    connection = sqlite3.connect('marx.db')
    q = "select * from users where username=?"
    cursor = connection.execute(q, [info[0]])
    results = [line for line in cursor]
    if len(results) == 0:
        q = "insert into users values(?,?,?,?,?,?)"
        cursor = connection.execute(q,[info[0],info[1],info[2],info[3],info[4],info[5]])
        connection.commit()
        return 1
    for i in range(0,len(userFields) ):
        if results[0][i] != info[i]:
            q = "update users set %s=? where username=?"%(userFields[i])
            cursor = connection.execute(q, [info[i],info[0]])
            connection.commit()
    return 1


def setTag(info):
    if len(info) != len(tagFields):
        return 0
    connection = sqlite3.connect('marx.db')
    q = "select * from tags where id=?"
    cursor = connection.execute(q, [info[0]])
    results = [line for line in cursor]
    if len(results) == 0:
        q = "insert into tags values(?,?,?,?,?,?,?)"
        cursor = connection.execute(q,[info[0],info[1],info[2],info[3],info[4],info[5],info[6]])
        connection.commit()
        return 1
    for i in range(0,len(tagFields) ):
        if results[0][i] != info[i]:
            q = "update tags set %s=? where id=?"%(tagFields[i])
            cursor = connection.execute(q, [info[i],info[0]])
            connection.commit()
    return 1


def setBookmark(info):
    if len(info) != len(bookmarkFields):
        return 0
    connection = sqlite3.connect('marx.db')
    q = "select * from bookmarks where id=?"
    cursor = connection.execute(q, [info[0]])
    results = [line for line in cursor]
    if len(results) == 0:
        q = "insert into bookmarks values(?,?,?,?)"
        cursor = connection.execute(q,[info[0],info[1],info[2],info[3]])
        connection.commit()
        return 1
    for i in range(0,len(bookmarkFields) ):
        if results[0][i] != info[i]:
            q = "update bookmarks set %s=? where id=?"%(bookmarkFields[i])
            cursor = connection.execute(q, [info[i],info[0]])
            connection.commit()
    return 1
