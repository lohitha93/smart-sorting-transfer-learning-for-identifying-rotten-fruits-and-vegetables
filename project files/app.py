import os
from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

classes = ['Fresh Apple', 'Fresh Banana', 'Fresh Orange', 'Rotten Apple', 'Rotten Banana', 'Rotten Orange']


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/blog/<slug>")
def blog_single(slug):
    return render_template("blog-single.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio-details.html")


@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'static', 'uploads')
    if not os.path.isdir(target):
        os.makedirs(target)

    for upload_file in request.files.getlist("file"):
        filename = upload_file.filename
        destination = os.path.join(target, filename)
        upload_file.save(destination)

        import numpy as np
        from keras.preprocessing import image
        from keras.models import load_model

        new_model = load_model('healthy_vs_rotten.h5')
        test_image = image.load_img(destination, target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = new_model.predict(test_image)
        result1 = result[0]

        for i in range(6):
            if result1[i] == 1.:
                break
        prediction = classes[i]

    return render_template("template.html", image_name=filename, text=prediction)


@app.route('/static/uploads/<filename>')
def send_image(filename):
    return send_from_directory(os.path.join('static', 'uploads'), filename)


if __name__ == "__main__":
    app.run(debug=False)
