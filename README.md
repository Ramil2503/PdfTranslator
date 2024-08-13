# PDF Translator

This project allows you to translate text within PDF documents. The process involves converting a PDF to a Word document, translating the text while preserving formatting, and then converting it back to PDF.

## Prerequisites
1. **Python 3.8+**: Ensure you have Python 3.8 or higher installed on your machine.
2. **Git**: Required for cloning the repository. (Alternatively, you can download project as ZIP and skip "Clone the Repository" step.)

## Installation
1. Clone the Repository (or download as ZIP):
```bash
git clone https://github.com/Ramil2503/PdfTranslator
```

2. Open the terminal and navigate to the project folder
```bash
cd PdfTranslator
```

3. Create a Virtual Environment (Optional but recommended):

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**macOS and Linux:**
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

3. Stop the Flask Application

To stop the Flask application running in the terminal, press **Ctrl + C**.

## Managing the Virtual Environment
### Activating the Virtual Environment
**Windows**
```bash
venv\Scripts\activate
```
**macOS and Linux**
```bash
source venv/bin/activate
```
### Deactivating the Virtual Environment
**Windows, macOS, and Linux**
```bash
deactivate
```
