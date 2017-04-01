from flask import Flask, json
from twitter import stream
app = Flask(__name__)

@app.route("/",methods=['GET'])
def run_twitter_stream():
    print "started"
    stream.filter(track=['flockos,@Flock_OS,@Flock'])


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000,debug=True)