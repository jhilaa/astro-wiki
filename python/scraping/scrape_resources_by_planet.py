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
table = h3.find_parent("h3").find_next("table")
table_header = table.find_all("th")
table_rows = table.find_all("tr")

header = []    
for th in table_header:
    text = th.get_text(strip=True)
    if text:
        header.append(text)
        
rows = []
for tr in table_rows:
    data = []
    table_data = tr.find_all("td")
    for td in table_data:
        text = td.get_text(strip=True)
        if text:
            data.append(text)
    if (len(data) > 0):
        rows.append(data)
     

#Export en CSV
with open("resources_by_planet.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(header)
    writer.writerows(rows)

print("✅ Scraping terminé, fichier resources.csv généré")

