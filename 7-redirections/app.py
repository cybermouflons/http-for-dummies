from flask import Flask, make_response, redirect, render_template, request, session, Response
import sqlite3 as sql

app = Flask(__name__)

flag = "flag{hidd3n_1n_pla1n_s1ght}"

@app.route('/')
def home():
    resp = Response(render_template('index.html'))
    return resp


@app.route('/account')
def account():
    if not session.get('logged_in'):
        resp = make_response(render_template('blank.html', flag=flag),301)
        resp.headers['Location'] = "/"
        return resp
    else:
        resp = make_response(render_template('account.html'))
        resp.set_cookie('flag', flag)
        return resp


@app.route('/login', methods=['POST'])
def do_login():

    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    con = sql.connect("database.db")
    cur = con.cursor()

    cur.execute("SELECT * from users WHERE username=?", [POST_USERNAME])
    result = cur.fetchall()
    con.commit()
    con.close()

    if result and POST_PASSWORD == result[0][2]:
        session['logged_in'] = True
        return account()
    else:
        return redirect("/?error=Invalid", code=302)


@app.route("/logout")
def do_logout():
    session['logged_in'] = False
    return home()


if __name__ == "__main__":
    app.secret_key = 'cc35aa50a05fa002d605aac310fc2e055c7a5807b3b8af961103347b3ec4b4ecf83a5ea077177b5b8dd031b29b414c80b075d1216dad40808a9dca80d625094c'
    app.run(debug=False, host='0.0.0.0', port=8086)
