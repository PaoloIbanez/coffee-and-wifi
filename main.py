from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location URL', validators=[DataRequired(), URL()])
    open_time = TimeField('Open Time (e.g. 8AM)', validators=[DataRequired()], format='%H:%M')
    close_time = TimeField('Close Time (e.g. 8PM)', validators=[DataRequired()], format='%H:%M')
    coffee = SelectField('Coffee Rating', choices=["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating', choices=["✘", "📶", "📶📶", "📶📶📶", "📶📶📶📶", "📶📶📶📶📶"], validators=[DataRequired()])
    power = SelectField('Power Socket Availability', choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([
                form.cafe.data,
                form.location.data,
                form.open_time.data.strftime('%I:%M %p'),
                form.close_time.data.strftime('%I:%M %p'),
                form.coffee.data,
                form.wifi.data,
                form.power.data,
            ])
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)



@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
