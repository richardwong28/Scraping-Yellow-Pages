# B2B Lead Generation Engine (Yellow Pages Scraper)

A high-performance, automated lead generation tool designed to extract business intelligence from directory listings. This project focuses on **Scalability**, **Pagination Handling**, and **Data Integrity**.

## Business Value
This tool enables businesses to automate their market research and lead prospecting by extracting thousands of business contacts (Name, Phone, Website) across various categories and locations in minutes.

## Advanced Features

* **Automated Pagination:** Seamlessly crawls through multiple search result pages using dynamic URL injection.
* **Lead Aggregation:** Collects and merges data from hundreds of listings into a single, clean dataset.
* **Smart Duplicate Removal:** Integrated with **Pandas** to identify and remove duplicate entries (common in "Featured Ads" sections).
* **Defensive Scraping:** Implements `playwright-stealth` and randomized delays to mimic human browsing behavior and minimize bot detection.
* **Robust Error Handling:** Uses a "Parent-to-Child" extraction logic to ensure data remains aligned even when certain fields (like websites) are missing.

## Technical Stack

* **Core:** Python 3.13
* **Automation:** Playwright (Chromium)
* **Bypass Tech:** Playwright-Stealth
* **Data Processing:** Pandas
* **Storage:** CSV / Excel (XLSX)

## Project Architecture

```text
Portfolio-2/
├── output/             # Generated lead databases (CSV)
├── src/
│   ├── scraper.py      # Pagination & Extraction logic
│   ├── data_handler.py # Data cleaning & deduplication
│   └── browser_manager.py # Browser & Fingerprint management
├── main.py             # Orchestrator
└── README.md