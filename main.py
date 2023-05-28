from flask import Flask, render_template, url_for
import requests

blog_url = "https://startbootstrap.com/previews/clean-blog"
clean_blog = requests.get(url=blog_url)

app = Flask(__name__)
fetch_data = requests.get("https://api.npoint.io/1f516027f3b6b95114e5")
response = fetch_data.json()
title = (response[0]['title'])
subtitle = (response[0]['subtitle'])
post_number = (response[1]['title'])
body_detail=(response[2]['body'])
print(body_detail)

# print(response[0]['author'])
# print(response[0]['dates'])
# TODO --dynamic static folder css create{{}}

@app.route("/")
def hello_world():
    return render_template("index.html", title1=title, sub1=subtitle, all_posts=response)


@app.route("/<int:post_id>")
def posts(post_id):
    post_body = response[post_id]['body']
    titlepost=response[post_id]['title']
    return render_template("post.html", post=post_body,main_title=titlepost)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
