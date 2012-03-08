#!/usr/bin/python

'''Contains the phrase classes. These are nearly identical, and could be
integrated into one class, but for organizational purposes won't'''

class Inphrase:
    def __init__(self, type, content, question = "", action = ""):
        self.type = type.lower()
        self.content = content
        self.action = action
        self.question = question
        
        if type.lower() == "query":
            if question != "":
                pass
            else:
                print("ERROR") #XXX: Yes, I should be throwing an exception here.
                
        elif type.lower() == "statement":
            if action != '':
                pass
            else:
                print("ERROR") #XXX: And throwing an exception here, as well
                
    def toXML(self):
        return '<inphrase type="' + self.type + '" question="' + self.question + '" action="' + self.action + '">' + self.content + '</inphrase>'
                
        

class Outphrase:
    def __init__(self, type, content, question = "", action = ""):
        self.type = type.lower()
        self.content = content
        self.question = question
        self.action = action
        
        if type.lower() == "query":
            if question != "":
                pass
            else:
                print("ERROR") #XXX: Yes, I should be throwing an exception here.
                
        elif type.lower() == "statement":
            if action != '':
                pass
            else:
                print("ERROR") #XXX: And throwing an exception here, as well
                
    def toXML(self):
        return '<outphrase type="' + self.type + '" question="' + self.question +'" action="' + self.action + '">' + self.content + '</outphrase>'