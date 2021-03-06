from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
	def get(self):
	    return "Hello, I love Digital Ocean!"

api.add_resource(Hello, '/')
if __name__ == "__main__":
    app.run()