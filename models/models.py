from google.appengine.ext import ndb

# These classes define the data objects
# that you will be able to store in
# AppEngine's data store.

class Position(ndb.Model):
	x = ndb.IntegerProperty()
	y = ndb.IntegerProperty()

class Player(ndb.Model):
	name = ndb.StringProperty()
	username = ndb.StringProperty()
	color = ndb.StringProperty()
	position = ndb.KeyProperty(kind=Position, repeated=True)
	image_file = ndb.BlobKeyProperty()


