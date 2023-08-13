import re
import spacy
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors

with open(r'C:\Users\Mariano\Documents\Temp\texto.txt', 'r', encoding="utf-8") as f:
    archivo = f.readlines()

nlp = spacy.load("es_core_news_sm")

fecha = ''
sents = []
for elem in archivo:
    if len(elem)>1:
        if re.match(r'\b[0-9]{1,2}/[0-9]{1,2}', elem):
            fecha = re.findall(r'\b[0-9]{1,2}/[0-9]{1,2}', elem)[0]
        for sent in nlp(elem).sents:
            sents.append([sent.text.replace(fecha + ': ', ''), fecha])

sents_list = [x[0] for x in sents]

embedder = SentenceTransformer('all-MiniLM-L6-v2')

corpus_embeddings = embedder.encode(np.array(sents_list))

# Normalize the embeddings to unit length
corpus_embeddings = corpus_embeddings /  np.linalg.norm(corpus_embeddings, axis=1, keepdims=True)
nbrs = NearestNeighbors(n_neighbors=3, algorithm='ball_tree').fit(corpus_embeddings)
distances, indices = nbrs.kneighbors(corpus_embeddings)

with open(r'C:\Users\Mariano\Documents\Temp\salida.txt', 'w', encoding="utf-8") as f:
    for n, s in enumerate(indices):
        if not (sents_list[n] == '\n'):
            f.write(f"#{n} - {sents_list[n]}\n")
            for i in range(0, 3):
                f.write(f"{sents[s[i]][0]} ##{sents[s[i]][1]}##\n")
            f.write("\n")