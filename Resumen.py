import re
from transformers import pipeline

##Prueba modelo de resumen

##cargar archivo y eliminar fechas
with open(r'C:\Users\Mariano\Documents\Temp\texto.txt', 'r', encoding="utf-8") as f:
    archivo = f.readlines()

fecha = ''
sents = []
for elem in archivo:
    if len(elem)>1:
        if re.match(r'\b[0-9]{1,2}/[0-9]{1,2}', elem):
            fecha = re.findall(r'\b[0-9]{1,2}/[0-9]{1,2}', elem)[0]
            sents.append(elem.replace(fecha + ': ', ''))
        else:
            sents.append(elem)

sents_list = [x for x in sents if 'Marcelo' in x]

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

salida_ok = False
start_block = 0
len_text = 50 #len(sents_list)

##resumir, recortar texto si no alcanza la memoria
while Tue:
    while not salida_ok:
        try:
            resumen = summarizer(''.join(sents_list[start_block:start_block + len_text]), max_length=600, 
                min_length=30, do_sample=False)
            start_block = len_text + start_block
            len_text = 50
            break
        except (MemoryError, IndexError):
            print (f"Error - {start_block} - {len_text}")
            len_text = len_text - 2

with open(r'C:\Users\Mariano\Documents\Temp\salida_resumen.txt', 'w', encoding="utf-8") as f:
    f.write(resumen[0]['summary_text'])

