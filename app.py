from flask import Flask, render_template

app = Flask(__name__)


PROJECT_NAME = 'HCP'

@app.route('/')
def home():
	return 'Hello, world!'

@app.route('/about')
def about():
	return render_template("about.html", PROJECT_NAME=PROJECT_NAME)

if __name__ == '__main__':
	app.run(debug=True)
