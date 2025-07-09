from mysql import connector
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access the environment variables
mysql_host = os.getenv("MYSQL_HOST")
mysql_user = os.getenv("MYSQL_USER")
mysql_password = os.getenv("MYSQL_PASSWORD")
mysql_database = os.getenv("MYSQL_DATABASE")

# Connect to the MySQL database using these variables
conn = connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)

cus = conn.cursor()
def get_user(login_id,password):
    cus.execute("SELECT id FROM User WHERE name = %s AND pass = %s",(login_id,password))
    u = cus.fetchone()
    return u[0] if u else None

def create_user(loing_id,password,email)->None:
    cus.execute("INSERT INTO User (name,pass,email) VALUES (%s,%s,%s)",(loing_id,password,email))
    conn.commit()

def load_data(uid):
    cus.execute("SELECT entry, amount FROM entrys WHERE user_id = %s;", (uid,))
    return cus.fetchall()

def add_data(uid,entry,amount)->None:
    cus.execute("INSERT INTO entrys (user_id, entry, amount) VALUES (%s, %s, %s)", (uid,entry, amount))
    conn.commit()

def add_data_multiple(uid,a)->None:
    for (entry, amount) in a:
        cus.execute("INSERT INTO entrys (user_id, entry, amount) VALUES (%s, %s, %s)", (uid,entry, amount))
        conn.commit()

def delet_data(uid,entry)->None:
    cus.execute("DELETE FROM entrys WHERE user_id = %s AND entry = %s", (uid, entry))
    conn.commit() 

def user_exists(login_id)->bool:
    cus.execute("SELECT id FROM User WHERE name = %s", (login_id,))
    return cus.fetchone() is not None  # Returns True if user exists, False otherwise

def get_total(uid):
    cus.execute("SELECT SUM(amount) FROM  entrys WHERE uid = %s",uid)
    return cus.fetchall()

def delet_user(uid):
    cus.execute("DELETE FROM User WHERE id = %s",(uid,))
    conn.commit()

