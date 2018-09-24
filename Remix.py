
# coding: utf-8

# In[5]:


get_ipython().system(u'pip install textblob ')


# In[97]:


import random 
from textblob import TextBlob

with open ('Remix.txt', 'r') as file:
    text = file.read()
    
blob = TextBlob(text)

adjectives = []
nouns = []
conjunction = []
preposition = []

for word, pos in blob.tags:
    if (pos == 'JJ'):
        adjectives.append(word)
    if (pos == 'NN'):
        nouns.append(word)
    if (pos == 'CC'):
        conjunction.append(word)
    if (pos == 'IN'):
        preposition.append(word)
        
        
for i in range(1):
    a = random.choice(adjectives)
    n = random.choice(nouns)
    c = random.choice(conjunction)
    p = random.choice(preposition)
    print(a,n,p)
    
for i in range(1):
    p = random.choice(preposition)
    print(p)
    
for i in range(1):
    a = random.choice(adjectives)
    n = random.choice(nouns)
    print(a,n + ".")
    
for i in range(2):
    print(a,c)
    a = random.choice(adjectives)
    print(a + ".")
    
for i in range(1):
    a = random.choice(adjectives)
    n = random.choice(nouns)
    c = random.choice(conjunction)
    p = random.choice(preposition)
    print(a,n,p)
    
for i in range(1):
    p = random.choice(preposition)
    print(p)
    
for i in range(1):
    a = random.choice(adjectives)
    n = random.choice(nouns)
    print(a,n + ".")
    
for i in range(2):
    print(a,c)
    a = random.choice(adjectives)
    print(a + "...")
    
        



