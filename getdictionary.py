
from urllib.request import urlopen
from urllib.error import URLError

def internet_on():
    try:
        urlopen("http://google.com")
        return True
    except URLError as e:
        # print(e.reason)
        return False
        
def is_word_to_keep(wordstr):
    no_dash = '-' not in wordstr
    no_dot = '.' not in wordstr
    no_slash = '/' not in wordstr
    no_digit = wordstr.isalpha()
    return no_dash and no_dot and no_slash and no_digit 

def extract_word(rawbytes):
    return rawbytes.decode('utf-8').strip()
    
def get_dictionary():
    # https://github.com/dwyl/english-words/blob/master/words.txt
    url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
    response = urlopen(url)
    allwords = [extract_word(word) for word in response]        
    words = [word for word in allwords if is_word_to_keep(word)]
    return words

assert internet_on(), 'internet is required'

wordlist = get_dictionary()
print(wordlist)


    




