__author__ = 'stefjanssen'

import speech_synthesis
import http_request_wit_ai

speech_synthesis.say_something("Ask me something!")
response = http_request_wit_ai.get_wit_response()

recipe = {"flour": "200 grams", "butter": "150 grams", "eggs": "2", "sugar": "150 grams"}

if response["intent"] == "check_amount":
    if "product" in response:
        if response["product"] not in recipe:
            speech_synthesis.say_something("You do not need " + response["product"])
        else:
            speech_synthesis.say_something("The amount you need of " + response["product"] + " is " + recipe[response["product"]])
    else:
        speech_synthesis.say_something("I did not quite get that, what product did you say?")