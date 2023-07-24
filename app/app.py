from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
@app.route("/home")
def home():
        return render_template('home.html', title='Home')
        
#Loading the about page
@app.route("/about")
def about():
        return render_template('about.html', title='About')
        
#Loading the play page
@app.route("/play")
def play():
        return render_template('play.html', title='Play')
        
#Loading the support page
@app.route("/support")
def support():
        return render_template('support.html', title='Support')
        
#Loading the login page
@app.route("/login")
def login():
        return render_template('login.html', title='Login')
        
#Loading the login page
@app.route("/signup")
def signup():
        return render_template('signup.html', title='Sign up')
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)