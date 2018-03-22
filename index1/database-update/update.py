from google.appengine.ext import ndb

class Update(ndb.Model):
    price = ndb.FloatProperty()
    time = ndb.DateTimeProperty()
    order = ndb.IntegerProperty()
