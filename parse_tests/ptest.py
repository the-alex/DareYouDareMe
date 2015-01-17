import keys
import parse_rest
from parse_rest.connection import register
from parse_rest.datatypes import Object as ParseObject

register(keys.APPLICATION_ID, keys.REST_API_KEY, master_key=None)

print Object.Query.all()
