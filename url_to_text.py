import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, time, json

def get_words_json(url):
    '''
    returns python lists and dicts of words in json format

    argument url must be str format
    '''

    # Replace the subscription_key string value with your valid subscription key.
    subscription_key = '996e10be4b784ae4a251f060c171b16c'
    uri_base = 'https://eastus2.api.cognitive.microsoft.com/vision/v1.0'

    requestHeaders = {
        # Request headers.
        # Another valid content type is "application/octet-stream".
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    # The URL of a JPEG image containing handwritten text.
    body = {'url' : url}

    # For printed text, set "handwriting" to false.
    params = {'handwriting' : 'true'}

    try:
        # This operation requrires two REST API calls. One to submit the image for processing,
        # The other to retrieve the text found in the image.
        #
        # This executes the first REST API call and gets the response.
        response = requests.request('POST', uri_base + '/RecognizeText', json=body, data=None, headers=requestHeaders, params=params)

        # Success is indicated by a status of 202.
        if response.status_code != 202:
            # If the first REST API call was not successful, display JSON data and exit.
            parsed = json.loads(response.text)
            print("Error:")
            print(json.dumps(parsed, sort_keys=True, indent=2))
            exit()

        # The 'Operation-Location' in the response contains the URI to retrieve the recognized text.
        operationLocation = response.headers['Operation-Location']

        # Note: The response may not be immediately available. Handwriting recognition is an
        # async operation that can take a variable amount of time depending on the length
        # of the text you want to recognize. You may need to wait or retry this GET operation.
        time.sleep(1)

        # Execute the second REST API call and get the response.
        response = requests.request('GET', operationLocation, json=None, data=None, headers=requestHeaders, params=None)

        # 'data' contains the JSON data. The following formats the JSON data for display.
        parsed = json.loads(response.text)
        return parsed
    except Exception as e:
        print('Error:')
        print(e)

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

    # Print status message
    json_status = json['status']

    # Sort lines. Lines are of type `dict`
    json_lines = json['recognitionResult']['lines']
    str_lines = {}

    for i, line in enumerate(json_lines):
        line_num = f"line{i}"
        str_lines[line_num] = line['text']

    return str_lines
