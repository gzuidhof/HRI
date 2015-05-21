from step import Step

class Recipe():

    def __init__(self, steps=[]):
        self.steps = steps
        self.step_number = 0

    def add_step(self,step):
        self.steps.append(step)

    def ask_amount(self,ingredient):

        for index in self._search_order():
            step = self.steps[index]
            if not step.get_ingredient(ingredient) == None:
                amount = step.get_ingredient(ingredient)
                break
        else: #no break, so ingredient was not found
            return "I don't know which ingredient you mean"

        return 'You need ' + amount + ' of ' + ingredient

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

print cupcakes.ask_amount('bread')
