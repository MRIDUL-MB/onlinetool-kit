from flask import Flask, render_template, request
from flask import send_from_directory
from werkzeug.utils import secure_filename
from library.pdf_converter import text_pdf, file_pdf
from library.base import base_result, check
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        result = file_pdf(f.filename)
        return render_template('download.html')


@app.route('/download/pdf')
def pdf():
    text = request.args.get('text')
    result = text_pdf(text)
    return render_template("download.html")


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/base/result')
def base_output():
    number = request.args.get('number')
    num = list(number.upper())
    radix = int(request.args.get('radix'))
    convert = int(request.args.get('convert'))
    if check(num, radix):
        output = base_result(num, radix, convert)
        return render_template('base.html', output=output, number=number, radix=radix, convert=convert)
    else:
        message = "Check the number and base"
    return render_template('base.html', number=number, message=message, radix=radix, convert=convert)


if __name__ == '__main__':
    app.run(debug=True)
