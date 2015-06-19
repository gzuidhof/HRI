import recipe
from facetracker import tracker
import eye_leds
from microphone_loudness import NoiseListener

use_nao = True
use_wit = True

if use_nao:
    import naoqi_speech as speech
else:
    import speech_synthesis as speech

if use_wit:
    import http_request_wit_ai


class Cookert():

    def __init__(self, recipe):
        self.recipe = recipe
        self.faceTracker = tracker.FaceTracker(use_nao)

    def cook(self):
        #Create noise listener
        listener = NoiseListener()

        while self.recipe.done == False:
            #Wait until user says "Nao!"
            listener.listen_until_noise()

            #Ask what's up
            self.query_user()

            #Listen to the user
            self.listen_and_answer()


        self.say("Thank you for cooking with me, I hope to see you again soon!")
            
    def query_user(self):
        self.say("Yessss?")

    #Listen to actual question and answer
    def listen_and_answer(self):
        self.faceTracker.startTracking()
        eye_leds.set_eyes_to_green()
        resp = self.get_response()
        eye_leds.set_eyes_to_blue()
        self.answer(resp)
        self.faceTracker.stopStracking()
        eye_leds.set_eyes_to_white()

    def answer(self, resp):
        if resp:
            response, product_name, intent, confidence = resp
        else:
            return

        if confidence and confidence < 0.5:
            self.faceTracker.shake_no()
            self.say("I don't know what you mean.")
            return
            
        else:
            self.faceTracker.shake_yes()
            
        if intent == 'instruction_navigation':
            if 'relative_instruction_navigation' in response:
                self.on_navigation_intent(response['relative_instruction_navigation'])
            elif "stop" in response:
                self.recipe.done = True
        elif intent == 'check_duration':
            self.on_how_long_intent()
        elif intent == 'check_amount':
            self.on_how_much_intent(product_name)
        elif intent == 'what_tools': #Doesn't exist yet
            self.on_tools_intent()
        elif intent == "get_all_ingredients":
            self.on_get_all_ingredients_intent()


    def get_response(self):
        if not use_wit:
            return

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
            if self.recipe.done:
                return
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

    def on_get_all_ingredients_intent(self):
        self.say(self.recipe.ask_ingredients())

    def say(self, what):
        print "Saying", what
        speech.say(what)

if __name__ == '__main__':
    cupcake_recipe = recipe.cupcakes

    cookert = Cookert(cupcake_recipe)
    cookert.cook()
