from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField, SelectField


class Update(FlaskForm):
    group = SelectField('Food Group:', coerce=int)
    longdes = StringField('Long Description:',
                           validators=[DataRequired(), Length(min=2, max=500)])
    shortdes = StringField('Short Description:',
                           validators=[DataRequired(), Length(min=2, max=500)])
    manu = StringField('Manufacturer Name:',
                           validators=[DataRequired(), Length(min=2, max=500)])
    sci = StringField('Scientific Name:',
                           validators=[DataRequired(), Length(min=2, max=500)])

    submit = SubmitField('Update Food')
