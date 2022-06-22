class classes:
    def __init__(self, name, credits, grades):
        self.name = name
        self.credits = credits
        self.grades = grades
        
    def get_name(self):
        return self.name
    def get_credits(self):
        return self.credits
    def get_grade(self):
        return self.grades
    
    
def calculate_gpa(list_of_classes):
    my_credits = 0
    total_credits = 0
    for grade in list_of_classes:
        total_credits += grade.credits
        my_credits += grade.credits * grade.grades
        
    return my_credits / total_credits
        

    