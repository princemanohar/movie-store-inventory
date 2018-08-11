from flask import Flask, render_template, request, redirect, url_for
from MovieStoreInventory.db.models.movie_db import fetchFilmDetails, fetchReleaseYear
from MovieStoreInventory.db.models.actor_db import fetchActorDetails, insertActorDetails, fetchActorNameAll
from MovieStoreInventory.db.models.customer_db import fetchCustomerAddresses

app = Flask(__name__)


@app.route('/')
def show_index_page():
    return render_template('index.html')

@app.route('/movies/details')
def hhhh():
    filmdetails = fetchFilmDetails()

    # return json.dumps(filmdetails)
    return render_template('rows_columns.html', result=filmdetails, title="Movies Details",url="http://127.0.0.1:5000/movies/details")


@app.route('/actor/name/details')
def ppp():
    namedetails = fetchActorNameAll()

    # return json.dumps(fetchActorNameAll)
    return render_template('rows_columns.html', result=namedetails, title="Actors Name")


@app.route('/customer/details')
def qqq():
    actoraddressdetails = fetchCustomerAddresses()

    # return json.dumps(fetchActorAddresses)
    return render_template('rows_columns.html', result=actoraddressdetails, title="Address Details")


@app.route('/release/details')
def www():
    releasedetails = fetchReleaseYear()

    # return json.dumps(fetchActorAddresses)
    return render_template('rows_columns.html', result=releasedetails, nvhjmngmhv="Release Details", )


@app.route('/actor/details')
def get_actor_details():
    actorsdetails = fetchActorDetails()

    # return json.dumps(fetchActorAddresses)
    return render_template('rows_columns.html', result=actorsdetails, title="Actors details",url="http://127.0.0.1:5000/input_actor")


# API to show input page
@app.route('/input_actor')
def show_input_actor_page():
    return render_template('input_actor_details.html')


@app.route('/actor', methods=['POST'])
def insert_actor_details():
    fname = request.form['first_name']
    lname = request.form['last_name']
    last_update = request.form['last_update']

    insertActorDetails(fname, lname, last_update)
    return redirect(url_for('get_actor_details'))


if __name__ == '__main__':
    app.run(debug=True)
