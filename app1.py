from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data (you would typically fetch this from a database)
menu_items = [
    {"id": 1, "name": "Burger", "price": 10.0},
    {"id": 2, "name": "Pizza", "price": 12.0},
    {"id": 3, "name": "Salad", "price": 8.0}
]

@app.route('/')
def index():
    return render_template('index.html', menu_items=menu_items)

@app.route('/bill', methods=['POST'])
def generate_bill():
    selected_items = request.form.getlist('item')
    total_cost = sum(float(menu_items[int(item) - 1]['price']) for item in selected_items)
    return render_template('bill.html', total=total_cost)

if __name__ == '__main__':
    app.run(debug=True)
