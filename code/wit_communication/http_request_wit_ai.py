__author__ = 'stefjanssen'

import wit
import json

access_token = 'ONIABRH52NRVRVSZIUHYHWUV6LGWKCP7'

print 'waaaaazzuuuup'

def get_outcome_response(json_response):
    print "Raw json: ", json_response

    for key, value in json_response.iteritems():
        if key == "_text":
            if value is None:
                return False

    for key, value in json_response.iteritems():
        if key == "outcomes":
            if value:
                outcome = value[0]
            break
    response = {}
    if outcome:
        for key, value in outcome.iteritems():
            if key == "entities":
                for key2, value2 in value.iteritems():
                    response[key2] = value2[0]["value"]
            if key == "intent":
                response["intent"] = value
            if key == "confidence":
                response["confidence"] = value
    return response

def get_wit_response():
    wit.init()
    response = wit.voice_query_auto(access_token)
    print('Raw: {}'.format(response))
    wit.close()
    response = json.loads(response)
    response = get_outcome_response(response)
    return response