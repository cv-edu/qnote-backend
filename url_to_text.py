'''
returns extracted text from the image of handwritten notes
url_to_text(url) returns str_lines.
str_lines is a dict with format: {'line0' : 'line1text', 'line1' : 'line2text, ... }
'''


import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, time, json


def get_words_json(url):
    '''
    returns python lists and dicts of words in json format
    
    argument url must be str format
    '''
    
    # Replace the subscription_key string value with your valid subscription key.
    subscription_key = '996e10be4b784ae4a251f060c171b16c'
    
    # Replace or verify the region.
    #
    # You must use the same region in your REST API call as you used to obtain your subscription keys.
    # For example, if you obtained your subscription keys from the westus region, replace 
    # "westcentralus" in the URI below with "westus".
    #
    # NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
    # a free trial subscription key, you should not need to change this region.
    uri_base = 'https://eastus2.api.cognitive.microsoft.com/vision/v1.0'
    
    requestHeaders = {
        # Request headers.
        # Another valid content type is "application/octet-stream".
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    
    # The URL of a JPEG image containing handwritten text.
    #body = {'url' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Cursive_Writing_on_Notebook_paper.jpg/800px-Cursive_Writing_on_Notebook_paper.jpg'}
    body = {'url' : url}
    
    # For printed text, set "handwriting" to false.
    params = {'handwriting' : 'true'}
    
    try:
        # This operation requrires two REST API calls. One to submit the image for processing,
        # the other to retrieve the text found in the image. 
        #
        # This executes the first REST API call and gets the response.
        response = requests.request('POST', uri_base + '/RecognizeText', json=body, data=None, headers=requestHeaders, params=params)
    
        # Success is indicated by a status of 202.
        if response.status_code != 202:
            # if the first REST API call was not successful, display JSON data and exit.
            parsed = json.loads(response.text)
            exit()
    
        # The 'Operation-Location' in the response contains the URI to retrieve the recognized text.
        operationLocation = response.headers['Operation-Location']
    
        # Note: The response may not be immediately available. Handwriting recognition is an
        # async operation that can take a variable amount of time depending on the length
        # of the text you want to recognize. You may need to wait or retry this GET operation.
        
        #time.sleep required. else microsoft detects as potential ddos attack
        time.sleep(1)
    
        # Execute the second REST API call and get the response.
        response = requests.request('GET', operationLocation, json=None, data=None, headers=requestHeaders, params=None)
    
        # 'data' contains the JSON data. The following formats the JSON data for display.
        parsed = json.loads(response.text)
        return parsed
        handwriting_json = json.dumps(parsed, sort_keys=True, indent=2)
        #return handwriting_json
    
    except Exception as e:
        print(e)
        exit()
    
def url_to_text(url):
    '''
    returns dict with the extracted text data in the format:
    str_lines = {'line0' : 'line1text', 'line1' : 'line2text'}
    '''
    json = get_words_json(url)
    str_lines = extract_words(json)
    return str_lines

def extract_words(json):
    '''
    prints relevant json data
    
    argument json must be in json type
    '''
    #print status message
    json_status = json['status']
    
    #sort lines. lines are dict type
    json_lines = json['recognitionResult']['lines']
    str_lines = {}
    cnt = 0
    for dict in json_lines:
        line_num = 'line' + str(cnt)
        str_lines[line_num] = dict['text']
        cnt = cnt + 1
    
    return str_lines

#https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Cursive_Writing_on_Notebook_paper.jpg/800px-Cursive_Writing_on_Notebook_paper.jpg
