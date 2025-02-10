# Dynamic Resume Viewer

A web application that generates professional resumes in both DOCX and PDF formats from JSON data, with built-in preview functionality.

## Features

- **JSON-based Resume Generation**: Create resumes by providing structured data in JSON format
- **Multiple Format Support**: Generate resumes in both DOCX and PDF formats
- **Live Preview**: Preview generated resumes directly in the browser
  - DOCX preview with HTML conversion
  - PDF preview with built-in PDF viewer
- **Sample Data**: Includes sample resume data for quick testing
- **Responsive Design**: Modern, mobile-friendly user interface
- **Real-time Error Handling**: Immediate feedback on any issues during generation

## Prerequisites

- Python 3.6 or higher
- Flask web framework
- python-docx for DOCX file generation
- Additional Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd dynamic-resume-viewer
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. You can either:
   - Click "Load Sample Data" to use the provided example
   - Paste your own JSON resume data in the text area

4. Click "Generate Resume" to create your resume

5. After generation, you can:
   - Download the resume in DOCX or PDF format
   - Preview either format directly in the browser
   - Switch between DOCX and PDF previews

## JSON Format

Your resume data should follow this structure:
```json
{
  "name": "Jane Doe",
  "contact": {
    "phone": "(555) 123-4567",
    "email": "jane.doe@example.com",
    "linkedin": "linkedin.com/in/janedoe",
    "location": "Anytown, USA"
  },
  "summary": "A highly adaptable professional...",
  "skills": [
    "Skill 1",
    "Skill 2"
  ],
  "experience": [
    {
      "title": "Job Title",
      "company": "Company Name",
      "dates": "2020 - Present",
      "responsibilities": [
        "Responsibility 1",
        "Responsibility 2"
      ]
    }
  ],
  "education": [
    {
      "institution": "University Name",
      "degree": "Degree Name",
      "dates": "2016 - 2020",
      "gpa": "3.8"
    }
  ]
}
```

## Technologies Used

- **Backend**:
  - Flask (Python web framework)
  - python-docx (DOCX generation)
  - PyPDF2 (PDF generation)

- **Frontend**:
  - HTML5/CSS3
  - JavaScript (ES6+)
  - Tailwind CSS (styling)
  - PDF.js (PDF preview)
  - Mammoth.js (DOCX preview)

## Error Handling

The application includes comprehensive error handling for:
- Invalid JSON data
- File generation issues
- Preview rendering problems
- Server communication errors

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
