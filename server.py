from flask import Flask, render_template, request, redirect
# import the class from friend.py


app = Flask(__name__)
from friend import Friend
from mysqlconnection import connectToMySQL


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    all_friends = Friend.get_all()
    print(all_friends)
    return render_template("index.html", all_friends=all_friends)
            
@app.route('/create_friend', methods=["POST"])
def create_friend():

@app.route("/friends/<int:id>")
def show(fiend_id):
    one_friend = Friend.get_one(friend_id)
    return render_template("show.html", one_friend=one_friend)

    Friend.save(request.form)
    return redirect("/")
    
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "occ": request.form["occ"]
    }
    
    Friend.save(data)
    
    return redirect('/')


    

if __name__ == "__main__":
    app.run(debug=True)