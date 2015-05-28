from step import Step

class Recipe():

    def __init__(self, steps=[]):
        self.steps = steps
        self.step_number = 0
        self.done = False

    def add_step(self,step):
        self.steps.append(step)

    def next_step(self):
        self.step_number += 1

        if self.step_number >= len(self.steps):
            self.done = True

    def previous_step(self):
        if self.step_number >= 1:
            stel.step_number -= 1

        # If someone says previous step at the very end
        self.done = False

    def get_current_instruction(self):
        return self.steps[self.step_number].instruction

    def get_current_duration(self):
        return self.steps[self.step_number].duration

    def ask_how_long(self):
        if len(self.get_current_duration()) > 0:
            return self.get_current_instruction() + " for " + self.get_current_duration()
        else:
            return self.get_current_instruction()

    def get_current_tools(self):
        return self.steps[self.step_number].tools

    def ask_amount(self,ingredient):

        for index in self._search_order():
            step = self.steps[index]
            if not step.get_ingredient(ingredient) == None:
                amount = step.get_ingredient(ingredient)
                break
        else: #no break, so ingredient was not found
            return "I don't know which ingredient you mean"

        if amount.isdigit():
            return 'You need ' + amount + ingredient
        else:
            return 'You need ' + amount + ' of ' + ingredient

    def ask_tools(self):
        tool_enumeration = ""
        for tool in self.get_current_tools():
            tool_enumeration += tool + 'and'

        #Remove last and
        tool_enumeration = tool_enumeration[:-3]

        return "For this step you need a " + tool_enumeration


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


    def _search_order(self):
        cur = self.step_number
        x = range(len(self.steps))

        order = x[cur:] + x[:cur]

        return order

cupcakes = Recipe()

step1 = Step(
    instruction="Throw everything into a bowl",
    ingredients={'flour': 'duzend gram', 'bread': '1 litre'},
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
