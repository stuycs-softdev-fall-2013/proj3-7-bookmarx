import sqlite3


connection = sqlite3.connect('marx.db')
q1 = "CREATE TABLE users(username TEXT, token TEXT)"
q2 = "CREATE TABLE tags(id INTEGER, name TEXT, description TEXT, color TEXT, creator TEXT, privacy TEXT)"
q3 = "CREATE TABLE bookmarks(id INTEGER, link TEXT, title TEXT)"
q4 = "CREATE TABLE taggings(bookmark INTEGER, tag INTEGER)"
q5 = "CREATE TABLE friendships(user1 TEXT, user2 TEXT)"
q6 = "CREATE TABLE followings(user TEXT, tag TEXT)"

cursor = connection.execute(q1)
cursor = connection.execute(q2)
cursor = connection.execute(q3)
cursor = connection.execute(q4)
cursor = connection.execute(q5)
cursor = connection.execute(q6)


connection.commit()
