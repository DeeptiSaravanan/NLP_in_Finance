import datetime
#Regulation class.
class Regulation(object):
    def __init__(self, name, reg_dict):
        #reg_dict is a dictionary consisting of chapters dictionaries. 
        #Each chapter dictioanry has rule number as key and rule object as value.
        self.reg_dict = reg_dict
        self.name = name
        self.last_updated = datetime.time()
        