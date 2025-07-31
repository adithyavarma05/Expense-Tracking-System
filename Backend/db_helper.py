import mysql.connector
from contextlib import contextmanager
import my_logger
log=my_logger.my_log("db_helper")

@contextmanager
def get_db_cursor(commit=False):
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kushi@05",
        database="expense_manager"
    )
    log.info("Successfully Connected with the database")
    cursor=connection.cursor(dictionary=True)
    log.info("Successfully Created Cursor")
    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    log.info("Successfully Closed the Cursor")
    connection.close()
    log.info("Successfully closed the connection with the database")

def fetch_expenses_for_date(expense_date):
    log.info("Started Fetching the data using date")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date=%s", (expense_date,))
        expenses=cursor.fetchall()
        log.info("Successful Fetching the data using date")
        return expenses

def insert_into_expenses(expense_date,amount,category,notes):
    log.info("Started Inserting the data into the database")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date,amount,category,notes) VALUES (%s,%s,%s,%s)",
            (expense_date,amount,category,notes)
        )
        log.info("Successful Inserted the data into the database")

def delete_expenses_for_date(expense_date):
    log.info("Deleting the data from the database with date")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "DELETE FROM expenses WHERE expense_date=%s",(expense_date,)
        )
        log.info("Successfully Deleted the data from the database with date")

def fetch_data_between_dates(expense_date_1, expense_date_2):
    log.info("Fetching the data from the database between the dates")
    with get_db_cursor() as cursor:
        cursor.execute("""
            SELECT category,SUM(amount) AS Total FROM expenses
            WHERE expense_date BETWEEN %s AND %s
            GROUP BY category;
            """, (expense_date_1, expense_date_2))
        data=cursor.fetchall()
        log.info("Successfully Fetched the data from the database between the dates")
        return data

def fetch_data_months():
    log.info("Fetching the data from the database between for the months")
    with get_db_cursor() as cursor:
        cursor.execute("""
            SELECT 
                MONTH(expense_date) AS month_number,
                MONTHNAME(expense_date) AS month_name,
                SUM(amount) AS total
            FROM expenses
            GROUP BY MONTH(expense_date), MONTHNAME(expense_date)
            ORDER BY month_number;
                       """)
        data=cursor.fetchall()
        log.info("Successfully Fetched the data from the database between the months")
        return data

if __name__ == "__main__":
    my_data=fetch_expenses_for_date("2024-08-26")
    print(my_data)
    # for expense in my_data:
    #     print(expense)
