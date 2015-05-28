import recipe
import http_request_wit_ai

use_nao = False

if use_nao:
    import naoqi_speech
else:
    import speech_synthesis


class Cookert():

    def __init__(self, recipe):
        self.recipe = recipe


    def cook(recipe):

        response, product_name, intent, confidence = self.get_response()

        #Start sequence, say hello

        #while recipe.done == False:

        if confidence and confidence < 0.5:
            say("I don't know what you mean.")

        if intent == 'instruction_navigation':
            if 'relative_instruction_navigation' in response:
                self.on_navigation_intent(response['relative_instruction_navigation'])
            else:
                print '?!?!?'
        elif intent == 'check_duration':
            self.on_how_long_intent()
        elif intent == 'check_amount':
            self.on_how_much_intent(product_name)
        elif intent == 'what_tools': #Doesn't exist yet
            self.on_tools_intent()


    def get_response(self):
        response = http_request_wit_ai.get_wit_response()
        if not response:
            return

        if "product" in response:
            product_name = str(response["product"])
            print "product: " + product_name

        if "intent" in response:
            intent = str(response["intent"])
            print "intent: " + intent

        if "confidence" in response:
            confidence = float(response["confidence"])
            print "confidence: " + str(confidence

        return response, product_name, intent, confidence

    def on_navigation_intent(self, relative):
        if relative == 'current':
            self.say(self.recipe.get_current_instruction())
        elif relative == 'next':
            self.recipe.next_step()
            self.say(self.recipe.get_current_instruction())
        elif relative == 'previous':
            self.recipe.previous_step()
            self.say(self.recipe.get_current_instruction())
        elif relative == 'unknown':
            self.say('Unknown relative instruction navigation')

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

    cookert = Cookert(cupcake_recipe)
    cookert.cook()
    #cook.on_navigation_intent('repeat')
    #cook.on_navigation_intent('next')
    #cook.on_how_long_intent()
    #cook.on_how_much_intent('flour')
    #cook.on_tools_intent()
