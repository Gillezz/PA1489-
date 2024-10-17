import mysql.connector

# for some reason i have to put my port aswell 
# Change accordingly for your own server details
HOST = "localhost"
USER = "root"
PASSWORD = ""
DATABASE = "burger"
PORT = 3308

FAIL = '\033[91m'
OK = '\033[92m'
ENDC = '\033[0m'


def validate_if_database_exists():
    conn = mysql.connector.connect(
        host = HOST,
        user = USER,
        password = PASSWORD,
        port=PORT
    )


    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS burger")
    cursor.execute("USE burger")

    create_table_query = """
    CREATE TABLE IF NOT EXISTS `orders` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `burgerName` varchar(50) NOT NULL,
    `tomato` tinyint(1) NOT NULL,
    `lettuce` tinyint(1) NOT NULL,
    `onion` tinyint(1) NOT NULL,
    `cheese` tinyint(1) NOT NULL,
    `bun` tinyint(1) NOT NULL,
    `meat` tinyint(1) NOT NULL,
    `bacon` tinyint(1) NOT NULL,
    `mockMeat` tinyint(1) NOT NULL,
    `cucumber` tinyint(1) NOT NULL,
    `chicken` tinyint(1) NOT NULL,
    `jalapeno` tinyint(1) NOT NULL,
    PRIMARY KEY (`id`)
    )
    """
    cursor.execute(create_table_query)

    if cursor:
        cursor.close()
        print(f"{OK}Cursor closed{ENDC}")

    close_connection(conn)




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
        query = "SELECT * FROM orders"
        cursor.execute(query)
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        return create_diconary(column_names, rows)
    except mysql.connector.Error:
        print(f"{FAIL}Query is not correct{ENDC}")
        raise SystemExit
    finally:
        if cursor:
            cursor.close()
            print(f"{OK}Cursor closed{ENDC}")
        close_connection(database_connection)

def is_ingredient(ingridient):
    if ingridient:
        return True
    return False

        
def create_diconary(columns, rows):
    # create new list with tuples
    new_list = list()
    for tuple_list in rows:
        temp_list = []
        for index in range(1, len(tuple_list)):
             if index == 1:
                 temp_list.append(tuple_list[index])
                 continue
             if tuple_list[index]:
                 temp_list.append(columns[index])
            
                 
        new_list.append(tuple(temp_list))

    return new_list


def display_table():
    """
    Displays items inside users table
    """

    # from the database i would probably like to get objects and from the objects i can get the infomration json format?
    # so this method should probably return a list of objects

    # column_row_list = fetch_table()

    # for tup in column_row_list:
    #     print(tup)
         

    # print(result)
    # return result
    # mby return a hashmap with all the objects and print them out later on the web?
    # so key = index, value = object or just skip that and push everything directly to the web


def create_order(burger_dict):
    """
    Add order 
    """
    database_connection = connect()
    cursor = database_connection.cursor()
    try:

        # perhaps there is a method that can  take a dictonary and create the query for itself or i have to create that for myself 
        #
        query = """
        INSERT INTO orders (burgerName, tomato, lettuce, onion, cheese, bun, meat, bacon, mockMeat, cucumber, chicken,jalapeno) 
        VALUES (%(burgerName)s, %(tomato)s, %(lettuce)s, %(onion)s, %(cheese)s,%(bun)s,%(meat)s,%(bacon)s,%(mockMeat)s,%(cucumber)s,%(chicken)s,%(jalapeno)s)
        """
        cursor.execute(query,burger_dict)
        database_connection.commit() 

    except mysql.connector.Error:
        print(f"{FAIL}Query is not correct{ENDC}")
        raise SystemExit
    finally:
        if cursor:
            cursor.close()
            print(f"{OK}Cursor closed{ENDC}")
        close_connection(database_connection)
    
    # push it to order table

def remove_order(id):
    """
    Remove order
    """
    # remove on index? or create a random order number?
    # pros on index always unique
    # negative order number we can get the same number twice

    database_connection = connect()
    cursor = database_connection.cursor()

    try:
        query = f"DELETE FROM orders WHERE id = {id}"
        cursor.execute(query)
        database_connection.commit()
    except mysql.connector.Error:
        print(f"{FAIL}Query is not correct{ENDC}")
        raise SystemExit
    finally:
        if cursor:
            cursor.close()
            print(f"{OK}Cursor closed{ENDC}")
        close_connection(database_connection)

validate_if_database_exists()
