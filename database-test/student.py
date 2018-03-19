from google.appengine.ext import ndb

class Student(ndb.Model):
    name = ndb.StringProperty()
    university = ndb.StringProperty()
    birthday = ndb.DateProperty()
