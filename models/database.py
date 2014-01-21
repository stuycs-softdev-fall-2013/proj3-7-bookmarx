import sqlite3

userFields = ["username","user_id"]
tagFields = ["id", "name", "description", "color", "creator", "privacy"]
bookmarkFields = ["id", "link", "title"]

################################ GET FUNCTIONS #################################
#Get functions return None if the entry doesn't exist

def getUser(user_id):
    # get relevant user
    connection = sqlite3.connect('marx.db')
    q = "select * from users where user_id=?"
    cursor = connection.execute(q, [user_id])
    matching_users = [line for line in cursor]

    if not matching_users:
        return None

    # returning user
    results = { 'username': matching_users[0][0] }

    # get tags created
    connection.execute("select id from tags where creator=?", [user_id])
    results['tags'] = [Tag(tagID) for tagID in cursor]

    # get friends
    q = "select user2 from friendships where user1=?"
    connection.execute(q, [user_id])
    results['friends'] = [line for line in cursor]

    # get followed tags
    q = "select tags.id from tags,followings where followings.user=? and " + \
        "tags.id=followings.tag"
    cursor = connection.execute(q, [user_id])
    results['followed'] = [Tag(tagID) for tagID in cursor]

    return results


def getTag(idnum):
    connection = sqlite3.connect('marx.db')
    q = "select * from tags where id=?"
    cursor = connection.execute(q, [str(idnum)])
    results = [line for line in cursor]
    if len(results) == 1:
        results = [line for line in results[0]]
        results[3] = results[3].split(',')
        q = "select bookmarks.* from bookmarks,taggings where taggings.tag=? and " + \
            "taggings.bookmark=bookmarks.id"
        cursor = connection.execute(q, [str(idnum)])
        bookmarks = [Bookmark(b[1],b[2]) for b in cursor]
        results.append(bookmarks)
        return results
    else:
        return None


def getBookmark(idnum):
    connection = sqlite3.connect('marx.db')
    q = "select * from bookmarks where id=?"
    cursor = connection.execute(q, [str(idnum)])
    results = [line for line in cursor]
    if len(results) == 1:
        results = [line for line in results[0]]
        q = "select tags.name,tags.id,tags.color from tags,taggings where taggings.bookmark=? and " + \
            "taggings.tag=tags.id"
        cursor = connection.execute(q, [str(idnum)])
        tags = [line for line in cursor]

        #put colors into proper format
        for tag in tags:
            tag[2] = tag[2].split(" ")

        results.append(tags)
        return results
    else:
        return None


############################### SET FUNCTIONS #################################

def setUser(user):
    info = [user.username, user.user_id, user.tags, user.followed_tags, user.friends]

    # get relevant user
    connection = sqlite3.connect('marx.db')
    q = "select * from users where user_id=?"
    cursor = connection.execute(q, [user.user_id])
    matching_users = [line for line in cursor]

    # if there is no such user in the db, create one and return
    if not matching_users:
        connection.execute("insert into users values(?,?)",
                           [user.username, user.user_id])
        connection.commit()
        return

    # update the existing user
    for i in range(len(userFields)):
        if matching_users[0][i] != info[i]:
            q = "update users set %s=? where user_id=?"%(userFields[i])
            connection.execute(q, [info[i], user.user_id])

#Tags shouldn't need to be updated from user context
    ##update relevant tags
    #connection.execute("delete from tags where tags.creator=?", [username])
    #for i in range(len(user.tags)):
    #    connection.execute("insert into tags values(?,?,?,?,?,?)", [tags[i][:6]#])

    # update relevant followings
    connection.execute("delete from followings where followings.user=?", [username])
    for i in range(len(user.followed_tags)):
        q = "insert into followings values(?,?)"
        connection.execute(q, [username, followed_tags[i][0]])
    
    # update relevant friendships
    connection.execute("delete from friendships where friendships.user1=?",
                       [user.user_id])
    connection.execute("delete from friendships where friendships.user2=?",
                       [user.user_id])
    for i in range(len(user.friends)):
        q = "insert into friendships values(?,?)"
        connection.execute(q, [username, friends[i][0]])
        connection.execute(q, [friends[i][0], username])
    connection.commit()


def setTag(tag):
    info = [tag.idnum, tag.name, tag.description,
            " ".join([str(c) for c in tag.color]),
            tag.creator, tag.privacy, tag.bookmarks]
    connection = sqlite3.connect('marx.db')

    cursor = connection.execute("select * from tags where id=?", [info[0]])
    results = [line for line in cursor]
    if not results:
        info[0] = len([l for l in connection.execute("select * from tags")])
        cursor = connection.execute("insert into tags values(?,?,?,?,?,?)", info[:-1])
        connection.commit()
        return

    for i in range(len(tagFields)):
        if results[0][i] != info[i]:
            q = "update tags set %s=? where id=?"%(tagFields[i])
            cursor = connection.execute(q, [info[i],idnum])
    q = "delete from taggings where tag=?"

    for i in range(len(tag.bookmarks)):
        q = "insert into taggings values(?,?)"
        try:
            connection.execute(q, [tag.idnum,tag.bookmarks[i].idnum])
        except:
            connection.execute(q, [tag.idnum,tag.bookmarks[i][0]])
            print "FUCK"
    connection.commit()


def setBookmark(bookmark):
    idnum = bookmark.idnum
    info = [bookmark.link, bookmark.title, bookmark.tags]
    connection = sqlite3.connect('marx.db')

    cursor = connection.execute("select * from bookmarks where id=?", [bookmark.idnum])
    results = [line for line in cursor]
    if not results:
        idnum = len([l for l in connection.execute("select * from tags")])
        q = "insert into bookmarks values(?,?,?)"
        connection.execute(q, [bookmark.idnum] + info[:2])
        connection.commit()
        return

    for i in range(len(bookmarkFields[:-1])):
        if results[0][i] != info[i]:
            q = "update bookmarks set %s=? where id=?"%(bookmarkFields[i])
            cursor = connection.execute(q, [info[i], bookmark.idnum])

    cursor = connection.execute("delete from taggings where bookmark=?", [idnum])
    for i in range(len(bookmark.tags)):
        q = "insert into taggings values(?,?)"
        try:
            cursor = connection.execute(q, [idnum, bookmark.tags[i].idnum])
        except:
            cursor = connection.execute(q, [idnum, bookmark.tags[i][0]])
            print "FUCK"
    connection.commit()

############################ REMOVE FUNCTIONS ##################################
def removeUser(username,tags):
    connection = sqlite3.connect('marx.db')
    cursor = connection.execute("delete from users where username=?",[username])
    cursor = connection.execute("delete from friendships where user1=?",[username])
    cursor = connection.execute("delete from friendships where user2=?",[username])
    cursor = connection.execute("delete from followings where user=?",[username])
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
