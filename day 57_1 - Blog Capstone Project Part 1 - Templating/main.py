from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
post_objects = []
# print(posts)
job_posting = posts["job_posting"]
for post in posts:
    post_obj = Post(post_id=1, title="Job Posting", subtitle="CNC Programmer/Operator", body=job_posting)
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)


