import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

#create this folder structure, static/uploads
UPLOAD_FOLDER = './static/uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/hello')
def uploaded_file():
    
    uploaded_file = request.args['filename']
    image = '<img src="{0}" height="400" width="400"/>'.format('/static/uploads/' + uploaded_file)
    print request.args['filename']

    return image 

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # retrieving the file property from dict
        # the type is filestorage
        file = request.files['file']

        print "request.files", request.files
        print "accesssing the file property", file
        print "the filename of the file is", file.filename
        print "the upload folder is", app.config['UPLOAD_FOLDER']

        # checks that there is a file and the extension is allowed
        if file and allowed_file(file.filename):
            #file goes through security check and then saved in the provided path
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

