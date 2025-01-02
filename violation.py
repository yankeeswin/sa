from flask import Flask, request, render_template, jsonify
import psycopg2

app = Flask(__name__)

# 配置 PostgreSQL 連接，請填入你的使用者名稱和密碼
db = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="1234",  # 這裡填入你的 PostgreSQL 密碼
    database="violations_db"
)

@app.route('/')
def index():
    return render_template('violation.html')

@app.route('/save_record', methods=['POST'])
def save_record():
    vehicle_number = request.form.get('vehicle_number')
    owner_name = request.form.get('owner_name')
    date = request.form.get('date')
    location = request.form.get('location')
    description = request.form.get('description')
    fine_amount = request.form.get('fine_amount')
    
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO violation_records (vehicle_number, owner_name, date, location, description, fine_amount)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (vehicle_number, owner_name, date, location, description, fine_amount))
    db.commit()
    
    cursor.close()
    
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)