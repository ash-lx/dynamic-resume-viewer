from flask import Flask, request, render_template, send_file, jsonify, send_from_directory
from generate_resume import generate_resume
import os
import json

app = Flask(__name__)

# Ensure the uploads directory exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Get resume data from request
        resume_data = request.json

        # Generate file paths
        docx_path = os.path.join(UPLOAD_FOLDER, 'resume.docx')
        pdf_path = os.path.join(UPLOAD_FOLDER, 'resume.pdf')

        # Generate the resume
        success = generate_resume(resume_data, docx_path, pdf_path)

        if success:
            return jsonify({
                'status': 'success',
                'message': 'Resume generated successfully',
                'docx_path': docx_path,
                'pdf_path': pdf_path
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Failed to generate resume'
            }), 500

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/download/<filetype>')
def download(filetype):
    try:
        if filetype == 'docx':
            path = os.path.join(UPLOAD_FOLDER, 'resume.docx')
            mimetype = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        elif filetype == 'pdf':
            path = os.path.join(UPLOAD_FOLDER, 'resume.pdf')
            mimetype = 'application/pdf'
        else:
            return jsonify({
                'status': 'error',
                'message': 'Invalid file type'
            }), 400

        return send_file(path, mimetype=mimetype, as_attachment=True)
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/preview/<filetype>')
def preview(filetype):
    try:
        if filetype == 'docx':
            path = os.path.join(UPLOAD_FOLDER, 'resume.docx')
            mimetype = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        elif filetype == 'pdf':
            path = os.path.join(UPLOAD_FOLDER, 'resume.pdf')
            mimetype = 'application/pdf'
        else:
            return jsonify({
                'status': 'error',
                'message': 'Invalid file type'
            }), 400

        return send_file(path, mimetype=mimetype)
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True)
