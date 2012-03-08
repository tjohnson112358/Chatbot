#!/usr/bin/python
import phraseparser

phrases = phraseparser.getphrasesfromfile('example.voc')

def getquestion(text):
    words = text.lower().replace(' the ', ' ').replace(' and ', ' ').replace(' a ', 
                       ' ').replace('.', '').replace(',', '').replace('?', '').split()
    num = -1
    highest_percent = 0.0
    for i in phrases:
        if i.type != 'query': 
            print("!= query")
            continue
        num_in_current_phrase = 0
        q = i.content.replace('.', '').replace(',', '').replace('?', '').lower().split()
        print(q)
        print('words: ' + str(words))
        for e in words:
            if e in q: num_in_current_phrase += 1
        cur_percent = (num_in_current_phrase + 0.0) / len(words)
        print('cur_percent: ' + str(cur_percent))
        if cur_percent > highest_percent: 
            highest_percent = cur_percent
            num = phrases.index(i)
    
    if num == -1:
        print("No matches")
        return None
    
    p = phrases[num]
    return p.question

def getconverse(type):
    '''Return the converse of a type.
       e.g. if passed "query" return "statement" and vice versa'''
    if type.lower() == 'query': return 'statement'
    elif type.lower() == 'statement': return 'query'
    
def get_question_or_statement_converse(q):
    qu = q.lower()
    if qu.startswith('query '):
        return 'STATE ' + q[6:]
    elif qu.startswith('state '):
        return 'QUERY ' + q[6:]

def getquestionresponse(question):
    type = question.split()[0].lower()
    for i in phrases:
        if i.type == getconverse(type):
            print('i.type passed')
            print(get_question_or_statement_converse(question))
            if i.action.lower() == get_question_or_statement_converse(question).lower():
                print('i.action passed')
                return i.content

question = getquestion("Where do you live?")
response = getquestionresponse(question)
print(question)
print(response)
print(getquestion("How do you feel today?"))
