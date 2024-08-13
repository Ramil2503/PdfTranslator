# PDF Translator

This project allows you to translate text within PDF documents. The process involves converting a PDF to a Word document, translating the text while preserving formatting, and then converting it back to PDF.

## Prerequisites
1. **Python 3.8+**: Ensure you have Python 3.8 or higher installed on your machine.
2. **Git**: Required for cloning the repository.

## Installation
1. Clone the Repository:
```bash
git clone https://github.com/Ramil2503/PdfTranslator
cd PdfTranslator
```

2. Create a Virtual Environment (Optional but recommended):

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```
**macOS**
```bash
python -m venv venv
source venv/bin/activate
```
### Install Dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application
1. Start the Flask Application:

```bash
python app.py
```
The application will be accessible at http://127.0.0.1:5000/.

2. Using the Application:

* Open your web browser and navigate to the application URL.
* Upload a PDF file and select the target language for translation.
* Download the translated PDF once the process is complete.