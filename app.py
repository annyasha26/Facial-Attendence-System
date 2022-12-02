from flask import Flask, render_template
from flask_socketio import SocketIO
from main import attendence_process
from handle_sheet_index import update_col_index, get_current_index




app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app,cross_allowed_origin="*")


@socketio.on("my event")
def handle(data):
    print("tested",data)

@socketio.on("message")
def handle(data):
    print("message",data)
    col_idx = get_current_index(data.get("params").get("subject"),data.get("params").get("section"))
    attendence_process(data.get("instruct"),data.get("params").get("section"),data.get("params").get("subject"),col_idx)
   


@app.route("/")
def home():
    return render_template("home.html")


if __name__=="__main":
    socketio.run(app)
