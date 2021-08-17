from fpdf import FPDF
import os
# from datetime import datetime as dt


def text_pdf(x):
    # now = dt.now()
    # date = str(dt.timestamp(now)).replace(".", "")
    # path = date + ".txt"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=18)
    with open('text.txt', 'w') as f:
        f.write(x)

    with open('text.txt', 'r') as f:
        for i in f:
            pdf.cell(200, 10, txt=i, ln=1)

    pdf.output('static/text.pdf')


def file_pdf(x):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=18)
    with open(x, 'r') as f:
        for i in f:
            pdf.cell(200, 10, txt=i, ln=1)

    pdf.output('static/text.pdf')
    os.remove(x)


if __name__ == "__main__":
    text_pdf()
