 from flask import Flask, render_template, url_for, request
import requests
import smtplib

blog_url = "https://startbootstrap.com/previews/clean-blog"
clean_blog = requests.get(url=blog_url)

app = Flask(__name__)
fetch_data = requests.get("https://api.npoint.io/1f516027f3b6b95114e5")
response = fetch_data.json()
title = (response[0]['title'])
subtitle = (response[0]['subtitle'])
post_number = (response[1]['title'])
body_detail = (response[2]['body'])
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
    titlepost = response[post_id]['title']
    return render_template("post.html", post=post_body, main_title=titlepost)


@app.route("/about")
def about_page():
    return render_template("about.html")


def email_send(name_details, mail):
    my_email = "shlomo.course@gmail.com"
    password = "@@@@@@@"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="shlomo.course@gmail.com"
                            , msg=f"new customer\n\n,{name_details}"
                                  f" \n{mail}")


def do_the_login():
    return 'post'


def show_the_login_form():
    return 'get'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return email_send("eeee33333")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route('/form_entry', methods=['GET', 'POST'])
def receive_data():
    data = request.form
    var1 = 'SENDING...'
    var2 = 'SUCCESS SENT YOR RESPONSE'
    if request.method == "POST":
        first_name = request.form.get("fname")
        customer_mail = request.form.get("mail")
        email_send(first_name, customer_mail)
        print("first_name_____", first_name, customer_mail)
        print(data['fname'],data['mail'])

    return render_template("contact.html", va11=var1, va22=var2)
    # '<h1 align="center" style="color:red;">SUCCESS SENT YOR RESPONSE<h1/>'


if __name__ == "__main__":
    app.run(debug=True)
