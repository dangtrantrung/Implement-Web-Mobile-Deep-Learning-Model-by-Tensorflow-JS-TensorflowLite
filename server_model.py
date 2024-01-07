
from flask import Flask, render_template
from flask_cors import CORS, cross_origin

# Khởi tạo Flask
app = Flask(__name__)

# Apply Flask - CORS
CORS(app)
app.config['CORS_HEADERS'] ='Content-Type'


# Hàm xử lý request
@app.route("/", methods=['GET'])
# @cross_origin()
def home_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(ssl_context='adhoc',host='0.0.0.0', debug=False)