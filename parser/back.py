import sqlite3
from parser.popa import GetThBases, GetBhBases

def UpdateTH(lvl):
  link = f"https://clash-of-clans-wiki.com/plans/th_{lvl}/"
  GetThBases("th", 1, link)

def UpdateBH(lvl):
  link = f"https://clash-of-clans-wiki.com/builder_hall_bases/bh_{lvl}/"
  GetBhBases("bh", 1, link)

def GetRandomTHBase(lvl):
  UpdateTH(lvl)
  connection = sqlite3.connect('source/th_bases.db')
  cursor = connection.cursor()
  cursor.execute('SELECT * FROM Bases WHERE lvl = ? ORDER BY random() LIMIT 1', (lvl, ))
  data = cursor.fetchall()
  return data[0]


def GetRandomBHBase(lvl):
  UpdateBH(lvl)
  connection = sqlite3.connect('source/bh_bases.db')
  cursor = connection.cursor()
  cursor.execute('SELECT * FROM Bases WHERE lvl = ? ORDER BY random() LIMIT 1', (lvl, ))
  data = cursor.fetchall()
  return data[0]
