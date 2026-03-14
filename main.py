import asyncio
from src.scraper import YellowPagesScraper
from src.data_handler import clean_and_save

async def main():
    keyword = "Dentist"
    location = "New York"

    print(f"Mulai scraping: '{keyword}' di '{location}'")
    scraper = YellowPagesScraper(keyword, location)

    try:
        leads = await scraper.scrape(max_pages=5)

        if leads:
            filename = f"{keyword}_{location}".replace(" ", "_")
            path = clean_and_save(leads, filename)
            print(f"Selesai! Hasil disimpan di: {path}")
        else:
            print("Tidak ada data yang ditemukan.")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    asyncio.run(main())