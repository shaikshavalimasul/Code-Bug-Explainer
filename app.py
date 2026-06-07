# from flask import Flask
# from flask import render_template,request,jsonify,redirect,url_for,session
# # render_template - a tool that opens the html from the templates folder and sends them to the browser
# # request - a tool that helps flask receive data sent from the browser(like buggy code user types)
# # jsonify - a tool that converts Python data into Json fromat to send back to browser
# import os
# # it helps python talk to your computer's operating system (Windows in our case )
# # without Os , python cannot access files and folders on our computer
# from dotenv import load_dotenv
# # it opens our .env file and loads all the secret keys into our program
# #import google.generativeai as genai
# # This library helps our python code talk to claude AI
# import requests
# from flask_mysqldb import MySQL
# from werkzeug.security import generate_password_hash,check_password_hash
# from functools import wraps

# load_dotenv()

# app = Flask(__name__)
# app.secret_key=os.getenv("SECRET_KEY")
# # __name__ this is a special python variable that tells flask "this is the main file, start from here"
# # Flask(__)-> we are creating a Flask Application
# OPENROUTER_API_KEY=os.getenv("OPENROUTER_API_KEY")

# app.config['MYSQL_HOST']=os.getenv("MYSQL_HOST")
# app.config['MYSQL_USER']=os.getenv("MYSQL_USER")
# app.config['MYSQL_PASSWORD']=os.getenv("MYSQL_PASSWORD")
# app.config['MYSQL_DB']=os.getenv("MYSQL_DB")

# mysql=MySQL(app)

# # GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
# # genai.configure(api_key=GEMINI_API_KEY)
# # client= google.config(api_key=GEMINI_API_KEY)
# # anthropic.Anthropic() we are creating a connection to claude AI using the anthropic library

# def login_requried(f):
#     @wraps(f)
#     def decorate_function(*args,**kwargs):
#         if 'user_id' not in session:
#             return redirect(url_for('login'))
#         return f(*args,**kwargs)
#     return decorate_function


# '''
# @app.route('/',methods=[])
# def func():
# '''

# @app.route('/')
# @login_requried
# def home():
#     return render_template('index.html',username=session['username'])

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         email = request.form.get('email')
#         password = request.form.get('password')
#         confirm_password = request.form.get('confirm_password')

#         if not username or not email or not password or not confirm_password:
#             return render_template('register.html', error="Please fill all fields!")

#         if password != confirm_password:
#             return render_template('register.html', error="Passwords do not match!")

#         if len(password) < 6:
#             return render_template('register.html', error="Password must be at least 6 characters!")

#         try:
#             cursor = mysql.connection.cursor()
#             cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
#             existing_user = cursor.fetchone()

#             if existing_user:
#                 cursor.close()
#                 return render_template('register.html', error="Email already exists! Please login.")

#             cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
#             existing_username = cursor.fetchone()

#             if existing_username:
#                 cursor.close()
#                 return render_template('register.html', error="Username already taken!")

#             hashed_password = generate_password_hash(password)
#             cursor.execute(
#                 "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
#                 (username, email, hashed_password)
#             )
#             mysql.connection.commit()
#             cursor.close()
#             return redirect(url_for('login'))

#         except Exception as e:
#             print("Register error:", e)
#             return render_template('register.html', error="Something went wrong! Please try again.")

#     return render_template('register.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')

#         if not email or not password:
#             return render_template('login.html', error="Please fill all fields!")

#         try:
#             cursor = mysql.connection.cursor()
#             cursor.execute("SELECT id, username, password FROM users WHERE email = %s", (email,))
#             user = cursor.fetchone()
#             cursor.close()

#             if not user:
#                 return render_template('login.html', error="Email not found! Please register.")

#             if not check_password_hash(user[2], password):
#                 return render_template('login.html', error="Wrong password! Please try again.")

#             session['user_id'] = user[0]
#             session['username'] = user[1]
#             return redirect(url_for('home'))

#         except Exception as e:
#             print("Login error:", e)
#             return render_template('login.html', error="Something went wrong! Please try again.")

#     return render_template('login.html')

# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('login'))

# @app.route('/explain',methods=['POST'])
# @login_requried
# def explain():
#     data=request.get_json()
#     code = data.get('code')
#     language=data.get('language')

# #     message=client.messages.create(model="claude-sonnet-4-20250514",max_tokens=1024,messages=[
# #         {
# #             "role":"user",
# #             "content":f"You are a coding expert. Explain the bug in this {language} code and how to fix it in simple wordds:\n\n{code}"
# #         }
# #     ]
# #     )
# #     explanation=message.content[0].text
# #  # message ->remeber this? it holds Claude's entire response
# #  # .content ->The response has a content section which holds the actual text
# #  # [0]->content is a list, we take the first item (index 0)
# #  # .text-> from that first item, get the actual text
# #   return jsonify({'Explanation':explanation}) 

