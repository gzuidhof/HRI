__author__ = 'stefjanssen'

import wit
import json

access_token = 'ONIABRH52NRVRVSZIUHYHWUV6LGWKCP7'

example_json = "'outcomes': [{ 'entities': { 'product': [{ 'value':  'flour'}]},  'confidence': 1,  'intent':  'check_amount',  '_text':  'how much flour do I need'}],  'msg_id':  '88f8655e-57af-4d65-b497-4be599ecd987',  '_text':  'how much flour do I need'"

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
                response[key2] = value2[0]["value"]
        if key == "intent":
            response["intent"] = value
    print "json response:"
    print response
    return response

def get_wit_response():
    wit.init()
    response = wit.voice_query_auto(access_token)
    print('Raw: {}'.format(response))
    wit.close()
    response = json.loads(response)
    response = get_outcome_response(response)
    print "Parsed"
    print response
    return response

def test_parsing():
    json_parsed = json.loads(example_json)
    return get_outcome_response(json_parsed)