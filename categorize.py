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
        return errortext_class
    
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
        errortext_date = 'dd-mm-yy'
        return errortext_date
    
def title_text(title_url):
    '''
    returns str of title
    '''
    title_dict = utt.url_to_text(title_url)
    dict_len = len(title_dict)
    
    if dict_len == 1:
        title_text = title_dict['line0']
        return title_text
    
    else:
        errortext_title = 'no title'
        return errortext_title

def body_text(body_url):
    '''
    returns str of body
    '''
    body_dict = utt.url_to_text(body_url)
    body_text = ''
    
    for linenum in body_dict:
        body_text = body_text + body_dict[linenum] + '\n'
    
    return body_text




'''
body_text('http://fabricjs.com/article_assets/2_7.png')
body_text('http://d2vlcm61l7u1fs.cloudfront.net/media%2F274%2F274f9b50-559e-438b-996c-ec73c8203158%2Fimage')
body_text('http://media02.hongkiat.com/psd-text-svg/logo-example.jpg')
body_text('http://www.jqueryscript.net/images/Easy-jQuery-Text-Rotator-With-Fancy-Typing-Animations-Bubble-Text.jpg')
body_text('https://static1.squarespace.com/static/5914d841e6f2e109b2a338f6/5967ce27197aea1849dcc069/596cf21f3a04110b1bad385a/1500392204866/buzzfeed.png')
'''
