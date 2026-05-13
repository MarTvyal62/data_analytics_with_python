def age_group_label(age, minor_threshold=30, senior_threshold=60):
    if age < minor_threshold:
        return "Minor"
    elif age < senior_threshold - 1:
        return "Middle-aged"
    else:
        return "Senior"


def income_band(income, low=80000, high=170000):
    if income < low:
        return "Low"
    elif income <= high:
        return "Medium"
    else:
        return "High"
    

def get_dependant_category(n_dependants):
    if n_dependants == 0:
        return "No dependants"
    elif n_dependants <= 2:
        return "Small family"
    else:
        return "Large family"
    
def set_senior_flag(age):
        return 'Senior' if age >= 60 else 'Non-Senior'
    
