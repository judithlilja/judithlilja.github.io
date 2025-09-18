import requests
from bs4 import BeautifulSoup
import csv

# URL till Gina Tricots bästsäljare
url = "https://www.ginatricot.com/eu/bestsellers"

# hämta sidan
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# hitta produkter
products = soup.find_all("a", class_="product-link")

# öppna en csv-fil att skriva till
with open("ginatricot_bestsellers.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Produktnamn", "Länk"])  # rubriker

    for p in products:
        name = p.get("aria-label", "Ingen titel")
        link = "https://www.ginatricot.com" + p.get("href", "")
        writer.writerow([name, link])

print("✅ Klart! Kolla filen: ginatricot_bestsellers.csv")


