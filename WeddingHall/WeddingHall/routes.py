from flask import render_template, request, session, redirect, url_for
from WeddingHall import app, db
from WeddingHall.models import AdminPanel, Booking

# Define the route functions here, as shown in the provided code
@app.route('/', methods=['GET', 'POST'])
def login():
    session.pop('logged_in', None)
    session.pop('username', None)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = AdminPanel.query.filter_by(ad_name=username, password=password).first()

        if user:
            session['logged_in'] = True
            session['username'] = user.ad_name
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid credentials")

    return render_template('login.html', error=None)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['number']
        date = request.form['date']
        guest = request.form['guest']
        hall = request.form['hall']

        existing_data = Booking.query.filter_by(name=name, mobile=mobile, date=date, guest=guest, hall=hall).first()

        if not existing_data:
            new_booking = Booking(name=name, mobile=mobile, date=date, guest=guest, hall=hall)
            db.session.add(new_booking)

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return render_template('add.html', error=str(e))

        return redirect('/booking')

    return render_template('add.html')


@app.route('/booking')
def bookings():
    booking = Booking.query.order_by(Booking.date.asc()).all()
    return render_template('booking.html', booking=booking)


@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        update_for = request.form['name']
        contact = request.form['number']
        old_date = request.form['olddate']
        old_hall = request.form['hall']
        new_date = request.form['newdate']
        new_hall = request.form['newhall']

        existing_entry = Booking.query.filter_by(name=update_for, mobile=contact, date=old_date, hall=old_hall).first()

        if existing_entry:
            if new_date:
                existing_entry.date = new_date

            if new_hall and new_hall != "Select a Hall":
                existing_entry.hall = new_hall

            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return render_template('booking.html', error=str(e))

        return redirect('/booking')


@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['number']
        date = request.form['date']
        hall = request.form['hall']

        existing_data = Booking.query.filter_by(name=name, mobile=contact, date=date, hall=hall).first()

        if existing_data:
            db.session.delete(existing_data)

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return render_template('booking.html', error=str(e))

        return redirect('/booking')


@app.route('/index')
def index():
    if session.get('logged_in'):
        return render_template('index.html', username=session['username'])
    else:
        return redirect(url_for('login'))


@app.route('/hall1')
def hall1():
    return render_template('hall1.html')


@app.route('/hall2')
def hall2():
    return render_template('hall2.html')


@app.route('/hall3')
def hall3():
    return render_template('hall3.html')


@app.route('/hall4')
def hall4():
    return render_template('hall4.html')


@app.route('/hall5')
def hall5():
    return render_template('hall5.html')
