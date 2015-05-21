class Step():

    def __init__(self, instruction="No instruction",ingredients={}, duration="", tools=[]):
        self.instruction = instruction
        self.ingredients = ingredients
        self.duration = duration

    def get_ingredient(self, what):
        if self.ingredients.has_key(what):
            return self.ingredients[what]
        return None;


Step()
