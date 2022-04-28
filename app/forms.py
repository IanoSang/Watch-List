from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import input_required


class ReviewForm(FlaskForm):
    title = StringField('Review title', validators=[input_required()])
    review = TextAreaField('Movie review', validators=[input_required()])
    submit = SubmitField('Submit')
