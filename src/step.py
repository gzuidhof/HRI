class Step():
    """
        One step in a recipe.
        Contains an instruction, and optionally contains ingredients, a duration
        and a list of tools
    """
    def __init__(self, instruction="No instruction",ingredients={}, duration="", tools=[]):
        self.instruction = instruction
        self.ingredients = ingredients
        self.duration = duration
        self.tools = tools

    def get_ingredient(self, what):
        if self.ingredients.has_key(what):
            return self.ingredients[what]
        return None
