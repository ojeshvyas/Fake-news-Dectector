import pickle

from flask import *

application = Flask(__name__)

global news


@application.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':
        global news
        news = request.form.get("upload")
        return redirect(url_for('uploads'))
    return render_template('index.html')


@application.route('/uploads', methods=['GET', 'POST'])
def uploads():
    data = detecting_fake_news(news)
    return render_template('result.html', data=data)


def detecting_fake_news(var):
    load_model = pickle.load(open('finalized_model.sav', 'rb'))
    prediction = load_model.predict([var])
    prob = load_model.predict_proba([var])

    return [prediction[0], prob[0][1]]



if __name__ == '__main__':
    application.run(debug=True)
