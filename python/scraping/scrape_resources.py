import requests
from bs4 import BeautifulSoup
#from requests_html import HTMLSession  # si on doit traiter le contenu généré dynamiquement
import csv
import re

# URL
URL = "https://astroneer.fandom.com/fr/wiki/Ressources"

print("✅ Lancement du script")

# Récupération du HTML
response = requests.get(URL)
response.raise_for_status()  # stoppe si erreur HTTP
html = response.text
    
# Parsing avec BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Récupération des données
h3 = soup.find("span", {"id": "Ressources_Naturelles"})
dl = h3.find_parent("h3").find_next("dl")
data = dl.find_all("dd")

# si on doit traiter le contenu généré dynamiquement
# session = HTMLSession()
# r = session.get("https://astroneer.fandom.com/fr/wiki/Ressources")
# r.html.render()  # exécution du JS
# data = r.html.find("h3 ~ dl dd a[title]")

header = ["resource", "image"]
rows = []
        
for row in data:
    text = row.get_text(strip=True)
    img_tag = row.find("img")
    img = img_tag.get("data-src") if img_tag else ""
    if text:
        rows.append([text, img])

# Export en CSV
with open("resources.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(header)
    writer.writerows(rows)

print("✅ Scraping terminé, fichier resources.csv généré")

