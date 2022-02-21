import os

import pandas as pd

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = os.path.join('repository')

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename))) 

      return read_file()


def read_file():
    filename = 'repository/total_sales.csv'
    data = pd.read_csv(filename, error_bad_lines=False, sep = ';', encoding="cp1252", header=0)
    myData = data.values
    return render_template('table.html', myData=myData)
		
if __name__ == '__main__':
   app.run(debug = True)