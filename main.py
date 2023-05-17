import re
import spacy

with open('texto.txt', 'r') as f:
    archivo = f.readlines()

nlp = spacy.load("es_core_news_sm")

fecha = ''
sents = []
for elem in archivo:
    if len(elem)>0:
        if re.match(r'\b[0-9]{1,2}/[0-9]{1,2}', elem):
            fecha = re.findall(r'\b[0-9]{1,2}/[0-9]{1,2}', elem)[0]
        for sent in nlp(elem).sents:
            sents.append([sent.text.replace(fecha + ': ', ''), fecha])
