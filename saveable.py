from databse import Database
class Saveable:

    def save(self):
        # print(self.to_dict())
        Database.insert(self.to_dict())
