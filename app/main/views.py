from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Booking
from .forms import BookingForm
from flask_login import login_required, current_user
from .. import db

@main.route('/')
# @login_required
def index():
    title = 'Studio'


    return render_template('index.html', title =title)

@main.route('/bookings/new_booking', methods = ['GET','POST'])

def new_booking():
    booking_form = BookingForm()

    if booking_form.validate_on_submit():
        booking = Booking(title = booking_form.title.data, day = booking_form.day.data, session = booking_form.session.data, category = booking_form.category.data)

        db.session.add(booking)
        db.session.commit()

        return redirect(url_for('main.index'))



    return render_template('booking.html', booking_form = booking_form )