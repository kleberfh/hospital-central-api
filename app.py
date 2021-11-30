from flask import Flask, request
import pickle

app = Flask(__name__)

filename = 'predict_risk_model.pkl'
model = pickle.load(open(filename, 'rb'))


@app.route('/')
def predict_risk():  # put application's code here
    print('Model loaded')
    return "Api Ativa"


@app.route('/api/get_user_risk', methods=['POST'])
def get_user_risk():
    content = request.json
    result = model.predict([[content['idade'], content['fumante'], content['obeso'], content['doenca_pulmonar'], content['nivel_sintomas']]])[0]
    print(result)
    return {
        "risk": int(result)
    }


if __name__ == '__main__':
    app.run()
