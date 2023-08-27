import sqlite3

def create_tables(cr):
    cr.execute('''
    CREATE TABLE IF NOT EXISTS worker (
        id INTEGER PRIMARY KEY NOT NULL,
        name VARCHAR(255),
        surname VARCHAR(255),
        work_rate NUMERIC
    )
    ''')
    cr.execute('''
    CREATE TABLE IF NOT EXISTS material (
        id INTEGER PRIMARY KEY NOT NULL,
        name VARCHAR(255),
        quantity_available INTEGER
    )
    ''')

    cr.execute('''
    CREATE TABLE IF NOT EXISTS client (
        id INTEGER PRIMARY KEY NOT NULL,
        name VARCHAR(255),
        surname VARCHAR(255),
        phone_number VARCHAR(64)
    )
    ''')

    cr.execute('''
    CREATE TABLE IF NOT EXISTS productivity (
        id INTEGER PRIMARY KEY NOT NULL,
        month INTEGER,
        worker_id INTEGER REFERENCES worker(id),
        hours DOUBLE,
        order_quantity INTEGER
    )
    ''')

    cr.execute('''
    CREATE TABLE IF NOT EXISTS shipper (
        id INTEGER PRIMARY KEY NOT NULL,
        name VARCHAR(255),
        contacts TEXT,
        material_id INTEGER REFERENCES material(id),
        price NUMERIC
    )
    ''')

    cr.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY NOT NULL,
        name VARCHAR(255),
        costs NUMERIC,
        qty INTEGER,
        date TIMESTAMP,
        worker_id INTEGER REFERENCES worker(id),
        client_id INTEGER REFERENCES client(id),
        material_id INTEGER REFERENCES material(id)
    )
    ''')

def fill_test_data(cr):
    cr.execute('''
    INSERT INTO client VALUES
    (1, 'Alex', 'Mishuk', '0987654321'),
    (2, 'Mike', 'Olke', '0987436253'),
    (3, 'That', 'Nitshu', '0968574382'),
    (4, 'Sancho', 'Riznuk', '0912834853'),
    (5, 'Mutaho', 'Shevki', '0194837457'),
    (6, 'Keklo', 'Runick', '0877463281')
    ''')

    cr.execute('''
    INSERT INTO worker VALUES
    (1, 'John', 'Jonhyk', 1),
    (2, 'Bob', 'Bobuk', 2)
    ''')

    cr.execute('''
    INSERT INTO material VALUES
    (1, 'Flower 1', 100),
    (2, 'Flower 2', 200)
    ''')

    cr.execute('''
    INSERT INTO shipper VALUES
    (1, 'Company 1', 'Some contact text 1', 1, 1000),
    (2, 'Company 2', 'Some contact text 2', 1, 2000)
    ''')

with sqlite3.connect("flowershop.db") as db:
    cr = db.cursor()
    create_tables(cr)
    cr.execute('SELECT id FROM client LIMIT 1')
    if not cr.fetchone():
        fill_test_data(cr)

    cr.execute('SELECT material_id FROM shipper WHERE material_id = 1')
    result = cr.fetchall()
    for row in result:
        print(row)

    cr.execute('''
    SELECT shipper.name, material.name
    FROM shipper
    LEFT JOIN material ON material.id = shipper.material_id
    WHERE material_id = 1
    ''')
    result = cr.fetchall()
    for row in result:
        print(row)
