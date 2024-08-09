from flask import Flask, request, send_file, render_template
import os
import uuid
from main import pdf_to_word, translate_word, word_to_pdf  # Adjust import based on your setup

app = Flask(__name__)

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

    # Process the file
    pdf_to_word(pdf_path, docx_path)
    translate_word(docx_path, language)
    word_to_pdf(docx_path, output_pdf_path)

    # Clean up
    os.remove(pdf_path)
    os.remove(docx_path)

    return send_file(output_pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
