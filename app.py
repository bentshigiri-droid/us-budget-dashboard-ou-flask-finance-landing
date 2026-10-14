from flask import Flask, render_template

app = Flask(__name__)

# Lien direct vers ton produit MyMaketou
MAKETOUP_URL = "https://naa-bee-shop.mymaketou.shop/products/the-ultimate-us-personal-finance-budget-dashboard-monthly-budget-planner-debt-payoff-savings-tracker-for-google-sheets-instant-download"

@app.route('/')
def home():
    return render_template('index.html', maketou_url=MAKETOUP_URL)

@app.route('/sitemap.xml')
def sitemap():
    return app.send_static_file('sitemap.xml') if 'sitemap.xml' else '', 200

if __name__ == '__main__':
    app.run(debug=True)
