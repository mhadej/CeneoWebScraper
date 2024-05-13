from app import app
from flask import render_template, request, redirect, url_for
from bs4 import BeautifulSoup
import requests

@app.route('/')
def index():
    return render_template("index.html.jinja")

@app.route('/extract', methods=['POST', 'GET'])
def extract():
    if request.method == 'POST':
        product_id = request.form.get("product_id")

        url = rf'https://www.ceneo.pl/{product_id}'
        respone = requests.get(url)

        if respone.status_code == requests.codes['ok']:
            page_dom = BeautifulSoup(response.txt, "html.parser")
            try:
                opinions_count = page_dom.select_one("a.product_reviev__link > span").get_text().strip()
            except AttributeError:
                opinions_count = 0
            
            if opinions_count:
                #proces ekstrakcji  
                #przekierowanie
                return redirect(url_for('product', product_id = product_id))
            
            error = "Dany produkt nie ma opinii"
            return render_template("extract.html.jinja", error = error)

        error = "Błędny kod produktu!"
        return render_template("extract.html.jinja", error = error)

    return render_template("extract.html.jinja")

@app.route('/products')
def products():
    return render_template("products.html.jinja")

@app.route('/author')
def author():
    return render_template("author.html.jinja")

@app.route('/product/<product_id>')
def product(product_id):
    return render_template("product.html.jinja", product_id = product_id)