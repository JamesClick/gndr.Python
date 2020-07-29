class identifyGender:

    def __init__(self, gender: str=None, pronouns: list=None):
        self.gender, self.pronouns = gender, pronouns

    def set(self, gender: str=None, pronouns: list=None):
        if gender != None:
            self.gender = gender
        
        if pronouns != None:
            self.pronouns = pronouns
        
        return [
            self.gender,
            self.pronouns
        ]
    
    def get(self):
        return [
            self.gender,
            self.pronouns
        ]
