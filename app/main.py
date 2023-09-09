from flask import Flask, request, render_template
import pytesseract
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        file_bytes = file.read()
        image = Image.open(io.BytesIO(file_bytes))
        text = pytesseract.image_to_string(image, lang='eng+jpn')

        # 画像をBase64エンコード
        image_base64 = base64.b64encode(file_bytes).decode('utf-8')
        return render_template('index.html', text=text, image_base64=image_base64)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
