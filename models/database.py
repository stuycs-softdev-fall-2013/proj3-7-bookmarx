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
    if len(results) == 1:
        results = [line for line in results[0]]
        q = "select * from tags where creator=?"
        cursor = connection.execute(q, [username])
        tags = [line for line in cursor]
        results.append(tags)
        q = "select user2 from friendships where user1=?"
        cursor = connection.execute(q, [username])
        friends = [line for line in cursor]
        q = "select user1 from friendships where user2=?"
        cursor = connection.execute(q, [username])
        friends2 = [line for line in cursor]
        friends.extend(friends2)
        results.append(friends)
        q = "select tags.* from tags,followings where followings.user=? and tags.id=followings.tag"
        cursor = connection.execute(q, [username])
        followed = [line for line in cursor]
        results.append(followed)
        return results
    else:
        return 0


def getTag(id):
    connection = sqlite3.connect('marx.db')
    q = "select * from tags where id=?"
    cursor = connection.execute(q, [id])
    results = [line for line in cursor]
    if len(results) == 1:
        results = [line for line in results[0]]
        results[3] = results[3].split(',')
        q = "select bookmarks.* from bookmarks,taggings where taggings.tag=? and taggings.bookmark=bookmarks.id"
        cursor = connection.execute(q, [id])
        bookmarks = [line for line in cursor]
        results.append(bookmarks)
        return results
    else:
        return 0


def getBookmark(id):
    connection = sqlite3.connect('marx.db')
    q = "select * from bookmarks where id=?"
    cursor = connection.execute(q, [id])
    results = [line for line in cursor]
    if len(results) == 1:
        results = [line for line in results[0]]
        q = "select tags.* from tags,taggings where taggings.bookmark=? and taggings.tag=tags.id"
        cursor = connection.execute(q, [id])
        tags = [line for line in cursor]
        results.append(tags)
        return results
    else:
        return 0


############################### SET FUNCTIONS #################################

def setUser(username, token, tags, followed, friends):
    info = [username,token,tags,followed,friends]
    connection = sqlite3.connect('marx.db')
    q = "select * from users where username=?"
    cursor = connection.execute(q, [info[0]])
    results = [line for line in cursor]
    if len(results) == 0:
        q = "insert into users values(?,?)"
        cursor = connection.execute(q,[info[0],info[1]])
        connection.commit()
        return 1
    for i in range(0,len(userFields) ):
        if results[0][i] != info[i]:
            q = "update users set %s=? where username=?"%(userFields[i])
            cursor = connection.execute(q, [info[i],info[0]])
    q = "delete from tags where tags.creator=?"
    cursor = connection.execute(q, [username])
    for i in range (0,len(tags)):
        q = "insert into tags values(?,?,?,?,?,?)"
        cursor = connection.execute(q, [tags[i][0],tags[i][1],tags[i][2],tags[i][3],tags[i][4],tags[i][5]])
    q = "delete from followings where followings.user=?"
    cursor = connection.execute(q, [username])
    for i in range (0,len(followed)):
        q = "insert into followings values(?,?)"
        cursor = connection.execute(q, [username, followed[i][0]])
    q = "delete from friendships where friendships.user1=?"
    cursor = connection.execute(q, [username])
    q = "delete from friendships where friendships.user2=?"
    cursor = connection.execute(q, [username])
    for i in range (0,len(friends)):
        q = "insert into friendships values(?,?)"
        cursor = connection.execute(q, [username, friends[i][0]])
        cursor = connection.execute(q, [friends[i][0], username])
    connection.commit()
    return 1


def setTag(id,name,description,color,creator,privacy,bookmarks):
    info = [id,name,description,color,creator,privacy,bookmarks]
    connection = sqlite3.connect('marx.db')
    q = "select * from tags where id=?"
    cursor = connection.execute(q, [info[0]])
    results = [line for line in cursor]
    if len(results) == 0:
        q = "insert into tags values(?,?,?,?,?,?)"
        cursor = connection.execute(q,[info[0],info[1],info[2],info[3],info[4],info[5]])
        connection.commit()
        return 1
    for i in range(0,len(tagFields) ):
        if results[0][i] != info[i]:
            q = "update tags set %s=? where id=?"%(tagFields[i])
            cursor = connection.execute(q, [info[i],info[0]])
    q = "delete from taggings where tag=?"
    for i in range(0,len(bookmarks)):
        q = "insert into taggings values(?,?)"
        cursor = connection.execute(q, [id,bookmarks[i][0]])
    connection.commit()
    return 1


def setBookmark(id, link, title, tags):
    info = [id,link,title,tags]
    connection = sqlite3.connect('marx.db')
    q = "select * from bookmarks where id=?"
    cursor = connection.execute(q, [info[0]])
    results = [line for line in cursor]
    if len(results) == 0:
        q = "insert into bookmarks values(?,?,?)"
        cursor = connection.execute(q,[info[0],info[1],info[2]])
        connection.commit()
        return 1
    for i in range(0,len(bookmarkFields) ):
        if results[0][i] != info[i]:
            q = "update bookmarks set %s=? where id=?"%(bookmarkFields[i])
            cursor = connection.execute(q, [info[i],info[0]])
    q = "delete from taggings where bookmark=?"
    cursor = connection.execute(q, [id])
    for i in range (0,len(tags)):
        q = "insert into taggings values(?,?)"
        cursor = connection.execute(q, [id,tags[i][0]])
    connection.commit()
    return 1

############################ REMOVE FUNCTIONS ##################################
def removeUser(username,tags):
    connection = sqlite3.connect('marx.db')
    q = "delete from users where username=?"
    cursor = connection.execute(q,[username])
    q = "delete from friendships where user1=?"
    cursor = connection.execute(q,[username])
    q = "delete from friendships where user2=?"
    cursor = connection.execute(q,[username])
    q = "delete from followings where user=?"
    cursor = connection.execute(q,[username])
    connection.commit()
    for tag in tags:
        removeTag(tag[0])
#Note: This will only remove bookmarks that are tagged. We need to make sure there is some kind of "No Tag"-tag that other bookmarks will be tagged to


def removeTag(id):
    connection = sqlite3.connect('marx.db')
    q = "delete from tags where id=?"
    cursor = connection.execute(q,[id])
    q = "select bookmark from taggings where tag=?"
    cursor = connection.execute(q,[id])
    bookmarks = [x[0] for x in cursor]
    for bookmark in bookmarks:
        q = "delete from bookmarks where id=?"
        cursor = connection.execute(q,[id])
    q = "delete from taggings where tag=?"
    cursor = connection.execute(q,[id])
    q = "delete from followings where tag=?"
    cursor = connection.execute(q,[id])
    q = "select bookmark from taggings where tag=?"
    cursor = connection.execute(q,[id])
    connection.commit()


def removeBookmark(id):
    connection = sqlite3.connect('marx.db')
    q = "delete from bookmarks where id=?"
    cursor = connection.execute(q,[id])
    connection.commit()
