import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_seo_data(url):
    # URL-ga HTTP so'rov yuborish
    response = requests.get(url)

    if response.status_code != 200:
        print("Saytni yuklashda xatolik yuz berdi.")
        return

    # Sahifani BeautifulSoup bilan tahlil qilish
    soup = BeautifulSoup(response.text, 'html.parser')

    # Meta tavsifini olish
    meta_description = soup.find('meta', attrs={'name': 'description'})
    description = meta_description['content'] if meta_description else 'Yo‘q'

    # Meta kalit so‘zlarini olish
    meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
    keywords = meta_keywords['content'] if meta_keywords else 'Yo‘q'

    # Sahifa sarlavhasini olish
    title = soup.find('title').text if soup.find('title') else 'Yo‘q'

    # Sahifadagi barcha linklarni olish
    links = soup.find_all('a', href=True)
    external_links = [link['href'] for link in links if 'http' in link['href']]
    internal_links = [link['href'] for link in links if 'http' not in link['href']]

    # Natijalarni ekranga chiqarish
    print(f"Sayt sarlavhasi: {title}")
    print(f"Meta tavsifi: {description}")
    print(f"Meta kalit so'zlari: {keywords}")
    print(f"Ichki havolalar: {len(internal_links)}")
    print(f"Tashqi havolalar: {len(external_links)}")

    return {
        "title": title,
        "description": description,
        "keywords": keywords,
        "internal_links": len(internal_links),
        "external_links": len(external_links)
    }


# URL kiritish
url = input("Sayt URL ni kiriting: ")
seo_data = get_seo_data(url)

# Natijalarni CSV faylga saqlash
if seo_data:
    df = pd.DataFrame([seo_data])
    df.to_csv('seo_data.csv', index=False)
    print("SEO ma'lumotlar CSV faylga saqlandi.")
