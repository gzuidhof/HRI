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
            return self.get_current_instruction() + " for however long you want!"

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
            tool_enumeration += tool + ' and '

        #Remove last and
        tool_enumeration = tool_enumeration[:-5]

        return "For this step you need a " + tool_enumeration

    # "What ingredients do I need?"
    def ask_ingredients(self):
        ingredients = self.get_all_ingredients()

        #Construct a sentence
        sentence = "To make " + self.name + " you need "
        n = len(ingredients)

        for i, ingredient in enumerate(ingredients):
            if i == n-1 and not i == 0:
                sentence += " and " + ingredient
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

step_o = Step(
    instruction="Preheat the oven to 180 degrees centigrade",
    ingredients={},
    duration='',
    tools=['oven']
)

step_a = Step(
    instruction="Put the flour into a bowl",
    ingredients={'flour': 'the whole package'},
    duration='',
    tools=['bowl']
)

step_b = Step(
    instruction="Add the eggs, water and butter",
    ingredients={'eggs': '2', "water": "50 mililitres", "butter": "125 grams"},
    duration='',
    tools=['bowl']
)

step_c = Step(
    instruction="Mix it together using the lowest setting on the mixer until homogenous",
    ingredients={},
    duration='',
    tools=['mixer', 'bowl']
)

step_d = Step(
    instruction="Beat the mixture until it's fluffy.",
    ingredients={},
    duration='1 minute',
    tools=['wisk', 'bowl']
)

step_e = Step(
    instruction="Put the baking shapes on the baking tray",
    ingredients={},
    duration='',
    tools=['baking shapes', 'spoon', 'baking tray']
)

step_f = Step(
    instruction="Put the dough into the baking shapes with a spoon",
    ingredients={},
    duration='',
    tools=['baking shapes', 'spoon']
)

step_g = Step(
    instruction="Put the baking shapes into the oven",
    ingredients={},
    duration='16 minutes',
    tools=['oven']
)

better_cupcakes = Recipe(name = "BetterCupcakes")
better_cupcakes.add_step(step_o)
better_cupcakes.add_step(step_a)
better_cupcakes.add_step(step_b)
better_cupcakes.add_step(step_c)
better_cupcakes.add_step(step_d)
better_cupcakes.add_step(step_e)
better_cupcakes.add_step(step_f)
better_cupcakes.add_step(step_g)