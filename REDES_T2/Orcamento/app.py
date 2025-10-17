from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuração do MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=7306,  # Porta personalizada
    database="rack_management"
)

@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM equipment")
    equipments = cursor.fetchall()
    total_value = sum(equipment['quantity'] * equipment['value'] for equipment in equipments)
    return render_template('index.html', equipments=equipments, total_value=total_value)

@app.route('/add', methods=['GET', 'POST'])
def add_equipment():
    if request.method == 'POST':
        equipment = {
            'name': request.form['name'],
            'description': request.form['description'],
            'model': request.form['model'],
            'quantity': int(request.form['quantity']),
            'unit': request.form['unit'],
            'value': float(request.form['value']),
            'research_link': request.form['research_link']
        }
        cursor = db.cursor()
        cursor.execute("INSERT INTO equipment (name, description, model, quantity, unit, value, research_link) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                        (equipment['name'], equipment['description'], equipment['model'], equipment['quantity'], equipment['unit'], equipment['value'], equipment['research_link']))
        db.commit()
        return redirect(url_for('index'))
    return render_template('add_equipment.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_equipment(id):
    cursor = db.cursor(dictionary=True)
    if request.method == 'POST':
        equipment = {
            'name': request.form['name'],
            'description': request.form['description'],
            'model': request.form['model'],
            'quantity': int(request.form['quantity']),
            'unit': request.form['unit'],
            'value': float(request.form['value']),
            'research_link': request.form['research_link']
        }
        cursor.execute("UPDATE equipment SET name = %s, description = %s, model = %s, quantity = %s, unit = %s, value = %s, research_link = %s WHERE id = %s",
                        (equipment['name'], equipment['description'], equipment['model'], equipment['quantity'], equipment['unit'], equipment['value'], equipment['research_link'], id))
        db.commit()
        return redirect(url_for('index'))
    cursor.execute("SELECT * FROM equipment WHERE id = %s", (id,))
    equipment = cursor.fetchone()
    return render_template('edit_equipment.html', equipment=equipment)

@app.route('/delete/<int:id>')
def delete_equipment(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM equipment WHERE id = %s", (id,))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5001, debug=True)
