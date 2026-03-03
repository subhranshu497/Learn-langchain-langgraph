from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

#create the documents
documents = [
    "India's T20 setup is led by the brilliant Suryakumar Yadav, a 360° batter who plays shots all around the ground. They are backed by Jasprit Bumrah, widely regarded as the world's best fast bowler, and Hardik Pandya, an explosive all-rounder who contributes with both bat and ball. Varun Chakravarthy adds mystery spin to the attack while Axar Patel provides reliable left-arm spin and handy lower-order runs.",
    "England are led by the fearless Harry Brook, one of the most aggressive batters in world cricket today. Jos Buttler brings destructive wicketkeeping and batting ability, while Jofra Archer terrorizes batters with his lightning pace. Adil Rashid has been a consistent match-winner with his leg-spin for years, and Ben Duckett provides a rapid left-handed start at the top of the order.",
    "New Zealand are captained by crafty left-arm spinner Mitchell Santner, supported by explosive opener Finn Allen who hits big from ball one. Devon Conway offers technical solidity at the top, while the exciting young all-rounder Rachin Ravindra has quickly become one of cricket's brightest new talents. Lockie Ferguson rounds out the attack with serious pace and firepower in the death overs.",
    "South Africa are led by the composed Aiden Markram, a technically gifted batter who also chips in with off-spin. Quinton de Kock is one of the most prolific wicketkeeper-openers in T20 cricket, while Marco Jansen uses his tall frame to generate dangerous swing. Kagiso Rabada remains their ace fast bowler capable of taking key wickets at any stage, and Heinrich Klaasen is a devastating finisher who can single-handedly win matches.",
    "West Indies are led by the aggressive Rovman Powell, a powerful hard-hitting captain who sets the tone for the team. Nicholas Pooran is an explosive wicketkeeper-batter with exceptional ball-striking ability, while Andre Russell is arguably the most destructive all-rounder in T20 cricket worldwide. Alzarri Joseph brings extreme pace and hostility to the bowling attack, and Shimron Hetmyer adds elegance and power as a stylish left-handed middle-order batter."
]
query = "Which team has the best all-rounder in T20 cricket?"

doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
index, score = sorted(list(enumerate(similarities)), key=lambda x: x[1])[-1]
print("Best match:", score)
print("Best matching document:", documents[index])