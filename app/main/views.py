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


@main.route('/booking/new_booking', methods = ['GET','POST'])

def new_booking():
    booking_form = BookingForm()
    title = 'Welcome Book with us a session'
    booking = Booking.query.all()


    if booking_form.validate_on_submit():
        booking = Booking(email = booking_form.email.data, title = booking_form.title.data, day = booking_form.day.data, session = booking_form.session.data, category = booking_form.category.data)

        db.session.add(booking)
        db.session.commit()

        return redirect(url_for('main.new_booking'))

    # if new_booking.query.filter(user=request.user).count()>=3:
    #     return redirect('Book the remaining days')



    return render_template('booking.html', booking_form = booking_form, bookings = booking, title = title )