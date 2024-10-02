import mysql.connector

# for some reason i have to put my port aswell 
# Change accordingly for your own server details
HOST = "localhost"
USER = "root"
PASSWORD = ""
DATABASE = "users"
PORT = 3308

FAIL = '\033[91m'
OK = '\033[92m'
ENDC = '\033[0m'


def connect():
    """
    Connect to the database.
    """
    try:
        mydb = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE,
            port=PORT
        )
        if mydb.is_connected():
            print(f"{OK}Connection established{ENDC}")
            return mydb
    except mysql.connector.Error:
        print(f"{FAIL}Something wrong with connection to server{ENDC}")
        raise SystemExit


def close_connection(database):
    """
    Close the database connection.
    """
    if database and database.is_connected():
        database.close()
        print(f"{OK}Connection closed{ENDC}")
    else:
        print("No open connection to close")


def fetch_table():
    """
    Display table content
    """
    database_connection = connect()
    cursor = database_connection.cursor()
    try:
        query = "SELECT * FROM user"
        cursor.execute(query)
        table = cursor.fetchall()
        return table
    except mysql.connector.Error:
        print(f"{FAIL}Query is not correct{ENDC}")
        raise SystemExit
    finally:
        if cursor:
            cursor.close()
            print(f"{OK}Cursor closed{ENDC}")
        close_connection(database_connection)
        


def display_table():
    """
    Displays items inside users table
    """
    table = fetch_table()

    for item in table:
        print(item)


    # mby return a hashmap with all the objects and print them out later on the web?
    # so key = index, value = object or just skip that and push everything directly to the web


def create_order():
    """
    Add order 
    """

    # push it to order table

def remove_order():
    """
    Remove order
    """
    # remove on index? or create a random order number?
    # pros on index always unique
    # negative order number we can get the same number twice




display_table()
