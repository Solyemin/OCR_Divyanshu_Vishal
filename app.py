from flask import Flask,render_template,request,url_for
from werkzeug.utils import secure_filename
from hashlib import md5
from os.path import join
from time import time
from PIL import Image

from segments import segment_img
# start flask app

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = './static/media/Input/'
#Flask route

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        FileObject = request.files['file']
        ch=request.form['fname']
        mimetype = FileObject.mimetype
        if mimetype == "image/jpeg" or mimetype == "image/png":
            img_name = secure_filename(md5(str(time()).encode()).hexdigest()+'.png')
            filename1 = join(app.config["UPLOAD_FOLDER"],img_name)
            FileObject=Image.open(FileObject)
            FileObject.save(filename1)
            filename=segment_img(filename1,img_name,ch)
            return render_template('index.html', filename=filename)
        else:
            return render_template('index.html',mimetype=mimetype) #for extra sequerty 
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8084, debug=True)
    # app.run(debug=True)