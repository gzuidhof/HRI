import recipe
import facetracker as tracker
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
        self.ledController = eye_leds.LedController(use_nao)

    def cook(self):
        #Create noise listener
        listener = NoiseListener()
        self.faceTracker.start_tracking()
        self.say("Hello there human, welcome to the cooking robot demo! I will help you how to make cupcakes."
                 " by answering your questions. You can ask me what to do, how long to do it, what you need, what the next step is"
                 " and many other things. Let's begin!"
        )
        self.faceTracker.stop_tracking()

        while self.recipe.done == False:
            #Wait until user says "Nao!"
            listener.listen_until_noise()

            #Ask what's up
            self.query_user()

            #Listen to the user
            self.listen_and_answer()


        self.say( "Thank you for cooking with me, I hope to see you again soon!")
            
    def query_user(self):
        self.say("Yessss?")

    #Listen to actual question and answer
    def listen_and_answer(self):
        self.faceTracker.start_tracking()
        self.ledController.set_eyes_to_green(use_nao)
        resp = self.get_response()
        self.ledController.set_eyes_to_blue(use_nao)
        self.answer(resp)
        self.faceTracker.stop_tracking()
        self.ledController.set_eyes_to_white(use_nao)

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
                if self.recipe.done:
                    self.say("Okay we're finished.")
            elif "stop" in response:
                self.say("Okay let's stop.")
                self.recipe.done = True
        elif intent == 'check_duration':
            self.on_how_long_intent()
        elif intent == 'check_amount':
            self.on_how_much_intent(product_name)
        elif intent == 'tools': #Doesn't exist yet
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
    cupcake_recipe = recipe.better_cupcakes

    cookert = Cookert(cupcake_recipe)
    cookert.cook()
