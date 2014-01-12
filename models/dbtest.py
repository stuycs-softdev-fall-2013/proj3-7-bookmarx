from database import *

print getBookmark(1)
print getTag(1)
print getUser("chris")
print setBookmark([1,"www.youtube.com","funny","youtube"])
print setTag([1, "funny", "Funny things", "FF0000", "chris", "1", "public"])
print setUser(["chris","token1","funny,blah","",""])


print setBookmark([2,"blah","aelkjlae","elaekj"])
print getBookmark(2)
