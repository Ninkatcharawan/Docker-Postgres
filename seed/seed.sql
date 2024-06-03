-- seed.sql

-- สร้างตารางสำหรับเก็บข้อมูลผลิตภัณฑ์
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

-- นำเข้าข้อมูลผลิตภัณฑ์ตัวอย่าง
INSERT INTO products (name, price) VALUES
    ('Product A', 19.99),
    ('Product B', 29.95),
    ('Product C', 9.99);

-- สร้างตารางสำหรับเก็บข้อมูลลูกค้า
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

-- นำเข้าข้อมูลลูกค้าตัวอย่าง
INSERT INTO customers (name, email) VALUES
    ('John Doe', 'john@example.com'),
    ('Jane Smith', 'jane@example.com');