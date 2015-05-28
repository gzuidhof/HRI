import recipe

class Cookert():

    def __init__(self, recipe):
        self.recipe = recipe


    def cook(recipe):

        #Start sequence, say hello


        while recipe.done == False:
            #Capture intent
            intent = None

            if intent.type == 'navigation':
                self.on_navigation_intent(intent)
            elif intent.type == 'how_lan':
                self.on_how_long_intent()
            elif intent.type == 'how_much':
                self.on_how_much_intent(intent.ingredient)
            elif intent.type == 'what_tools':
                self.on_tools_intent()



    def on_navigation_intent(self, intent_type):
        if intent_type == 'repeat':
            self.say(self.recipe.get_current_instruction())
        elif intent_type == 'next':
            self.recipe.next_step()
            self.say(self.recipe.get_current_instruction())
        elif intent_type == 'previous':
            self.recipe.previous_step()
            self.say(self.recipe.get_current_instruction())

    def on_how_long_intent(self):
        self.say(self.recipe.ask_how_long())

    def on_how_much_intent(self, ingredient):
        self.say(self.recipe.ask_amount(ingredient))

    def on_tools_intent(self):
        self.say(self.recipe.ask_tools())

    def say(self, what):
        print what







if __name__ == '__main__':
    cupcake_recipe = recipe.cupcakes

    cook = Cookert(cupcake_recipe)
    cook.on_navigation_intent('repeat')
    cook.on_navigation_intent('next')
    cook.on_how_long_intent()
    cook.on_how_much_intent('flour')
    cook.on_tools_intent()
    #cook.on_how_long_intent()
    #cook.get_current_instruction()
