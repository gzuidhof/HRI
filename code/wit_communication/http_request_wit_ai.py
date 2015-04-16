__author__ = 'stefjanssen'

import wit
import json
import speech_synthesis

access_token = 'ONIABRH52NRVRVSZIUHYHWUV6LGWKCP7'

def get_outcome_response(json_response):
    print "Raw json: ", json_response
    for key, value in json_response.iteritems():
        if key == "outcomes":
            outcome = value[0]
            break
    response = {}
    for key, value in outcome.iteritems():
        if key == "entities":
            for key2, value2 in value.iteritems():
                if key2 == "product":
                    print "Printing product value"
                    print key2, value2
                    response["product"] = value2[0]["value"]
        if key == "intent":
            response["intent"] = value

    return response

def get_wit_response():
    wit.init()
    response = wit.voice_query_auto(access_token)
    print('Response: {}'.format(response))
    wit.close()
    response = json.loads(response)
    response = get_outcome_response(response)
    return response

speech_synthesis.say_something("Ask me something!")
response = get_wit_response()

recipe = {"flour": "200 grams", "butter": "150 grams", "eggs": "2", "sugar": "150 grams"}

if response["intent"] == "check_amount":
    if "product" in response:
        if response["product"] not in recipe:
            speech_synthesis.say_something("You do not need " + response["product"])
        else:
            speech_synthesis.say_something("The amount you need of " + response["product"] + " is " + recipe[response["product"]])
    else:
        speech_synthesis.say_something("I did not quite get that, what product did you say?")




