#https://stackoverflow.com/questions/56579394/run-rasa-with-flask

from flask import Flask
from flask.json import jsonify
from flask_cors import CORS
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.utils.endpoints import EndpointConfig
from flask import request
app = Flask(__name__)
CORS(app)


def rasa_agent():
    # interpreter = RasaNLUInterpreter("/Users/mirfan/PycharmProjects/rasa-faq-bot/models/nlu-20200324-152315/nlu")
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    # agent = Agent.load("/Users/mirfan/PycharmProjects/rasa-faq-bot/models/core-20200324-152613/core", interpreter=interpreter, action_endpoint=action_endpoint)
    # agent = Agent.load("/Users/mirfan/PycharmProjects/rasa-faq-bot/models/core-20200324-152613/core", action_endpoint=action_endpoint)
    agent = Agent.load("models/20200324-192130.tar.gz", action_endpoint=action_endpoint, generator=action_endpoint)
    return agent


@app.route("/", methods=['POST'])
def evaluate():
    agent = rasa_agent()
    print(request.json["message"])
    reply = agent.handle_text(request.json["message"])
    print(reply)
    output = {"reply": reply}
    return output


if __name__ == '__main__':
    app.run(debug=False)
