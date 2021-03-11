from flask_wtf import FlaskForm
from wtforms.validators import Required, Email, EqualTo
from wtforms import StringField, SubmitField,RadioField
from wtforms import SelectField, IntegerField

class BookingForm(FlaskForm):
    email = StringField('Enter email to recieve reciept', validators=[Required(), Email()] )
    title = SelectField('Session Type', choices=[('Music Record', 'Music Record'),('Photo Session', 'Photo Session')])
    day = SelectField('Days', choices =[('Monday','Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),('Thursday','Thursday'),('Friday','Friday')])
    session = SelectField('Session', choices=[('Morning Session', 'Morning Session'),('Midday Session','Midday Session'),('Evening Session','Evening Session')])
    category = SelectField('Category', choices =[('Video Record','Video Record'),('Photo Session','Photo Session'),('Music Record','Music Record')])
    submit = SubmitField('Book now')

