import bs4
import requests as r

from parser.fill_db import GetSource


def GetPages(hall, link):
  soup = bs4.BeautifulSoup(r.get(link).content, features="lxml")
  last_page = 0
  for elem in soup.find_all("a", href=True):
    if "page" in elem["href"] and int(elem["href"].split("/")[-2].split("_")[1]) >= last_page:
      last_page = int(elem["href"].split("/")[-2].split("_")[1])
  if hall == "th":
    GetThBases(hall ,1, link)
    for i in range(2, last_page + 1):
      GetThBases(hall, i, link + f"page_{i}/")
  elif hall == "bh":
    GetBhBases(hall, 1, link)
    for i in range(2, last_page + 1):
      GetBhBases(hall, i, link + f"page_{i}/")
  


def GetThBases(hall, p_num, link):
  tags = ["war", "farm", "defence", "troll", "funny"]
  soup = bs4.BeautifulSoup(r.get(link).content, features="html.parser")
  bases = []
  for elem in soup.find_all("a", href=True):
    if any([x in elem["href"] for x in tags]) and elem["href"][-5:] == ".html":
      bases.append(elem["href"].split("/")[3])
  for elem in bases:
    if "page" in link:
      GetSource(hall, link.replace(f"page_{p_num}","") + elem)
    else:
      GetSource(hall, link + elem)

def GetBhBases(hall, p_num, link):
  soup = bs4.BeautifulSoup(r.get(link).content, features="html.parser")
  bases = []
  for elem in soup.find_all("a", href=True):
    if ".html" in elem["href"]:
     bases.append(elem["href"].split('/')[3])
  for elem in bases:
    if "page" in link:
      GetSource(hall, link.replace(f"page_{p_num}","") + elem)
    else:
      GetSource(hall, link + elem)







