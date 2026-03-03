# tp5/scrapper_music.py
import requests
from bs4 import BeautifulSoup
import re
import psycopg2
from datetime import datetime
import time
import logging

# ===================== CONFIG =====================
logging.basicConfig(
    filename='scraped_music.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    encoding='utf-8'
)

conn = psycopg2.connect(
    host="localhost",
    database="pymusic_tp5",  
    user="postgres",
    password="gui123reis13",
    port="5433"
)
cur = conn.cursor()

HEADERS = {'User-Agent': 'PyMusic-Scraper/1.0 (TP5-Educacional)'}

def clean(text):
    return re.sub(r'\s+', ' ', text).strip() if text else ""

def extract_infobox_data(soup):
    infobox = soup.find("table", class_="infobox")
    data = {}
    if not infobox:
        return data
    for tr in infobox.find_all("tr"):
        th = tr.find("th")
        td = tr.find("td")
        if not th or not td:
            continue
        key = clean(th.get_text())
        value = clean(td.get_text())
        if "Artista" in key or "Intérprete" in key:
            data["artist"] = value.split(",")[0].split(" e ")[0].split(" & ")[0]
        elif "Lançamento" in key or "Gravação" in key:
            year = re.search(r'\d{4}', value)
            data["year"] = int(year.group()) if year else None
        elif "Gênero" in key:
            data["genre"] = value.split(",")[0].split("•")[0]
    return data

def scrape_album(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=12)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find("h1", class_="firstHeading").get_text(strip=True)
        intro = soup.find("div", class_="mw-parser-output")
        desc = ""
        for p in intro.find_all("p", recursive=False):
            if p.get_text(strip=True):
                desc = clean(p.get_text())
                break

        info = extract_infobox_data(soup)
        artist = info.get("artist", "Desconhecido")
        year = info.get("year")
        genre = info.get("genre", "Diversos")

        # === INSERE OU IGNORA ÁLBUM ===
        cur.execute("""
            INSERT INTO tp5.albums (title, artist, release_year, genre, description, wikipedia_url)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (wikipedia_url) DO NOTHING
            RETURNING id
        """, (title, artist, year, genre, desc[:1000], url))

        album_inserted = cur.fetchone() is not None
        success = True

        # === REGISTRA PÁGINA RASPADA ===
        cur.execute("""
            INSERT INTO tp5.scraped_pages (url, page_title, status_code, success)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (url) DO UPDATE SET
                scraped_at = NOW(),
                page_title = EXCLUDED.page_title,
                status_code = EXCLUDED.status_code,
                success = EXCLUDED.success
        """, (url, title, response.status_code, True))

        if album_inserted:
            print(f"Álbum adicionado: {title} – {artist} ({year})")
            logging.info(f"SUCESSO | {title} | {artist} | {url}")
        else:
            print(f"Já existe: {title}")
            logging.info(f"DUPLICADO | {title} | {url}")

    except Exception as e:
        success = False
        error_msg = str(e)[:500]
        print(f"Falha em {url} → {type(e).__name__}")
        logging.error(f"FALHA | {url} | {error_msg}")

        # Registra falha
        cur.execute("""
            INSERT INTO tp5.scraped_pages (url, status_code, success, error_message)
            VALUES (%s, %s, false, %s)
            ON CONFLICT (url) DO UPDATE SET
                scraped_at = NOW(), error_message = EXCLUDED.error_message, success = false
        """, (url, getattr(response, 'status_code', None) if 'response' in locals() else None, error_msg))

        cur.execute("""
            INSERT INTO tp5.scraping_errors (page_id, error_type, error_detail)
            VALUES ((SELECT id FROM tp5.scraped_pages WHERE url = %s), %s, %s)
        """, (url, type(e).__name__, error_msg))

    finally:
        conn.commit()
        time.sleep(1.5)  # respeita a Wikipédia

# ===================== EXECUÇÃO =====================
if __name__ == "__main__":
    print("Iniciando PyMusic Scraper – TP5 (Música)\n")
    with open(r"C:\Users\gabib\OneDrive\Documentos\TPS DE PB\TP5\urls_albums.txt", "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip() and line.startswith("http")]

    for url in urls:
        print(f"Raspando → {url}")
        scrape_album(url)

    print("\nScraping concluído! Veja tp5/scraped_music.log")