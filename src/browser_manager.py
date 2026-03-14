import random
from playwright_stealth import Stealth

class BrowserManager:
    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        ]

    async def get_context(self, playwright):
        random_ua = random.choice(self.user_agents)

        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=random_ua)
        page = await context.new_page()
        await Stealth().apply_stealth_async(page)

        # FIX 5: kembalikan browser agar caller bisa menutupnya
        return browser, context, page