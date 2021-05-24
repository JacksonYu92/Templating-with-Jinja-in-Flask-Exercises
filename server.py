from flask import Flask, render_template
import random
from datetime import datetime
import requests

def find_gender(name):
    gender_param = {
        "name": name,
    }
    gender_response = requests.get("https://api.genderize.io", params=gender_param)
    gender_data = gender_response.json()
    gender = gender_data['gender']
    return gender

def find_age(name):
    age_param = {
        "name": name,
    }
    age_response = requests.get("https://api.agify.io", params=age_param)
    age_data = age_response.json()
    age = age_data['age']
    return age

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.today().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    gender = find_gender(name)
    age = find_age(name)
    return render_template("guess.html", name=name.title(), gender=gender, age=age)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)