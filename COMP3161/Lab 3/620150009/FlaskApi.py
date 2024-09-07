from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Helper function to get database connection
def get_db():
    conn = mysql.connector.connect(user='root', password='jimjones2266',
                                host='127.0.0.1',
                                database='customer_data')
    return conn

# Endpoint to get all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Customers;')
    customers = cursor.fetchall()
    conn.close()
    return jsonify(customers)

# Endpoint to get customer by ID
@app.route('/customer/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Customers WHERE CustomerID = ?;', (customer_id,))
    customer = cursor.fetchall()
    conn.close()
    if customer:
        return jsonify(customer)
    else:
        return jsonify({'error': 'Customer not found'}), 404

# Endpoint to add customer
@app.route('/add_customer', methods=['POST'])
def add_customer():
    customer_data = request.json
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Customers (CustomerID, Gender, Age, AnnualIncome, SpendingScore, Profession, WorkExperience, FamilySize) VALUES (?, ?, ?, ?, ?, ?, ?, ?);', 
                    (customer_data['CustomerID'], customer_data['Gender'], customer_data['Age'], customer_data['AnnualIncome'], customer_data['SpendingScore'], 
                     customer_data['Profession'], customer_data['WorkExperience'], customer_data['FamilySize']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Customer added successfully'})

# Endpoint to update profession by customer ID
@app.route('/update_profession/<int:customer_id>', methods=['PUT'])
def update_profession(customer_id):
    profession_data = request.json
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE Customers SET Profession = ? WHERE CustomerID = ?;', (profession_data['Profession'], customer_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Profession updated successfully'})

# Endpoint to get highest income earners by profession
@app.route('/highest_income_report', methods=['GET'])
def highest_income_report():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT CustomerID, AnnualIncome, Profession FROM Customers ORDER BY AnnualIncome DESC;')
    rows = cursor.fetchall()
    conn.close()

    # Create a dictionary to store the highest income earners by profession
    highest_income_report = {}
    for row in rows:
        customer_id, annual_income, profession = row
        if profession not in highest_income_report or annual_income > highest_income_report[profession]['AnnualIncome']:
            highest_income_report[profession] = {
                'CustomerID': customer_id,
                'AnnualIncome': annual_income,
                'Profession': profession
            }

    # Convert the dictionary values to a list
    report_list = list(highest_income_report.values())
    return jsonify(report_list)

# Endpoint to get total income earned by profession
@app.route('/total_income_report', methods=['GET'])
def total_income_report():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(AnnualIncome) AS TotalIncome, Profession FROM Customers GROUP BY Profession;')
    report = cursor.fetchall()
    conn.close()
    return jsonify(report)

# Endpoint to get average work experience by profession for young high earners
@app.route('/average_work_experience', methods=['GET'])
def average_work_experience():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT AVG(WorkExperience) AS AverageExperience, Profession FROM Customers WHERE AnnualIncome > 50000 AND Age < 35 GROUP BY Profession;')
    report = cursor.fetchall()
    conn.close()
    return jsonify(report)

# Endpoint to get average spending score by gender for a specific profession
@app.route('/average_spending_score/<profession>', methods=['GET'])
def average_spending_score(profession):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT Gender, AVG(SpendingScore) AS AverageSpendingScore FROM Customers WHERE Profession = ? GROUP BY Gender;', (profession,))
    report = cursor.fetchall()
    conn.close()
    return jsonify(report)

# Run the Flask app
if __name__ == '__main__':
    app.run(port=6000)
