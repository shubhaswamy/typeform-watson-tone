#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#

# import libraries 
import sys
import json
from watson_developer_cloud import ToneAnalyzerV3

# get the response data from typeform, and proccess it using Watson Tone Analyzer
def main(args):
    response = args.get('form_response')
    
    answerText = "" 
    
    # parse through typeform response payload 
    for x in response["answers"]:
        answersID = x['field']['id']
        questionID = 'R2xIdf96H85x'
        
        if (answersID == questionID):
            answerText = x["text"]
    
    #set username and password
    tone_analyzer = ToneAnalyzerV3(
    version ='2017-09-21',
    username ='{username}', # replace this
    password ='{password}' # replace this 
    )
    
    content_type = 'application/json'
    
    #return tone in JSON format
    tone = tone_analyzer.tone({"text": answerText},content_type) 
    
    # print(json.dumps(tone, indent=2))
    