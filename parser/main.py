import bs4
import requests as r

from parser.popa import GetPages

def TownHall():
  link = "https://clash-of-clans-wiki.com/plans/"
  soup = bs4.BeautifulSoup(r.get(link).content, features="lxml")
  links = []
  for element in soup.find_all("a", href=True):
    if "th" in element["href"]:
      links.append(element["href"])
  links = list(set(links))
  for elem in links:
    GetPages("th", link + elem.split('/')[2] + '/')

def BuilderHall():
  link = "https://clash-of-clans-wiki.com/builder_hall_bases/"
  soup = bs4.BeautifulSoup(r.get(link).content, features="lxml")
  links = []
  for element in soup.find_all("a", href=True):
    if "bh" in element["href"]:
      links.append(element["href"])
  links = list(set(links))
  for elem in links:
    GetPages("bh", link + elem.split('/')[2] + '/')

TownHall()
BuilderHall()

