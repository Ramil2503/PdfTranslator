from flask import Flask, request, send_file, render_template, jsonify, url_for
from flask_socketio import SocketIO, emit
import os
import uuid
from main import pdf_to_word, translate_word, word_to_pdf

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or 'language' not in request.form:
        return "No file or language selected", 400

    file = request.files['file']
    language = request.form['language']
    if file.filename == '':
        return "No file selected", 400

    # Generate unique filenames
    pdf_filename = f"{uuid.uuid4().hex}.pdf"
    docx_filename = f"{uuid.uuid4().hex}.docx"
    output_pdf_filename = f"{uuid.uuid4().hex}_translated.pdf"

    pdf_path = os.path.join(UPLOAD_FOLDER, pdf_filename)
    docx_path = os.path.join(UPLOAD_FOLDER, docx_filename)
    output_pdf_path = os.path.join(OUTPUT_FOLDER, output_pdf_filename)

    # Save the uploaded file
    file.save(pdf_path)

    def update_progress(progress, text):
        print(f"Progress: {progress * 100}% - {text}")  # Debug print statement
        socketio.emit('progress', {'progress': progress * 100, 'text': text})
        
    # Process the file
    update_progress(0, 'Reading PDF file...')
    pdf_to_word(pdf_path, docx_path)

    # Start processing and updating progress
    update_progress(0, 'Starting translation...')
    translate_word(docx_path, language, progress_callback=update_progress)
    
    update_progress(100, 'Translation complete. Preparing PDF...')
    word_to_pdf(docx_path, output_pdf_path)
    update_progress(100, 'Completed')

    # Clean up
    os.remove(pdf_path)
    os.remove(docx_path)

    # Provide the URL for the download
    return jsonify({'download_url': url_for('download_file', filename=output_pdf_filename)})

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(OUTPUT_FOLDER, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found", 404

if __name__ == '__main__':
    socketio.run(app, debug=True)
