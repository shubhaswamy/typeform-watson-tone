
# import libraries for watson & to work with JSON data 
import requests
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
        questionID = args.get('questionID') #get custom questionID from parameters
        
        if (answersID == questionID):
            answerText = x["text"]
    
    #set username and password from parameters
    tone_analyzer = ToneAnalyzerV3(
    version ='2017-09-21',
    username = args.get('username'),
    password =args.get('password') 
    )
    
    content_type = 'application/json'
    
    #return tone in JSON format
    tone = tone_analyzer.tone({"text": answerText},content_type) 
    
    
    
    
    # ----- send data to slack -----
    
    #parse through data to send in slack
    tones = str(tone['document_tone']['tones'])
    review = ""
    for x in tone['sentences_tone']:
        review += (x["text"] + " ")

    allTones = ""
    for y in tone['document_tone']['tones']:
        allTones += (y['tone_name'] + " ")
        
    scoreTotal = 0
    count = 0
    for z in tone['document_tone']['tones']:
        scoreTotal += z["score"]
        count += 1

    averageScore = scoreTotal/count
    strAvgScore = str(averageScore)
    

    # send slack payload 
    slack_data = {
    "attachments": [
        {
            "pretext": "New review submitted",
            "color": "#0b439e",
            "text": review,
            "fields": [
                {
                    "title": "Tones Found in Review",
                    "value": allTones,
                    "short": False
                },
                {
                    "title": "Average Tone Score",
                    "value": strAvgScore,
                    "short": False
                }
            ]
        }
    ]
}

    # get custom webhook from parameter 
    webhook_url = args.get('slackWebhook')
    

    #Post data to slack
    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    
    #return JSON format   
    return {"body":tone}
    
    