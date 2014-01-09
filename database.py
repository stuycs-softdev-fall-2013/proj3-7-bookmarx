import sqlite3

userFields = ["username","token", "tags", "friends", "followed"]
tagFields = ["id", "name", "description", "color", "creator", "bookmrks", "privacy"]
bookmarks = ["id", "link", "tags", "title"]

#The type is either "users", "tags", or "bookmarks"
#The id is the username or id you want
def getInfo(type,id):
    connection = sqlite3.connect('marx.db')
    if type == "users":
        q = "select * from users where username=?"
        cursor = connection.execute(q, [id])
    else:
        q = "select * from ? where id=?"
        cursor = connection.execute(q, [type,id])
    results = [line for line in cursor]
    return results


#The type is either "users", "tags", or "bookmarks"
#The id is the username or id you want
#The info is a list of the info you want to store
def setInfo(type,id,info):
    connection = sqlite3.connect('marx.db')
    if type == "users":
        fields = userfields
        numFields = 5
        idName = "username"
    elif type == "tags":
        q = "select * from tags where id=?"
        fields = tagfields
        numFields = 7
        idName = "id"
    elif type == "bookmarks":
        q = "select * from bookmarks where id=?"
        fields = bookmarkfields
        numFields = 4
        idName = "id"
    q = "select * from ? where ?=?"
    cursor = connection.execute(q, [type,idName,id])
    results = [line for line in cursor]
    for i in range(0,numFields):
            if results[i] != info[i]:
                q = "update users set ?=? where ?=?"
                cursor = connection.execute(q, [fields[i],info[i],idName,id])
    connection.commit()
