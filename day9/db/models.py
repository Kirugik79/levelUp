import psycopg2
conn = psycopg2.connect(database="mydb", user = "postgres", password = "Malakwen", host = "127.0.0.1", port = "5432")
print ("database opened successfully")

cur = conn.cursor()
cur.execute ('''CREATE TABLE users (
        user_id SERIAL PRIMARY KEY NOT NULL,
        first_name VARCHAR(255),
        last_name VARCHAR(255), 
        email VARCHAR(100), 
        username VARCHAR(100),
        password VARCHAR(100));''')

cur = conn.cursor()
cur.execute ('''CREATE TABLE comments (
        comment_id SERIAL PRIMARY KEY NOT NULL,
        comment VARCHAR (255),
        date TIMESTAMP (255), 
        user_id INT );''')

cur = conn.cursor()
cur.execute ('''CREATE TABLE admin (
        admin_id SERIAL PRIMARY KEY NOT NULL,
        username VARCHAR (100),
        password VARCHAR (100));''')
print ("Database Tables created successfully")

cur = conn.cursor()

cur.execute("INSERT INTO users (user_id, first_name, last_name, email, username, password) \
      VALUES (1, 'Robert', 'Kirui', 'rkirui84@gmail.com', 'Robert', 'abc456')");

cur.execute("INSERT INTO comments (comment_id, comment, date, user_id) \
      VALUES (2, 'This is Andela', '20180709', 1)");

cur.execute("INSERT INTO admin (admin_id, username, password) \
      VALUES (3, 'Admin', 'Admin123')");
conn.commit()
print ("Database data inserted successfully")
conn.close()