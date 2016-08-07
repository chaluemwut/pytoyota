from mongoengine import *
from config import Config
from bson.objectid import ObjectId
import datetime, os

connect('toyoya', host=os.environ['TOYOTA_DB_1_PORT_27017_TCP_ADDR'])

class Problem(Document):
    problem_level = StringField()
    title = StringField()
    message = StringField()
    create_date = DateTimeField(default=datetime.datetime.now)

print('***** test db')
p = Problem.objects
print(p)