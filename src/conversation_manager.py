__author__ = 'stefjanssen'


import http_request_wit_ai

use_nao = True

if use_nao:
    import naoqi_speech
else:
    import speech_synthesis

def say(speech):
    if use_nao:
        naoqi_speech.say(speech)
    else:
        speech_synthesis.say_something(speech)


def ask_for_something():
    response = http_request_wit_ai.get_wit_response()
    if not response:
        return
    recipe = {"flour": "200 grams", "butter": "150 grams", "eggs": "2", "sugar": "150 grams", "duration": "15 minutes"}

    steps = ["Mix flour with butter", "Cook the pasta", "Do something cool"]

    current_step = 0
    if "product" in response:
        product_name = str(response["product"])
        print "product: " + product_name

    if "intent" in response:
        intent = str(response["intent"])
        print "intent: " + intent

    if "confidence" in response:
        confidence = float(response["confidence"])
        print "confidence: " + str(confidence)

    if confidence and confidence < 0.5:
        say("U wot, repeat that shit bitch")
        return

    if intent == "check_amount":
        if "product" in response:
            if product_name not in recipe:
                say("You do not need " + product_name)
            else:
                say("The amount you need of " + product_name + " is " + recipe[product_name])
        else:
            say("I did not quite get that, what product did you say?")

    if intent == "check_duration":
        say("You need to perform this for " + recipe["duration"])

    if intent == "instruction_navigation":
        print 'in instruction navigation'
        print response
        if "relative_instruction_navigation" in response:
            print 'in relative if'
            if response["relative_instruction_navigation"] == "next":
                print 'next'
                current_step += 1
                say("The next step is: " + steps[current_step])
            elif response["relative_instruction_navigation"] == "previous":
                print 'previous'
                current_step -= 1
                current_step = max(0, current_step)
                say("The previous step is: " + steps[current_step])
            elif response["relative_instruction_navigation"] == "current":
                print 'current'
                say("The current step is: " + steps[current_step])
            else:
                print "unknown"
                say("Unknown relative instruction navigation")
    return False

ask_for_something()


