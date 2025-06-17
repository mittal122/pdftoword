from flask import Flask, request, render_template, send_file, jsonify
import os
import tempfile
from werkzeug.utils import secure_filename
from pdf2docx import Converter
import threading
import time

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def cleanup_file(filepath, delay=300):
    """Delete file after delay (5 minutes by default)"""
    def delete_file():
        time.sleep(delay)
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
                print(f"Cleaned up: {filepath}")
        except Exception as e:
            print(f"Error cleaning up {filepath}: {e}")
    
    thread = threading.Thread(target=delete_file)
    thread.daemon = True
    thread.start()

def allowed_file(filename):
    """Check if file is a PDF"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'pdf'

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_pdf():
    """Handle PDF to DOCX conversion"""
    try:
        # Check if file was uploaded
        if 'file' not in request.files:
            return 'No file uploaded', 400
        
        file = request.files['file']
        
        if file.filename == '':
            return 'No file selected', 400
        
        if not allowed_file(file.filename):
            return 'Invalid file type. Please upload a PDF file.', 400
        
        # Generate secure filename
        filename = secure_filename(file.filename)
        
        # Create temporary files
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as pdf_temp:
            pdf_path = pdf_temp.name
            file.save(pdf_path)
        
        # Generate output filename
        docx_filename = filename.rsplit('.', 1)[0] + '.docx'
        with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as docx_temp:
            docx_path = docx_temp.name
        
        # Convert PDF to DOCX
        try:
            cv = Converter(pdf_path)
            cv.convert(docx_path, start=0, end=None)
            cv.close()
        except Exception as e:
            # Clean up temp files
            if os.path.exists(pdf_path):
                os.remove(pdf_path)
            if os.path.exists(docx_path):
                os.remove(docx_path)
            return f'Conversion failed: {str(e)}', 500
        
        # Schedule cleanup of temp files
        cleanup_file(pdf_path)
        cleanup_file(docx_path)
        
        # Send the converted file
        return send_file(
            docx_path,
            as_attachment=True,
            download_name=docx_filename,
            mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        
    except Exception as e:
        return f'Server error: {str(e)}', 500

@app.errorhandler(413)
def too_large(e):
    """Handle file too large error"""
    return 'File too large. Maximum size is 16MB.', 413

if __name__ == '__main__':
    # Set max content length
    app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
    
    # Run the app
    print("🚀 PTOD File server starting...")
    print("📍 Access the app at: http://localhost:5000")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        threaded=True
    )
