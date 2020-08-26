import os
import io

from flask import Flask,request,redirect,url_for,flash,request,render_template
from werkzeug.utils import secure_filename
from Bio import SeqIO
from Bio.Seq import Seq

ALLOWED_EXTENSIONS = ['fasta']

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/',methods=['GET', 'POST'])
def translate_dna_submission():

    if request.method == 'POST':
        file = request.files['file']
        input_sequence = request.form.get('sequence')

        if file and allowed_file(file.filename):
            fasta_string = file.read().decode('utf-8')
            record = SeqIO.read(io.StringIO(fasta_string),'fasta')
            protein_seq = record.translate().seq

        elif input_sequence:
            protein_seq = Seq(input_sequence).translate()

        else:
            flash("A fasta file or sequence must be submitted.")
            return redirect(request.url)

        return render_template('index.html',protein=protein_seq)

    return render_template('index.html',protein=None)

def allowed_file(filename):
    return  '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



