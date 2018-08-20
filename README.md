# Make your Typeform Surveys Smarter with Watson AI 

### Sign Up Here Your IBM Cloud and Typeform Account

- [IBM Cloud](http://ibm.biz/toneanalyzer082218)
- [Typeform](http://bit.ly/tf-ibm-signup)

## Presentation 

[Make your Typeform surveys smarter with IBM Watson](https://docs.google.com/presentation/d/18JR1mW5xpEDqOqwv4ErYOefSy8QTtYQeD4p6-kjrxNs/edit?usp=sharing)

## Tutorial 

1. Sign Up for a Typeform Account 

   Use your Typeform account to create custom online surveys. We'll be using the "Webhooks" feature under "Integrate" to connect with Watson's Tone Analyzer API and to get survey data responses in real time. 

2. Sign Up for a IBM Cloud Account 

   We'll be using IBM Cloud Action to run our code and process our data using IBM Watson Tone Analyzer API. You can find the code [here](https://github.com/shubhaswamy/typeform-watson-tone/blob/master/assets/code/function.py). 

   - Configuring webhooks: 

     Integrate webhooks by creating an "Endpoint" URL in IBM Actions and adding it as a "Destination URL" in Typeform's Webhooks configurations. This enables Typeform to send IBM Actions data in real time as users submit responses.

     ![URLendpoint](https://raw.githubusercontent.com/shubhaswamy/typeform-watson-tone/master/assets/screenshots/URLendpoint.png)

   - Parameters:

     To make the application work, you'll need to set a few credentials as parameters in Cloud Actions. You'll need to set your `username` and `password` for IBM Watson Tone Analyzer. You can read more about the authentication [here](https://www.ibm.com/watson/developercloud/tone-analyzer/api/v3/curl.html?curl#authentication). You will also need to set the `questionID` for your specific question/ answer text that you would like to work with. You can find this questionID by investigating your JSON payload from Typeform and finding the corresponding "id". We'll be sending our results to Slack as an example for this demo. If you decide to do the same, you'll also need to create a [incoming slack Webhook](https://api.slack.com/incoming-webhooks).

   

   ![params](https://raw.githubusercontent.com/shubhaswamy/typeform-watson-tone/master/assets/screenshots/params.png)

   

   - Code: 

     The image below outlines the anatomy for the code we'll be using for this demo. You can find the code [here](https://github.com/shubhaswamy/typeform-watson-tone/blob/master/assets/code/function.py). 

   

   ![params](https://raw.githubusercontent.com/shubhaswamy/typeform-watson-tone/master/assets/screenshots/code.png)

   - Sending Results to Slack

     For this demo, we'll be sending our results into slack as users submit their responses on Typeform in real-time. Once you have added the code to your _Actions_ and configured the settings as shown above, you will be able to receive notifications on Slack which look like this: 

     ![params](https://raw.githubusercontent.com/shubhaswamy/typeform-watson-tone/master/assets/screenshots/slack.png)

     

     

     

     

     

     

     

     

     