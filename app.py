# coding: utf-8
from flask import Flask, request
from flask_cors import CORS
import sys, os, json
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

#Config pour que notre api accept les fichiers
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'html'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Petit donction pour check l'extention de nos fichiers
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello_world():
    return 'Hello World!'

#path pour récuperer notre fichier
@app.route('/form',methods = ['POST'])
def form():
    print("test", file=sys.stdout)
    if request.method == 'POST':
        # Verifier si le post a bien un fichier
        if 'file' not in request.files:
            print('No file part')
            return "No File"
        file = request.files['file']
        # Autre check si le fichier exist bien, propre a certains navigateur
        if file.filename == '':
            print('No selected file')
            return "False"
        # Si notre fichier existe et qu'il a bien l'extension attendu
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            #quelques lignes pour lire notre fichier
            f = open(UPLOAD_FOLDER+"/"+file.filename, "r")
            print(f.read(), file=sys.stdout)

            return "Ici return le json avec les details du calcul"
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