#     # model=genai.GenerativeModel('gemini-pro')
#     # response=model.generate_content(
#     #     f"You are a coding expert. Explain the bug in this {language} code and how to fix it in simple wordds:\n\n{code}"
#     # ) 
#     # return jsonify({'explanation':response.text})

#     response=requests.post(
#         'https://openrouter.ai/api/v1/chat/completions',
#         headers={
#             'Authorization':f'Bearer {OPENROUTER_API_KEY}',
#             'Content-Type':'application/json',
#         },
#         json={
#             'model':'meta-llama/llama-3.2-3b-instruct:fee',
#             'max_tokens':1000,
#             'messages':[
#                 {
#                     'role':'user',
#                     'content':[
#                         {
#                         'type':'text',
#                         'text':f'You are a coding expert helping a beginner. Analyze this {language} code carefully and provide a COMPLETE explanation including: 1) What the bug is 2) which line has thebug 3) why it is a bug 4) How to fix it with corrected code 5) and also give a additional example of same type also. Always finish your complete explanation:\n\n{code}'
#                         # 'text':f"You are a coding expert. Explain the bug in this {language} code and how to fix it in simple wordds:\n\n{code},And also explain the same code for different examples also give any two examples"
#                         }
#                         ]
#                 }
#             ]
#         }
#     )
#     result=response.json()
#     # explanation=result['choices'][0]['message']['content']
#     # return jsonify({'explanation':explanation})
#     print(result)
#     if 'choices' in result:
#         explanation=result['choices'][0]['message']['content']
#     else:
#         explanation=str(result)
#     cursor = mysql.connection.cursor()
#     cursor.execute("insert into bugs (language,code,explanation,user_id) values(%s,%s,%s,%s)",
#                    (language,code,explanation,session['user_id']))
#     mysql.connection.commit()
#     cursor.close()

#     return jsonify({'explanation':explanation})        

# @app.route('/history')
# @login_requried
# def history():
#     cursor = mysql.connection.cursor()
#     cursor.execute("select language,code,explanation,created_at from bugs where user_id=%s order BY  created_at DESC",(session['user_id'],))
#     bugs=cursor.fetchall()
#     cursor.close()
#     return render_template('history.html',bugs=bugs,username=session['username'])


# if __name__=='__main__':
#     app.run(debug=True) 
# # app.run ->actually starts your flask web server
# # debug=True ->enables debug mode ( Debug mode enables if you make any changes to your code, the server automatically restarts)



from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import os
from dotenv import load_dotenv
import requests
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from collections import Counter
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

if os.environ.get('RENDER'):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bugexplainer.db'
else:
    db_user = os.getenv("MYSQL_USER")
    db_password = os.getenv("MYSQL_PASSWORD")
    db_host = os.getenv("MYSQL_HOST")
    db_name = os.getenv("MYSQL_DB")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_user}:{db_password}@{db_host}/{db_name}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    bugs = db.relationship('Bug', backref='user', lazy=True)

class Bug(db.Model):
    __tablename__ = 'bugs'
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(50))
    code = db.Column(db.Text)
    explanation = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

with app.app_context():
        db.create_all()

def levenshtein_distance(s1, s2):
    rows = len(s1) + 1
    cols = len(s2) + 1

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        matrix.append(row)

    for i in range(rows):
        matrix[i][0] = i
    for j in range(cols):
        matrix[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):
            if s1[i-1] == s2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                top = matrix[i-1][j]
                left = matrix[i][j-1]
                diagonal = matrix[i-1][j-1]
                matrix[i][j] = 1 + min(top, left, diagonal)

    return matrix[rows-1][cols-1]


