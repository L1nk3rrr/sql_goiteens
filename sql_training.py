import sqlite3

with sqlite3.connect('first.db') as db:
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER,
        book_name VARCHAR(255),
        book_author VARCHAR(255),
        price NUMERIC
    )
    """)
    # Це запис
    # INSERT INTO table_name VALUES (value1, value2, ...), ...
    # cursor.execute("""
    #     INSERT INTO books VALUES
    #         (1, 'Python PRO', 'Robert D.', 1000.50),
    #         (2, 'Ukraine Now', 'Rapich V.', 1500),
    #         (3, 'Now or never', 'Dever B.', 800),
    #         (4, 'Winter', 'Zerlen U.', 500)
    # """)
    
    #query - запит, в просто народі "кверя"
    # * - всі колонки!
    cursor.execute("""
        SELECT *
        FROM books
    """)
    # fetchall - взяти все (вертає list з tuple'ами)
    # fetchone - взяти перший (вертає один tuple)
    result = cursor.fetchall()
    for row in result:
        print(row)

    # SELECT field_name1, field_name2, ...
    # FROM table_name
    cursor.execute("""
        SELECT book_name, price 
        FROM books
    """)
    result = cursor.fetchall()
    for row in result:
        print(row)

    # LIMIT your_number - вказується в кінці квері 
    cursor.execute("""
        SELECT book_name, book_author 
        FROM books
        LIMIT 2
    """)
    result = cursor.fetchall()
    for row in result:
        print(row)



    # UPDATE table_name
    # SET column_name1 = 'str_value',
    #     column_name2 = 100
    # WHERE column_name_id = ... AND/OR ...
    cursor.execute("""
        UPDATE books
        SET price = 500
        WHERE id_book = 1
    """)
    cursor.execute("""
        SELECT id_book, price
        FROM books
        WHERE id_book = 1
    """)
    result = cursor.fetchone() 
    print(result)

    # DELETE FROM table_name
    # WHERE column_name = ...
    cursor.execute("""
        DELETE FROM books
        WHERE id_book = 3
    """)
    cursor.execute("""
        SELECT *
        FROM books
    """)
    result = cursor.fetchall()
    for row in result:
        print(row)
    
    # DROP TABLE table_name - видалення таблички
    cursor.execute("""
        DROP TABLE books
    """)


    #CRUD
    # C REATE - INSERT INTO ...
    # R EAD - SELECT ...
    # U PDATE - UPDATE ...
    # D ELETE - DELETE ...

    # Створити таблицю, що буде містити поля: user_id, username, email_address.
    # Заповнити цю таблицю даними (5 записів).
    
    # CREATE TABLE IF NOT EXIST users(
    # user_id INTEGER,
    # username VARCHAR(255)
    # email_address VARHCHAR(255)
    # )


    # INSERT INTO users VALUES
    #   (1, 'John', 'john@gmail.com'),
    #   (2, 'John', 'john@gmail.com'),
    #   (3, 'John', 'john@gmail.com'),
    #   (4, 'John', 'john@gmail.com'),
    #   (5, 'John', 'john@gmail.com')

    # Прочитати дані зі стовпців user_id та email_address.

    # SELECT user_id, email_address
    # FROM users


    #Змінити username для користувача з айді 4 на «jenna_2002».

    # UPDATE users
    # SET username = '«jenna_2002»'
    # WHERE user_id = 4