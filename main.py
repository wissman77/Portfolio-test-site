from flask import Flask, render_template, url_for, request, flash, redirect
import datetime
import os

app = Flask(__name__)
app.secret_key = 'Very_Strong_Secret_Key_12321122111'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/programs')
def programs():
    return render_template('programs.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact(is_ok=0):
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        if not name:
            flash('Name is requried')
        if not email:
            flash('Email is requried')
        if not message:
            flash('Message is requried')

        if not name or not email or not message:
            return redirect(url_for('contact'))

        if not os.path.exists('/messages'):
            os.mkdir('messages')

        with open(f"messages/{datetime.datetime.now().timestamp()}.txt", "w") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Message: {message}\n")
        flash('Thank for contacting me!')
        return redirect(url_for('contact'))

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
