from mongoengine import *
from config import Config
from bson.objectid import ObjectId
import datetime

connect('toyoya', host=Config.db_host)

class Problem(Document):
    problem_level = StringField()
    title = StringField()
    message = StringField()
    create_date = DateTimeField(default=datetime.datetime.now)