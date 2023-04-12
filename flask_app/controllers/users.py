from flask_app import app
from flask import render_template, redirect, redirect, request
from flask_app.models.user import User


# main page showing all users
@app.route("/users")
def show_users():
    users = User.get_all()
    return render_template("read.html", users=users)


# Page showing a single user profile
@app.route('/users/<int:id>')
def show_single_user(id):
    user = User.get_by_id(id)
    return render_template('single_user.html', user=user)


# Form to create a new user
@app.route('/users/new')
def create_page():
    return render_template('create.html')


# Form for editing a user
@app.route('/users/<int:id>/edit')
def edit_a_user(id):
    user = User.get_by_id(id)
    return render_template('edit.html', user=user)


# create database entry for new user and redirect to that user's page
@app.route('/add_user', methods=['POST'])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    user = User.save(data)
    return redirect('/users/' + str(user))


# Updates database entry for a user and redirects to that user's page
@app.route('/update_user', methods=['POST'])
def update_a_user():
    data = {
        'id': request.form['id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    User.update(data)
    return redirect('/users/' + str(request.form['id']))


# Deletes database entry for a user then redirects to main page
@app.route('/users/<int:id>/delete')
def remove_a_user(id):
    data = {'id': id}
    User.delete_by_id(data)
    return redirect('/users')
