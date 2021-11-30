from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

filename = 'predict_risk_model.pkl'
model = pickle.load(open(filename, 'rb'))


@app.route('/')
def api_status():  # put application's code here
    print('Model loaded')
    return "Api Ativa"


@app.route('/api/predict_risk', methods=['POST'])
def predict_risk():
    content = request.json
    result = model.predict([[content['idade'], content['fumante'], content['obeso'], content['doenca_pulmonar'], content['nivel_sintomas']]])[0]
    return {
        "risk": int(result)
    }


@app.route('/api/hospitals', methods=['GET'])
def get_hospitals():
    return jsonify([
        {
            "id": 2,
            "name": 'Hospital - ITE',
            "coords": {
                "latitude": -22.325118,
                "longitude": -49.092425,
            }
        },
        {
            "id": 1,
            "name": 'UPA Jardim América',
            "coords": {
                 "latitude": -22.344876,
                 "longitude": -49.060491,
            }
        },
        {
            "id": 2,
            "name": 'Unidade de saúde terra branca',
            "coords": {
                  "latitude": -22.348687,
                  "longitude": -49.091489,
            }
        },
    ])


if __name__ == '__main__':
    app.run()
