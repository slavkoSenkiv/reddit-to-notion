import bs4
import requests
url1 = 'https://www.reddit.com/r/passive_income/comments/qhl73c/advice_for_a_fulltime_mom_who_doesnt_want_a_basic/'
url2 = 'https://www.reddit.com/r/passive_income/comments/lm1vnc/warren_buffett_says_if_you_dont_find_a_way_to/gnspihn/?context=3'
selector1 = 'h1[class="_eYtD2XCVieq6emjKBH3m"]'
title_selector = 'h1'
paragraph_selector = 'p'
page = requests.get(url2)
page.raise_for_status()
soup = bs4.BeautifulSoup(page.text, 'html.parser')
title_text = soup.select(title_selector)[0].getText()
print(title_text)
topic_text = soup.select(paragraph_selector)
for text in topic_text:
    print(text.getText())


