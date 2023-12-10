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

sents_list = [x for x in sents if 'work' in x]

summarizer = pipeline("summarization", model="Falconsai/text_summarization")
##summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

with open(r'C:\Users\Mariano\Documents\Temp\salida_resumen_falcon.txt', 'w', encoding="utf-8") as f:
	for n, sent in enumerate(sents_list):
		try:
			if sent.count(" ") > 30:
				resumen = summarizer(sent, min_length=20, max_length=45, do_sample=True)
				f.write(resumen[0]['summary_text'] + "\n")
				print("-----")
				print(sent)
				print(resumen[0]['summary_text'] + "\n")
			else:
				f.write(sent + "\n")
				print("-----")
				print(sent)
		except (MemoryError, IndexError):
			print (f"Error - {len(sent)}")

