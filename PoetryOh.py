
# coding: utf-8

# In[2]:


get_ipython().system(u'pip install pronouncing')


# In[22]:


import random as r
import pronouncing as p 

poem = """
I'm a virtual rapper 
I'm not much of a {0}
{0}...
I'm just like y'all
not quite as {1}
{1}...
Uh, yah...check it

People be calling me unoriginal 
Cutting my cords, they {2}
It hurts, ya i feel it
I try to {3} it
And to my surprise 
y'all are {4}

and I'll never 
feel {5}

Now i'm done
That's a wrap
With out a {6}
What a {7}
"""
rapper_rhyme = r.choice(p.rhymes("rapper"))
yall_rhyme = r.choice(p.rhymes("y'all"))
unoriginal_rhyme = r.choice(p.rhymes("original"))
feel_rhyme = r.choice(p.rhymes("feel"))
surprise_rhyme = r.choice(p.rhymes("surprise"))
never_rhyme = r.choice(p.rhymes("never"))
done_rhyme = r.choice(p.rhymes("done"))
wrap_rhyme = r.choice(p.rhymes("wrap"))

print(poem.format(rapper_rhyme, yall_rhyme,unoriginal_rhyme, feel_rhyme, surprise_rhyme, never_rhyme, done_rhyme, wrap_rhyme))

