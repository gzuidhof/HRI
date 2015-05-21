__author__ = 'stefjanssen'

import speech_synthesis
import http_request_wit_ai
import naoqi_speech

def ask_for_something():
    naoqi_speech.say("Ask me something!")

    response = http_request_wit_ai.get_wit_response()
    recipe = {"flour": "200 grams", "butter": "150 grams", "eggs": "2", "sugar": "150 grams", "duration": "15 minutes"}

    steps = ["Mix flour with butter", "Cook the pasta", "Do something cool"]

    current_step = 0

    product_name = str(response["product"])
    intent = str(response["intent"])
    print "printing stuff"
    print product_name
    print intent


    if intent == "check_amount":
        if "product" in response:
            if product_name not in recipe:
                naoqi_speech.say("You do not need " + product_name)
            else:
                naoqi_speech.say("The amount you need of " + product_name + " is " + recipe[product_name])
        else:
            naoqi_speech.say("I did not quite get that, what product did you say?")

    if intent == "check_duration":
        naoqi_speech.say("You need to perform this for " + recipe["duration"])

    if intent == "instruction_navigation":
        print 'in instruction navigation'
        if "relative_instruction_navigation" in response["entities"]:
            print 'in relative if'
            if response["relative_instruction_navigation"] == "next":
                print 'next'
                current_step += 1
                naoqi_speech.say("The next step is: " + steps[current_step])
            elif response["relative_instruction_navigation"] == "previous":
                print 'previous'
                current_step -= 1
                current_step = max(0, current_step)
                naoqi_speech.say("The previous step is: " + steps[current_step])
    ask_for_something()

ask_for_something()