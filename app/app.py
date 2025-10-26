import secrets
# from werkzeug.security import gen_salt
# print(gen_salt(32))


secret_key = secrets.token_urlsafe(32)
print(secret_key)

# aplicacion de muestra

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def inicial():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)