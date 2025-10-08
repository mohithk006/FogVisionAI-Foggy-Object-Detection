from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
from ultralytics import YOLO
import os
import cv2
from werkzeug.utils import secure_filename

# Initialize the Flask app

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong secret key

# Folder for uploaded images and detection results
UPLOAD_FOLDER = 'uploads'
RESULTS_FOLDER = 'results'

# Create directories if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULTS_FOLDER'] = RESULTS_FOLDER

# Load the YOLO model
model = YOLO('best.pt')  # Path to your trained YOLO weights

users = {'admin': 'admin'}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username  
            return redirect(url_for('index'))
        else:
            return "Login failed. Please check your username and password."

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username not in users:
            users[username] = password
            return redirect(url_for('login'))
        else:
            return "Registration failed. User already exists."

    return render_template('register.html')

@app.route('/index')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

# @app.route('/')
# def home():
#     return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('home'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('home'))

    if file:
        # Save the uploaded file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Perform object detection
        results = model(file_path)

        # Save the annotated image
        result_img_path = os.path.join(app.config['RESULTS_FOLDER'], f"result_{filename}")
        annotated_frame = results[0].plot()  # Annotate the image
        cv2.imwrite(result_img_path, annotated_frame)

        # Render result.html with paths to the original and detected images
        return render_template('result.html',
                               original_file=f'uploads/{filename}',
                               result_file=f'results/result_{filename}')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/results/<filename>')
def result_file(filename):
    return send_from_directory(app.config['RESULTS_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
