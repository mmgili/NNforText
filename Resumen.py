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

##summarizer = pipeline("summarization", model="Falconsai/text_summarization")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

salida_ok = False
start_block = 0
len_text = 18 #len(sents_list)

##resumir, recortar texto si no alcanza la memoria
with open(r'C:\Users\Mariano\Documents\Temp\salida_resumen.txt', 'w', encoding="utf-8") as f:
	while not (start_block >= len(sents_list)) or start_block > 200:
		try:
			resumen = summarizer(''.join(sents_list[start_block:start_block + len_text]), max_new_tokens=40, do_sample=False)
			f.write(resumen[0]['summary_text'] + "\n")
		except (MemoryError, IndexError):
			print (f"Error - {start_block} - {len_text}")
			len_text = len_text - 2
		else:
			start_block = len_text + start_block
			len_text = 50


