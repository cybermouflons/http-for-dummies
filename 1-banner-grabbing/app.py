from flask import Flask, render_template, Response

app = Flask(__name__)

flag = "flag{ident1fyinG_th3_t3chn0log1e5_us3d_1s_Sup3r_1mp0rtant}"


@app.after_request
def apply_caching(resp):
    resp.headers['Server'] = flag
    return resp


@app.route('/')
def home():
    resp = Response(render_template('index.html'))
    return resp


if __name__ == "__main__":
    app.secret_key = 'cc35aa50a05fa002d605aac300fc2e055c7a5807b3b8af961103347b3ec4b4ecf83a5ea077177b5b8dd031b29b414c80b075d1216dad40808a9dca80d625094c'
    app.run(debug=False, host='0.0.0.0', port=8080)
