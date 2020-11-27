from requests_html import HTMLSession
from bs4 import BeautifulSoup
import asyncio
from pyppeteer import launch

async def getHTMLwithJavascriptContentHeadless(url):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.waitForSelector('div.slick-list')
    cont = await page.content()
    await browser.close()
    return cont


def getHTMLwithJavascriptContent(url):
    session = HTMLSession()
    resp = session.get(url)
    resp.html.render(timeout=20)
    return resp.html.html


if __name__ == "__main__":
    url = 'https://tv.verizon.com/watch/'
    DOM = asyncio.get_event_loop().run_until_complete(getHTMLwithJavascriptContentHeadless(url))
    soup = BeautifulSoup(DOM, 'html.parser')
    for link in soup.find_all('a'):
        if str(link.get('href')).startswith('/'):
            print(link.get('href'))
