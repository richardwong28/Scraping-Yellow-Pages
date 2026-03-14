import asyncio
from urllib.parse import quote_plus
from playwright.async_api import async_playwright
from playwright_stealth import Stealth
from bs4 import BeautifulSoup

class YellowPagesScraper:
    def __init__(self, keyword, location):
        clean_keyword = quote_plus(keyword)
        clean_location = quote_plus(location)
        self.base_url = f"https://www.yellowpages.com/search?search_terms={clean_keyword}&geo_location_terms={clean_location}"
        self.data = []

    async def scrape(self, max_pages=10):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/119.0.0.0 Safari/537.36"
            )
            page = await context.new_page()
            await Stealth().apply_stealth_async(page)

            try:
                for current_page in range(1, max_pages + 1):
                    target_url = f"{self.base_url}&page={current_page}"
                    print(f"Scraping halaman {current_page}: {target_url}")

                    try:
                        await page.goto(target_url, wait_until="networkidle", timeout=30000)

                        listings = await page.query_selector_all('.v-card')
                        if not listings:
                            print(f"Tidak ada listing di halaman {current_page}, berhenti.")
                            break

                        for item in listings:
                            name_el = await item.query_selector('.business-name')
                            name = await name_el.inner_text() if name_el else "N/A"

                            phone_el = await item.query_selector('.phones')
                            phone = await phone_el.inner_text() if phone_el else "N/A"

                            web_el = await item.query_selector('.track-visit-website')
                            web = await web_el.get_attribute('href') if web_el else "N/A"

                            rating_el = await item.query_selector('.result-rating')
                            rating = "N/A"
                            if rating_el:
                                html = await rating_el.evaluate('el => el.outerHTML')
                                soup = BeautifulSoup(html, 'html.parser')
                                rating_div = soup.select_one('.result-rating')
                                if rating_div:
                                    classes = rating_div.get('class', [])
                                    rating_map = {
                                        'one': 1, 'one half': 1.5,
                                        'two': 2, 'two half': 2.5,
                                        'three': 3, 'three half': 3.5,
                                        'four': 4, 'four half': 4.5,
                                        'five': 5
                                    }
                                    for cls in classes:
                                        if cls in rating_map:
                                            rating = rating_map[cls]
                                            break

                            self.data.append({
                                'Name': name.strip(),
                                'Phone': phone.strip(),
                                'Web': web,
                                'Rating': rating
                            })

                        print(f"Halaman {current_page}: terkumpul {len(self.data)} data total.")

                        if current_page < max_pages:
                            await asyncio.sleep(2)

                    except Exception as e:
                        print(f"Error di halaman {current_page}: {e}")
                        continue

            finally:
                await browser.close()

        return self.data