import bs4
import requests as r
import sqlite3

def GetSource(hall, link):
  hall_lvl = link.split("/")[4].split("_")[1]
  soup = bs4.BeautifulSoup(r.get(link).content, features="html.parser")
  base_img ="https://clash-of-clans-wiki.com" + soup.find("img", src=True)["src"]
  base_link = ""
  for elem in soup.find_all("a", href=True):
    if "clashofclans" in elem["href"]:
      base_link = elem["href"]
  if base_link != "" and base_img != "https://clash-of-clans-wiki.com/template/icons/update_white.svg":
    Fill(hall, hall_lvl, base_img, base_link)

def Fill(hall, lvl, img, link):
  connection = sqlite3.connect(f"source/{hall}_bases.db")
  cursor = connection.cursor()
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS Bases(
    lvl INTEGER,
    img TEXT NOT NULL,
    link TEXT NOT NULL)
  '''
  )
  cursor.execute('INSERT OR IGNORE INTO Bases(lvl, img, link) VALUES (?, ?, ?)', (lvl, img, link))
  connection.commit()
  connection.close()

