from flask import Flask, render_template, Response

app = Flask(__name__)

flag = "flag{1ts_always_a_g0od_1d34_t0_ch3ck_the_c0nt3nts_of_n0n_Exist3nt_res0urces}"


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html', flag=flag), 404


@app.route('/')
def home():
    resp = Response(render_template('index.html'))
    return resp


if __name__ == "__main__":
    app.secret_key = 'cc35aa50a05fa002d605aac300fc2e055c7a5807b3b8af961103347b3ec4b4ecf83a5ea077177b5b8dd031b29b414c80b075d1216dad40808a9dca80d625094c'
    app.run(debug=False, host='0.0.0.0', port=8081)
