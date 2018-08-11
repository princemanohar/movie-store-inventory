import MySQLdb
import json

# Open database connection
db = MySQLdb.connect("localhost", "root", "root")


def fetchActorNameAll():
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    cursor.execute("SELECT first_name, last_name FROM sakila.actor  ")
    # "where actor_id>50 and actor_id<100")

    results = cursor.fetchall()

    final_op = []

    for entry in results:
        op1 = {"first_name": entry[0], "last_name ": entry[1]}
        final_op.append(op1)
        # disconnect from server
    # db.close()
    return final_op


# fetchActorNameAll()



def fetchActorDetailsByID(actorid):
    cursor = db.cursor()

    query = " SELECT actor_id,first_name, last_name, last_update FROM sakila.actor " \
            " where actor_id = " + str(actorid)
    print(query)
    cursor.execute(query)

    results = cursor.fetchall()

    final_op = []

    for entry in results:
        op1 = {"actor_id": entry[0], "first_name": entry[1], "last_name": entry[2], "last_update": entry[3]}
        final_op.append(op1)

    # db.close()

    return final_op


# fetchActorDetailsByID(1008)

def fetchActorDetails():
    cursor = db.cursor()

    query = " SELECT actor_id,first_name, last_name, last_update FROM sakila.actor " \
        # " where actor_id >0 " + str(  )
    print(query)
    cursor.execute(query)

    results = cursor.fetchall()

    final_op = []

    for entry in results:
        op1 = {"actor_id": entry[0], "first_name": entry[1], "last_name": entry[2], "last_update": entry[3]}
        final_op.append(op1)

    # db.close()

    return final_op


# abc = fetchActorDetails(89)

def insertActorDetails(first_name, last_name, last_update):
    insert_query = '''INSERT INTO sakila.actor (first_name,last_name,last_update)
                   VALUES (%s,%s,%s)'''
    args = (first_name, last_name, last_update)

    cursor = db.cursor()
    cursor.execute(insert_query, args)

    if cursor.lastrowid:
        print('last insert id', cursor.lastrowid)
    else:
        print('last insert id not found')

    db.commit()
    cursor.close()


if __name__ == "__main__":
    insertActorDetails('3456789', 'Singh098', '2018-8-10 1:38:34')
