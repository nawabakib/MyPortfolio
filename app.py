from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_123'

# --- SAARE ROUTES YAHAN HAIN ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/guard')
def guard():
    return render_template('guard.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/single')
def single():
    return render_template('single.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()