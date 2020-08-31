#Class of a Rule from a regulation file. 
class Rule(object):
    def __init__(self, regulation_file_name, chapter_number, rule_number, text):
        self.PIC = []
        self.actions = []
        self.places = []
        self.time = []
        self.assets = []
        self.people = []
        self.things = []
        self.legal_doc = []
        self.company = []
        self.penalty = []
        self.investigation = []
        self.chapter_number = chapter_number
        self.rule_number = rule_number
        self.text = text
        #Name of the regulation file where the rule was found.
        self.regulation_file_name = regulation_file_name
#         self.parts_present = parts_present
#         self.note_present = note_present
#         def self.additional_input(self, self.note_present):
#             if self.note_present ==True:
#                 self.note = note_from end
#             else:
#                 self_note = None
    def fill_attributes(self, directory):
        self.actions = directory['Action']
        self.PIC = directory['Person In charge']
        self.people = directory['Person - General']
        self.things = directory['Object']
        self.company = directory['Company']
        self.penalty = directory['Penalty']
        self.investigation = directory['Investigation']
        self.legal_doc = directory['Legal Doc']
        self.time = directory['time']
        self.assets = directory['Assets']
        self.places = directory['Place']