def similarity_percentage(s1, s2):
    distance = levenshtein_distance(s1, s2)
    max_length = max(len(s1), len(s2))
    if max_length == 0:
        return 100
    similarity = (1 - distance/max_length) * 100
    return round(similarity, 2)



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@login_required
def home():
    return render_template('index.html', username=session['username'])

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if not username or not email or not password or not confirm_password:
            return render_template('register.html', error="Please fill all fields!")
        if password != confirm_password:
            return render_template('register.html', error="Passwords do not match!")
        if len(password) < 6:
            return render_template('register.html', error="Password must be at least 6 characters!")
        try:
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                return render_template('register.html', error="Email already exists!")
            existing_username = User.query.filter_by(username=username).first()
            if existing_username:
                return render_template('register.html', error="Username already taken!")
            hashed_password = generate_password_hash(password)
            new_user = User(username=username, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except Exception as e:
            print("Register error:", e)
            return render_template('register.html', error="Something went wrong!")
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if not email or not password:
            return render_template('login.html', error="Please fill all fields!")
        try:
            user = User.query.filter_by(email=email).first()
            if not user:
                return render_template('login.html', error="Email not found! Please register.")
            if not check_password_hash(user.password, password):
                return render_template('login.html', error="Wrong password! Please try again.")
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('home'))
        except Exception as e:
            print("Login error:", e)
            return render_template('login.html', error="Something went wrong!")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/explain', methods=['POST'])
@login_required
def explain():
    data = request.get_json()
    code = data.get('code')
    language = data.get('language')

    previous_bugs = Bug.query.filter_by(
        user_id=session['user_id']
    ).all()

    for prev_bug in previous_bugs:
        similarity = similarity_percentage(code, prev_bug.code)
        if similarity >= 80:
            return jsonify({
                'explanation': prev_bug.explanation,
                'duplicate': True,
                'similarity': similarity
            })

    response = requests.post(
        'https://openrouter.ai/api/v1/chat/completions',
        headers={
            'Authorization': f'Bearer {OPENROUTER_API_KEY}',
            'Content-Type': 'application/json'
        },
        json={
            'model': 'meta-llama/llama-3.2-3b-instruct:fee',
            'max_tokens': 1000,
            'messages': [
                {
                    'role': 'user',
                    'content': [
                        {
                            'type': 'text',
                            'text': f'You are a coding expert helping a beginner. Analyze this {language} code carefully and provide a COMPLETE explanation including: 1) What the bug is 2) Which line has the bug 3) Why it is a bug 4) How to fix it with corrected code. Always finish your complete explanation:\n\n{code}'
                        }
                    ]
                }
            ]
        }
    )
    result = response.json()
    if 'choices' in result:
        explanation = result['choices'][0]['message']['content']
    else:
        explanation = str(result)

    new_bug = Bug(
        language=language,
        code=code,
        explanation=explanation,
        user_id=session['user_id']
    )
    db.session.add(new_bug)
    db.session.commit()

    return jsonify({
        'explanation': explanation,
        'duplicate': False,
        'similarity': 0
    })

@app.route('/history')
@login_required
def history():
    bugs = Bug.query.filter_by(user_id=session['user_id']).order_by(Bug.created_at.desc()).all()
    return render_template('history.html', bugs=bugs, username=session['username'])

@app.route('/statistics')
@login_required
def statistics():
    bugs = Bug.query.filter_by(user_id=session['user_id']).all()
    
    if not bugs:
        return render_template('statistics.html', 
            username=session['username'],
            total=0,
            language_stats=[])
    
    languages = [bug.language for bug in bugs]
    total = len(languages)
    frequency = Counter(languages)
    frequency_sorted = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    language_stats = []
    for language, count in frequency_sorted:
        percentage = round((count / total) * 100, 1)
        language_stats.append({
            'language': language,
            'count': count,
            'percentage': percentage
        })
    
    most_common = language_stats[0]['language']
    
    return render_template('statistics.html',
        username=session['username'],
        total=total,
        language_stats=language_stats,
        most_common=most_common)

@app.route('/search')
@login_required
def search():
    query = request.args.get('language', '').lower()
    bugs = Bug.query.filter_by(
        user_id=session['user_id']
    ).order_by(Bug.language).all()

    if not query:
        return render_template('history.html',
            bugs=bugs,
            username=session['username'],
            search_query='')

    languages = [bug.language.lower() for bug in bugs]
    found_index = -1
    left = 0
    right = len(languages) - 1

    while left <= right:
        middle = (left + right) // 2
        if languages[middle] == query:
            found_index = middle
            break
        elif languages[middle] < query:
            left = middle + 1
        else:
            right = middle - 1

    if found_index == -1:
        return render_template('history.html',
            bugs=[],
            username=session['username'],
            search_query=query,
            not_found=True)

    result_indices = [found_index]

    i = found_index - 1
    while i >= 0 and languages[i] == query:
        result_indices.append(i)
        i -= 1

    i = found_index + 1
    while i < len(languages) and languages[i] == query:
        result_indices.append(i)
        i += 1

    result_bugs = [bugs[i] for i in result_indices]

    return render_template('history.html',
        bugs=result_bugs,
        username=session['username'],
        search_query=query,
        not_found=False)        

if __name__ == '__main__':
    app.run(debug=True)