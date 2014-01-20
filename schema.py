import sqlite3


connection = sqlite3.connect('marx.db')
queries = [
 "DROP TABLE IF EXISTS users",
 "DROP TABLE IF EXISTS tags",
 "DROP TABLE IF EXISTS bookmarks",
 "DROP TABLE IF EXISTS taggings",
 "DROP TABLE IF EXISTS friendships",
 "DROP TABLE IF EXISTS followings",
 "CREATE TABLE users(username TEXT, user_id TEXT)",
 "CREATE TABLE tags(id INTEGER, name TEXT, description TEXT, color TEXT, creator TEXT, privacy TEXT)",
 "CREATE TABLE bookmarks(id INTEGER, link TEXT, title TEXT, creator TEXT, num_tags INTEGER)",
 "CREATE TABLE taggings(bookmark INTEGER, tag INTEGER)",
 "CREATE TABLE friendships(user1 TEXT, user2 TEXT)",
 "CREATE TABLE followings(user TEXT, tag TEXT)"
]

for q in queries:
    connection.execute(q)

connection.commit()
