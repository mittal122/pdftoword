# PTOD File - PDF to Word Converter

A modern, dark-themed web application that converts PDF files to Word (DOCX) format with a clean and intuitive user interface.

![PTOD File Screenshot](https://via.placeholder.com/800x450.png?text=PTOD+File+PDF+to+Word+Converter)

## Features

- **Modern Dark Theme UI**: Sleek design with responsive layout
- **Drag & Drop Interface**: Easy file uploading with drag-and-drop support
- **Real-time Feedback**: Progress indicators and status messages
- **Secure Processing**: Files are processed securely and deleted after conversion
- **Mobile Friendly**: Works on all devices with responsive design
- **No Registration Required**: Free to use without any sign-up

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python Flask
- **Conversion Engine**: pdf2docx library
- **Containerization**: Docker

## Installation

### Option 1: Using Docker (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mittal122/pdftoword.git
   cd pdftoword
   ```

2. **Build Docker image:**
   ```bash
   docker build -t pdftoword:latest .
   ```

3. **Run the container:**
   ```bash
   docker run -p 5000:5000 pdftoword:latest
   ```

4. **Access the application:**
   - Open your browser and go to: `http://localhost:5000`

### Option 2: Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mittal122/pdftoword.git
   cd pdftoword
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   - Open your browser and go to: `http://localhost:5000`

## Usage

1. **Upload PDF**: Click on the upload area or drag and drop a PDF file
2. **Convert**: Click the "Convert to Word" button
3. **Download**: Once conversion is complete, click "Download DOCX File"

## Project Structure

```
pdftoword/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── static/                 # Static assets
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   └── js/
│       └── script.js       # Frontend JavaScript
├── templates/
│   └── index.html          # Main HTML template
└── uploads/                # Temporary upload directory (created at runtime)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [pdf2docx](https://github.com/dothinking/pdf2docx) - PDF to DOCX conversion library
- [Flask](https://flask.palletsprojects.com/) - Web framework for Python
- [Docker](https://www.docker.com/) - Containerization platform

---

Created by [mittal122](https://github.com/mittal122) - Feel free to contact me!
