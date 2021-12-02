from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://${{ secrets.USER_DATABASE }}:${{ secrets.PASS_DATABASE }}@${{ secrets.HOST_DATABASE }}:${{ secrets.PORT_DATABASE }}/flaskmysql'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)

from models import Client

@application.route("/")
def root():
    return "This is the app index"

#Get all clients
@application.route("/getall")
def get_all():
    try:
        clients=Client.query.all()
        return  jsonify([e.serialize() for e in clients])
    except Exception as e:
        return(str(e))

#--------Main------------------
if __name__ == "__main__":
    application.debug = True
    application.run()
#------------------------------


