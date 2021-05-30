from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')
@app.route("/aboutme.html")
def aboutme():
    return render_template('aboutme.html')
@app.route("/gallery.html")
def gallery():
    return render_template('gallery.html')
@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route('/error_internal')
def error_internal():
    return render_template('template.html', name='ERROR 505'), 505
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
@app.route('/error_not_found')
def error_not_found():
    response = make_response(render_template('template.html', name='ERROR 404'), 404)
    response.headers['X-Something'] = 'A value'
    return response

if __name__ == '__main__':
    app.run(debug = True)