import sqlite3



class DB:
    def __init__(self):

        self.con = sqlite3.connect("memory.db")
    
    def get(self):
        cur = self.con.cursor()

ob = DB()
ob.get()


def ge():
    import random
    import string
    import math
    letters = string.ascii_lowercase
    val = []
    print(letters)
    # return [random.choice(letters) for i in range(10)]
    for i in range(6):
        val.append(math.floor(random.random()*10))
        print(val)
    random.shuffle(val)
    print(val)

