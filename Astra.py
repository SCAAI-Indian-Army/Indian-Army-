from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route("/")
def login():
	return render_template("login.html")

@app.route("/logout")
def logout():
 	return redirect("/")

@app.route("/main_menu")
def main_menu():
 	return render_template("admin_dashboard.html")

@app.route("/create_user")
def create_user():
 	return render_template("Create_User.html")

@app.route("/add_New")
def add_New():
 	return render_template("Add_Person_Record.html")

@app.route("/search")
def search():
 	return render_template("search_menu.html")

@app.route("/search_name")
def search_name():
	return render_template("search_name.html")

@app.route("/search_location")
def search_location():
	return render_template("search_Location.html")

@app.route("/view")
def view():
	return render_template("profile_Card_try.html")

@app.route("/view_vehicle")
def view_vehicle():
	return render_template("vehicle_Card_try.html")

@app.route("/back")
def back():
	return redirect("/main_menu") 
