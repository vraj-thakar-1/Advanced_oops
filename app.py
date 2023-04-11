from admin import Admin
from databse import Database

a = Admin('raj', "1234", 3)
a.save()
print(Database.find(lambda x: x['username'] == 'raj'))
