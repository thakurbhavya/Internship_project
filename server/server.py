from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hi this is a test API"


@app.route('/convert_image')

def convert_image():
   
    request_data = request.get_json()
    image_data = request_data['image_data']
    

    
    class_label = util.convert_image(image_data)

   
    response = {'class_label': class_label}

   
    return jsonify(response), 200, #response_headers

if __name__ == "__main__":
    print("Starting Python Flask Server For Image to String Converter")
    util.load_saved_artifacts()
    app.run(port=5000)

