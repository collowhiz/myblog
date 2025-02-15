from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    blog_url = 'https://api.npoint.io/faf51f28586ed5854630'
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

