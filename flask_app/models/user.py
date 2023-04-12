# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# model the class after the friend table from our database


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    # Method for getting all users in the database. Returns a list of user objects
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for person in results:
            users.append(cls(person))
        return users

    # Method to get a single user. Returns user object
    @classmethod
    def get_by_id(cls, id):
        data = {'id': id}
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        user = cls(results[0])
        return user

    # Method for adding a new user to the database
    @classmethod
    def save(cls, data):
        query = 'INSERT into users ( first_name, last_name, email, created_at, updated_at) values (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() );'
        return connectToMySQL(DATABASE).query_db(query, data)

    # Method for updating an existing user
    @classmethod
    def update(cls, data):
        # print('in the update method')
        query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    # Method for deleting a user from the database
    @classmethod
    def delete_by_id(cls, data):
        query = 'DELETE from users WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)
