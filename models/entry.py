class Entry():
    # create an instance of the class by putting parenthesis after
    # __init__method define properties that every instance of the 
    # class will contain

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, mood_id, concept, entry, date):
        self.id = id
        self.mood_id = mood_id
        self.concept = concept
        self.entry = entry
        self.date = date