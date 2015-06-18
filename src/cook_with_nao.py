import recipe
import http_request_wit_ai
import time
from microphone_loudness import TapTester

use_nao = False

if use_nao:
    import naoqi_speech
else:
    import speech_synthesis


class Cookert():

    def __init__(self, recipe):
        self.recipe = recipe



    def cook(self):
        #Create noise listener
        listener = TapTester()

        while self.recipe.done == False:
            listener.listen_until_noise()
            self.listen_and_answer()
            time.sleep(3) #Sleep 3 seconds as Nao talks


    #Listen to actual question and answer
    def listen_and_answer(self):
        resp = self.get_response()

    def answer(self, resp):
        if resp:
            response, product_name, intent, confidence = resp
        else:
            return

        #Start sequence, say hello

        #while recipe.done == False:

        if confidence and confidence < 0.5:
            self.say("I don't know what you mean.")
            return

        if intent == 'instruction_navigation':
            if 'relative_instruction_navigation' in response:
                self.on_navigation_intent(response['relative_instruction_navigation'])
            else:
                print 'askdfjasdfj'
        elif intent == 'check_duration':
            self.on_how_long_intent()
        elif intent == 'check_amount':
            self.on_how_much_intent(product_name)
        elif intent == 'what_tools': #Doesn't exist yet
            self.on_tools_intent()


    def get_response(self):
        response = http_request_wit_ai.get_wit_response()
        product_name = None
        intent = None
        confidence = None
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
            print "confidence: " + str(confidence)

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
