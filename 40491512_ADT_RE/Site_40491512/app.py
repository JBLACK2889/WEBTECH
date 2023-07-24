from flask import Flask, url_for, render_template,  request, session, redirect, flash
app = Flask(__name__)

#-----------------------Loads the navigation bar main pages---------------

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
        
#Loading the sign up page
@app.route("/signup", methods=['POST', 'GET'])
def signup():
    return render_template('signup.html', title='Signup')
        

        
 #-------------------------Question Pathways------------------------------

#First the paths for the animated movie questions
#Loads question one  
@app.route("/ANIMATIONQ1")
def animationq1():
    return render_template('ANIMATIONQ1.html', title="Animation Q1")
    
#Loads question two  
@app.route("/ANIMATIONQ2")
def animationq2():
    return render_template('ANIMATIONQ2.html', title="Animation Q2")

#Loads question three 
@app.route("/ANIMATIONQ3")
def animationq3():
    return render_template('ANIMATIONQ3.html', title="Animation Q3")
    
#Loads question four  
@app.route("/ANIMATIONQ4")
def animationq4():
    return render_template('ANIMATIONQ4.html', title="Animation Q4")
    
#Loads question five
@app.route("/ANIMATIONQ5")
def animationq5():
    return render_template('ANIMATIONQ5.html', title="Animation Q5")
    
    
#Next, the paths for the classic movie questions
#Loads question one  
@app.route("/classicq1")
def classicq1():
    return render_template('CLASSICQ1.html', title="Classic Q1")
    
#Loads question two  
@app.route("/classicq2")
def classicq2():
    return render_template('CLASSICQ2.html', title="Classic Q2")

#Loads question three 
@app.route("/classicq3")
def classicq3():
    return render_template('CLASSICQ3.html', title="Classic Q3")
    
#Loads question four  
@app.route("/classicq4")
def classicq4():
    return render_template('CLASSICQ4.html', title="Classic Q4")
    
#Loads question five
@app.route("/classicq5")
def classicq5():
    return render_template('CLASSICQ5.html', title="Classic Q5")
    
  
#Finally, the paths for the "horror" questions
#Loads question one  
@app.route("/HORRORQ1")
def horrorq1():
    return render_template('HORRORQ1.html', title="Horror Q1")
    
#Loads question two  
@app.route("/HORRORQ2")
def horrorq2():
    return render_template('HORRORQ2.html', title="Horror Q2")

#Loads question three 
@app.route("/HORRORQ3")
def horrorq3():
    return render_template('HORRORQ3.html', title="Horror Q3")
    
#Loads question four  
@app.route("/HORRORQ4")
def horrorq4():
    return render_template('HORRORQ4.html', title="Horror Q4")
    
#Loads question five
@app.route("/HORRORQ5")
def horrorq5():
    return render_template('HORRORQ5.html', title="Horror Q5")


#------------------Finally, the pages for winning or losing the quiz---------

#Loading the game over page
@app.route("/gameover")
def gameover():
        return render_template('gameover.html', title='Game Over')
        
#Loads the 'winner' page
@app.route("/WINNER")
def winner():
        return render_template('winner.html', title='Winner')

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)