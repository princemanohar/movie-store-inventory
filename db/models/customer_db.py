import MySQLdb
import json

# Open database connection
db = MySQLdb.connect("localhost", "root", "root")


def fetchCustomerAddresses():
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    quweye = "SELECT c.first_name,c.last_name,c.email,a.address " + \
             " from sakila.customer as c " + \
             " inner join sakila.address  as a " + \
             " on c.address_id = a.address_id "
    print(quweye)
    cursor.execute(quweye)

    results = cursor.fetchall()

    final_op = []

    for entry in results:
        op1 = {"first_name": entry[0], "last_name ": entry[1], "email": entry[2], "address": entry[3]}
        final_op.append(op1)

    # disconnect from server
    # db.close()
    return final_op
    # fetchCustomerAddresses()
