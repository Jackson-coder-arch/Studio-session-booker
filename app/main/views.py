from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Booking
from .forms import BookingForm, updateProfile
from flask_login import login_required, current_user
from .. import db,photos

@main.route('/')
@login_required
def index():


    return render_template('index.html')


@main.route('/booking/new_booking', methods = ['GET','POST'])
@login_required
def new_booking():
    booking_form = BookingForm()
    title = 'Welcome Book with us and get the best deals in town'
    booking = Booking.query.all()


    if booking_form.validate_on_submit():
        booking = Booking(email = booking_form.email.data, title = booking_form.title.data, day = booking_form.day.data, session = booking_form.session.data, category = booking_form.category.data)

        db.session.add(booking)
        db.session.commit()

        return redirect(url_for('main.new_booking'))

    

    return render_template('booking.html', booking_form = booking_form, bookings = booking, title = title )


@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user)

@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))

    return render_template('profile/update.html', form = form)

@main.route('/user/<uname>/update/pic', methods = ['POST'])
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile', uname = uname))