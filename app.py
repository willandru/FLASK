from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def index():

	data={
		'titulo': 'Index',
		'bienvenido' : '' 

	}

	return '<h1>@willandru | Holamundo en Flask</h1>'

if __name__ == '__main__':
	app.run(debug=True, port=5000)