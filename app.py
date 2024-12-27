import flask
import flask_cors
from parser.back import GetRandomTHBase, GetRandomBHBase

app = flask.Flask(__name__)
flask_cors.CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@flask_cors.cross_origin()
def index():
  return flask.jsonify({"gaygaygay":"gaygaygaygay"})

@app.route('/th', methods = ["GET"])
@flask_cors.cross_origin()
def Th():
  lvl = flask.request.args.get("lvl", type=str)
  return flask.jsonify(f"{GetRandomTHBase(lvl)[1]}, {GetRandomTHBase(lvl)[2]}")


@app.route('/bh', methods = ["GET"])
@flask_cors.cross_origin()
def Bh():
  lvl = flask.request.args.get("lvl", type=str)
  return flask.jsonify(f"{GetRandomBHBase(lvl)[1]}, {GetRandomBHBase(lvl)[2]}")


if __name__ == "__main__":
  app.run(host="127.0.0.1")