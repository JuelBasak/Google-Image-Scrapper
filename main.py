from flask import Flask, render_template
from bs4 import BeautifulSoup as bs
from selenium import webdriver

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    browser = webdriver.Chrome()
    url_link = 'https://www.google.com/search?tbm=isch&q=' + 'apple'

    browser.get(url_link)
    browser.implicitly_wait(30)
    search_html = browser.page_source
    google_html = bs(search_html, 'html.parser')
    google_html.findAll('img', {'class': 'rg_i Q4LuWd'})

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

