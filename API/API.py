from flask import Flask
from flask_restful import Api, Resource
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

# Wenn MySql-Datenbank aufgesetzt ist

mydb= mysql.connector.connect(
    host="192.168.178.23",
    user="admin",
    password="root",
    database="Plants",
    autocommit= True,
    )

mycursor = mydb.cursor()

class PlantData(Resource):
    def get(self):
        mycursor.execute("SELECT * FROM classroom")
        result = mycursor.fetchall()
        return {"data":result}
        #return {"data": "123456789"}

api.add_resource(PlantData, "/api/getPlantData")

if __name__ == "__main__":

    app.run(host="192.168.178.23",debug=True)
    
