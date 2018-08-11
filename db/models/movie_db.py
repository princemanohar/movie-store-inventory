import MySQLdb
import json

# Open database connection
db = MySQLdb.connect("localhost", "root", "root")

'''
Thsi function give the details of the movie when ve give any film_id
'''


def fetchFilmDetails():
    db = MySQLdb.connect("localhost", "root", "root")
    cursor = db.cursor()

    query = " select film_id,title,description,release_year,language_id from sakila.film " \
        # " LIMIT 10 "
    # " where film_id =  " + str()

    print(query)
    cursor.execute(query)

    kkk = cursor.fetchall()

    final_op = []

    for entry in kkk:
        op1 = {"film_id": entry[0], "title ": entry[1], "discription": entry[2], "release_year": str(entry[3]),
               "language_id": entry[4]}
        final_op.append(op1)

    # db.close()

    return final_op


if __name__ == "__main__":
    pass
    #acc = fetchFilmDetails()
    #print(json.dumps(acc, indent=2))

def insertMoviesDetails(title,description,release_year,language_id):
    insert_query = '''INSERT INTO sakila.film (title,description,release_year,language_id) 
                    VALUES (%s,%s,%s,%s)'''
    args = (title,description,release_year,language_id)

    cursor = db.cursor()
    cursor.execute(insert_query, args)

    if cursor.lastrowid:
        print('last insert id', cursor.lastrowid)
    else:
        print('last insert id not found')

    db.commit()
    cursor.close()

if __name__ == "__main__":
    insertMoviesDetails('ABCD','A Movie wilt lots for dance on different differet forms.','2016','01')


def fetchReleaseYear():
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    query = " select f.release_year, " + \
            " count(*) as No_of_Actors_Acted_That_Year " + \
            " from sakila.film as f " + \
            " join sakila.film_actor as fa " + \
            " on f.film_id = fa.film_id "
    cursor.execute(query)

    results = cursor.fetchall()

    final_op = []

    for entry in results:
        op1 = {"release_year": entry[0], "No_of_Actors_Actrd_That_Year ": entry[1]}
        final_op.append(op1)

    # disconnect from server
    # db.close()

    return final_op
    # fetchReleaseYear()
