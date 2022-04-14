class Entry():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, mood_id, concept, entry, date):
        self.id = id
        self.mood_id = mood_id
        self.concept = concept
        self.entry = entry
        self.date = date