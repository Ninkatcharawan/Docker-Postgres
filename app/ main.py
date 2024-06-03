from fastapi import FastAPI
import pandas as pd
from sklearn.linear_model import LogisticRegression
import psycopg2
from sqlalchemy import create_engine

# สร้าง FastAPI instance
app = FastAPI()

# ฟังก์ชันสำหรับโหลดข้อมูลจากฐานข้อมูล
def load_data_from_db():
    # ข้อมูลการเชื่อมต่อฐานข้อมูล
    db_host = "db"
    db_name = "mydb"
    db_user = "myuser"
    db_pass = "mypassword"

    # สร้าง Connection String
    conn_string = f"postgresql://{db_user}:{db_pass}@{db_host}/{db_name}"

    # สร้าง SQLAlchemy Engine
    engine = create_engine(conn_string)

    # ดึงข้อมูลจากตาราง
    query = "SELECT * FROM products"
    data = pd.read_sql_query(query, engine)

    # ปิด Connection
    engine.dispose()

    return data

# แสดงข้อมูลตัวอย่าง
@app.get("/")
def read_root():
    data = load_data_from_db()
    return {"message": "Data from database", "data": data.to_dict('records')}

# ทำนายข้อมูลด้วย Logistic Regression
@app.post("/predict")
def make_prediction(data: dict):
    # โหลดข้อมูลจากฐานข้อมูล
    dataset = load_data_from_db()
    
    # สมมติให้คอลัมน์ 'target' เป็นคอลัมน์ที่ต้องการทำนาย
    X = dataset.drop('target', axis=1)
    y = dataset['target']
    
    # สร้างและฝึกสอนโมเดล Logistic Regression
    model = LogisticRegression()
    model.fit(X, y)
    
    # ทำนายข้อมูลใหม่
    new_data = pd.DataFrame(data, index=[0])
    prediction = model.predict(new_data)
    
    return {"prediction": prediction.tolist()}