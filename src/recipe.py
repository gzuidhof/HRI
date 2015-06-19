from step import Step

class Recipe():
    """
        Data structure for recipes, contains a bunch of steps and keeps track
        of where in the process the user is.
    """
    def __init__(self, steps=[], name='this'):
        self.steps = steps
        self.step_number = 0
        self.done = False
        self.name = name

    def add_step(self,step):
        self.steps.append(step)

    def next_step(self):
        self.step_number += 1

        if self.step_number >= len(self.steps):
            self.done = True

    def previous_step(self):
        if self.step_number >= 1:
            self.step_number -= 1

        # If someone says previous step at the very end
        self.done = False

    def get_current_instruction(self):
        return self.steps[self.step_number].instruction

    def get_current_duration(self):
        return self.steps[self.step_number].duration

    # "How long do I ...?"
    def ask_how_long(self):
        if len(self.get_current_duration()) > 0:
            return self.get_current_instruction() + " for " + self.get_current_duration()
        else:
            return self.get_current_instruction()

    def get_current_tools(self):
        return self.steps[self.step_number].tools


    # "How much of X do I need?"
    def ask_amount(self,ingredient):

        for index in self._search_order():
            step = self.steps[index]
            if not step.get_ingredient(ingredient) == None:
                amount = step.get_ingredient(ingredient)
                break
        else: #no break, so ingredient was not found
            return "I don't know which ingredient you mean"

        #Construct sentence
        if amount.isdigit(): #You need 3 eggs
            return 'You need ' + amount + ingredient
        else: #You need 200 grams of flour
            return 'You need ' + amount + ' of ' + ingredient

    # "What tools do I need (for this step)?"
    def ask_tools(self):
        tool_enumeration = ""
        for tool in self.get_current_tools():
            tool_enumeration += tool + 'and'

        #Remove last and
        tool_enumeration = tool_enumeration[:-3]

        return "For this step you need a " + tool_enumeration

    # "What ingredients do I need?"
    def ask_ingredients(self):
        ingredients = self.get_all_ingredients

        #Construct a sentence
        sentence = "To make " + self.name + " you need "
        n = len(ingredients)

        for i, ingredient in ingredients:
            if i == n and not i == 0:
                sentence += "and " + ingredient
            else:
                if i==0:
                    sentence += ingredient
                else:
                    sentence += ", " + ingredient

        return sentence


    def get_all_tools(self):
        tools = []

        for step in self.steps:
            for tool in step.tools:
                tools.append(tool)

        return tools

    def get_all_ingredients(self):
        ingredients = {}

        for step in self.steps:
            for ingr in step.ingredients:
                amount = step.ingredients[ingr]
                ingredients[ingr] = amount

        return ingredients

    #Used for searching amount required of ingredient
    #Starts from current step
    def _search_order(self):
        cur = self.step_number
        x = range(len(self.steps))

        order = x[cur:] + x[:cur]

        return order


## Cupcake recipe definition

cupcakes = Recipe()

step1 = Step(
    instruction="Throw the flour, water and egg into a bowl",
    ingredients={'flour': '1000 grams', 'water': '1 litre', 'egg': '1'},
    duration='',
    tools=['bowl']
)

step2 = Step(
    instruction="Mix it all together using your wisk",
    ingredients={},
    duration='5 minutes',
    tools=['wisk']
)

step3 = Step(
    instruction="Pour it into the shapes",
    ingredients={},
    duration='',
    tools=['baking shapes']
)

step4 = Step(
    instruction="Put it in the oven",
    ingredients={},
    duration='8 minutes',
    tools=['oven']
)

cupcakes.add_step(step1)
cupcakes.add_step(step2)
cupcakes.add_step(step3)
cupcakes.add_step(step4)
