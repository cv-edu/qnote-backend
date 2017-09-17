import url_to_text as utt
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, time, json

def class_text(class_url):
    '''
    returns str of class name
    if the class name is not detected, returns string 'uncategorised notes'
    '''
    class_dict = utt.url_to_text(class_url)
    dict_len = len(class_dict)
    
    if dict_len == 1:
        class_text = class_dict['line0']
        return class_text
    else:
        errortext_class = 'uncategorised notes'
        return error_class
    
def date_text(date_url):
    '''
    returns str of date
    '''
    date_dict = utt.url_to_text(date_url)
    dict_len = len(date_dict)
    
    if dict_len == 1:
        date_text = date_dict['line0']
        return date_text
    else:
        print('Error: failed to detect date')
        errortext_date = 'dd-mm-yy'
        return errortext_date
    
def title_text(title_url):
    '''
    returns str of title
    '''
    pass

def body_text(body_url):
    '''
    returns str of body
    '''
    pass

date_text('http://media02.hongkiat.com/psd-text-svg/logo-example.jpg')
date_text('http://www.jqueryscript.net/images/Easy-jQuery-Text-Rotator-With-Fancy-Typing-Animations-Bubble-Text.jpg')
date_text('https://static1.squarespace.com/static/5914d841e6f2e109b2a338f6/5967ce27197aea1849dcc069/596cf1fe17bffc03c0c16cca/1500392204858/mashable.png')
