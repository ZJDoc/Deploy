# -*- coding: utf-8 -*-

"""
@date: 2024/11/9 下午9:25
@file: app.py
@author: zj
@description: 
"""

from flask import Flask, request, send_from_directory
import os
import argparse

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return f"File {filename} has been uploaded."


@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the Flask file server.")
    parser.add_argument('--port', type=int, default=5000, help="Port to run the server on (default: 5000)")
    parser.add_argument('--debug', action='store_true', help="Run the server in debug mode")
    args = parser.parse_args()

    app.run(port=args.port, debug=args.debug)
