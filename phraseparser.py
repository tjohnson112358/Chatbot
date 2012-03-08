#!/usr/bin/python
from HTMLParser import HTMLParser
import phrases as ph

class MyHTMLParser(HTMLParser):
    current_type = None
    current_question = None
    current_action = None
    current_phrase = None
    phrases = []
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        attrs_dict = {"type": '', 'question': '', 'action': ''}
        for i in attrs:
            attrs_dict[i[0]] = i[1] 
        if tag == "inphrase":
            print attrs
            self.current_phrase = ph.Inphrase(attrs_dict['type'], "", question = attrs_dict['question'],
                                              action = attrs_dict['action']);
        elif tag == 'outphrase':
            self.current_phrase = ph.Outphrase(attrs_dict['type'], "", question = attrs_dict['question'],
                                              action = attrs_dict['action']);
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
        self.phrases.append(self.current_phrase)
    def handle_data(self, data):
        print('Data: ' + data + ':end')
        self.current_phrase.content = data
        print("Encountered some data  :", data)

parser = MyHTMLParser()

def getphrasesfromdata(data):
    parser.feed(data.strip().replace('\n', '').replace('\r', ''))
    return parser.phrases

def getphrasesfromfile(filename):
    return getphrasesfromdata(open(filename).read())