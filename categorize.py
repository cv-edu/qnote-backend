import url_to_text as utt
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, time, json

def class_text(content):
    '''
    returns str of class name
    if the class name is not detected, returns string 'uncategorised notes'
    '''

    if len(content) == 1:
        return content['line0']
    else:
        return 'uncategorised notes'

def date_text(content):
    '''
    returns str of date
    '''

    if len(content) == 1:
        return content['line0']
    else:
        return 'dd-mm-yy'

def title_text(content):
    '''
    returns str of title
    '''

    if len(content) == 1:
        return content['line0']
    else:
        return 'no title'

def body_text(content):
    '''
    returns str of body
    '''
    body_text = ''

    for linenum in content:
        body_text += content[linenum] + '\n'

    return body_text
