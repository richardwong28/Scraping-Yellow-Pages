# YellowPages Scraper

Async web scraper for extracting business leads from YellowPages.com. Built with Python, Playwright, and BeautifulSoup — outputs clean, deduplicated CSV files ready for outreach or analysis.

## What it does

- Searches any keyword + location on YellowPages.com (e.g. `"Dentist"` in `"New York"`)
- Extracts: business name, phone number, website URL, and star rating
- Handles multi-page pagination automatically
- Applies stealth techniques to reduce bot detection
- Cleans and deduplicates results before saving
- Saves output as UTF-8 CSV compatible with Excel and Google Sheets

## Tech stack

| Tool | Role |
|---|---|
| Python 3.10+ | Core language |
| Playwright (async) | Browser automation |
| playwright-stealth | Anti-bot fingerprint reduction |
| BeautifulSoup | HTML parsing for rating extraction |
| Pandas | Data cleaning and deduplication |

## Project structure

```
├── src/
│   ├── scraper.py          # Core scraping logic (async, paginated)
│   ├── browser_manager.py  # Browser context with rotating user agents
│   └── data_handler.py     # Deduplication and CSV export
├── main.py                 # Entry point
├── output/                 # CSV results saved here
├── logs/                   # Runtime logs
└── requirements.txt
```

## Setup

```bash
# Install dependencies
pip install playwright playwright-stealth beautifulsoup4 pandas openpyxl
playwright install chromium

# Run
python main.py
```

Edit `main.py` to change keyword and location:

```python
keyword = "Dentist"
location = "New York"
```

## Output format

```
Name,Phone,Web,Rating
Bright Smile Dental,+1 (212) 555-0142,https://brightsmile.com,4.5
Downtown Orthodontics,+1 (212) 555-0198,N/A,3
...
```

## Notes

- YellowPages uses anti-bot protection. If scraping fails, the site may be blocking the request — not a code bug. Increasing delay or using a residential proxy resolves this.
- CSS selectors may need updating if YellowPages changes their HTML structure. Verify selectors in browser DevTools before running at scale.
- Always respect the target site's `robots.txt` and terms of service.

## Key technical decisions

**Why async Playwright over Requests/Scrapy?**
YellowPages renders content client-side. Playwright handles JavaScript-rendered pages that Requests cannot access.

**Why BeautifulSoup for ratings?**
Ratings are encoded as CSS class names (e.g. `four-half`), not text — BS4 makes parsing the class list straightforward alongside Playwright's async context.

**Why `utf-8-sig` encoding?**
Windows Excel auto-detects BOM-signed UTF-8 correctly. Without it, special characters in business names render as garbage in Excel on Indonesian/Asian locales.

<img width="1919" height="868" alt="image" src="https://github.com/user-attachments/assets/7263f5e4-2475-42ea-83d6-8f6d5a908e58" />
