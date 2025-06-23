from pprint import pprint

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

def wait_element(driver_or_tag, delay_seconds=1, by=By.TAG_NAME, value=None):
    return WebDriverWait(driver_or_tag, delay_seconds).until(presence_of_element_located((by, value)))



path = ChromeDriverManager().install()

service = Service(executable_path=path)
driver = Chrome(service=service)
driver.get('https://habr.com/ru/articles/')

## Определяем список ключевых слов:
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'битва', 'тупость', 'купить', 'доступ', 'если']

articles = []

print("СТАТЬИ, в заголовках которых есть слова:", KEYWORDS)

article_list_tag = wait_element(driver, 1, By.CLASS_NAME, 'tm-articles-list')
article_tags = article_list_tag.find_elements(By.TAG_NAME, value='article')

for article_tag in article_tags:
    time_tag = wait_element(article_tag, 1, By.TAG_NAME, value='time')
    h2_tag = wait_element(article_tag, 1, By.TAG_NAME, value='h2')
    a_tag = wait_element(h2_tag, 1, By.TAG_NAME, value='a')
    span_tag = a_tag.find_element(By.TAG_NAME, value='span')

    publication_time = time_tag.get_attribute('datetime')
    absolute_article_link = a_tag.get_attribute('href')
    article_title = span_tag.text.strip()

    article_dict = {
            'publication_time': publication_time,
            'article_title': article_title,
            'absolute_article_link': absolute_article_link,
            'article_text': ''
        }

    for word in KEYWORDS:
        if word in article_title.split():
            print(article_dict)

    articles.append(article_dict)


print("Боковая панель: 'ЧИТАЮТ СЕЙЧАС'. Статьи, в заголовках которых есть слова:", KEYWORDS)

sidebar_article_list_tag = wait_element(driver, 1, By.CLASS_NAME, 'tm-article-list-block__list')
sidebar_article_tags = sidebar_article_list_tag.find_elements(By.CLASS_NAME, value='tm-article-list-block__item')

for sidebar_article_tag in sidebar_article_tags:

    # time_tag = wait_element(article_tag, 1, By.TAG_NAME, value='time')
    try:
        h2_tag = wait_element(sidebar_article_tag, 1, By.TAG_NAME, value='h2')
        a_tag = wait_element(h2_tag, 1, By.TAG_NAME, value='a')
        span_tag = a_tag.find_element(By.TAG_NAME, value='span')

        # publication_time = time_tag.get_attribute('datetime')
        absolute_article_link = a_tag.get_attribute('href')
        article_title = span_tag.text.strip()

        article_dict = {
            'publication_time': '',
            'article_title': article_title,
            'absolute_article_link': absolute_article_link,
            'article_text': ''
        }

        for word in KEYWORDS:
            if word in article_title.split():
                print(article_dict)

        articles.append(article_dict)
    except Exception:
        print("Не дождался")



print("СТАТЬИ, в тексте которых есть слова:", KEYWORDS)
for article_dict in articles:
    driver.get(article_dict['absolute_article_link'])
    article_tag = wait_element(driver, 1, By.ID, 'post-content-body')
    article_text = article_tag.text.strip()

    article_dict['article_text'] = article_text

    for word in KEYWORDS:
        if word in article_text.split():
            print(article_dict)
            print(f"Количество вхождений слова '{word}':", article_text.count(word))



# pprint(articles)


# import requests
# import bs4
# import fake_headers
# from pprint import pprint
#
# headers_generator = fake_headers.Headers(os='win', browser='chrome')
# main_page_response = requests.get('https://habr.com/ru/articles/', headers=headers_generator.generate())
# main_soup = bs4.BeautifulSoup(main_page_response.text, features='lxml')

# # Поиск в блоке "Все потоки" раздел "Статьи"
# print("СТАТЬИ:")
# articles_div_tag = main_soup.find('div', class_='tm-articles-list')
# articles_tags = articles_div_tag.find_all('article')
#
# articles = []
#
# for article_tag in articles_tags:
#     time_tag = article_tag.find('time')
#     h2_tag = article_tag.find('h2')
#     a_tag = h2_tag.find('a')
#     span_tag = a_tag.find('span')
#
#     publication_time = time_tag['datetime']
#
#     relative_article_link = a_tag['href']
#     absolute_article_link = f'https://habr.com{relative_article_link}'
#     article_title = span_tag.text.strip()
#
#     article_http_response = requests.get(absolute_article_link, headers=headers_generator.generate())
#     article_html = article_http_response.text
#     article_soup = bs4.BeautifulSoup(article_html, features='lxml')
#
#     articles_div_tag = article_soup.find('div', id='post-content-body')
#     article_text = articles_div_tag.text.strip()
#
#     article_dict = {
#         'publication_time': publication_time,
#         'article_title': article_title,
#         'absolute_article_link': absolute_article_link,
#         'article_text': article_text
#     }
#     print(article_dict)
#     articles.append(article_dict)
# # print(articles)
