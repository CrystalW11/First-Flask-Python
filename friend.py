# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append(cls(friend))
        return friends
            
@classmethod
def save(cls, data):
    query = """INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)
    VALUES (%(fname)s, %(lname)s, %(occ)s, NOW(), NOW()):"""
    
    return connectToMySQL('cls.DB') .query_db(query, data)

@classmethod
def get_one(cls, id):
    query = """SELECT * FROM friends
            WHERE id = %(id)s """
    results = connectToMySQL(cls.DB).query_db(query, {"id":id})
    return  cls(results[0])

@classmethod
def get_all(cls):
    query = "SELECT * FROM friends;"
    results = connectToMySQL(cls.DB).query_db(query)
    
    all_friends = []
    for row in results:
        
        all_friends.append(cls(row))
    return results