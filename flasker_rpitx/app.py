from flask import Flask
import shlex
import subprocess

app = Flask(__name__)

process_run = None

@app.route("/")
def hello_world():
    global process_run
    if process_run is not None:
        poll = process_run.poll()
        if poll is None:
            return "<p>Running</p>"

    process_run = subprocess.Popen(shlex.split('sudo /home/pi/rpitx/sendiq -s 250000 -f 433.92e6 -t u8 -i /home/pi/rpitx/record.iq'))
    return "<p>Triggered!</p>"
