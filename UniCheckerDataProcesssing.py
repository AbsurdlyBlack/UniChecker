#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import bs4

unilist = []

url = 'https://www.macleans.ca/education/canadian-universities-minimum-entering-grades-by-faculty/'

res = requests.get(url)
soup = bs4.BeautifulSoup(res.text,'lxml')

uni_list = soup.select('tbody')

for info in uni_list:
    unilist.append(info)


# In[3]:


uni_list


# In[4]:


str(unilist)


# In[39]:


string = str(unilist)
x = string.replace("<tr>", "*")
y = x.replace("</tr>", "*")
z = y.replace("<td>", "*")
a = z.replace("</td>", "*")
print(a)


# In[6]:


uniT = a.split('#')
uniT


# In[7]:


for item in uniT:
    if item == "\n":
        uniT.remove(item)

print(uniT)


# In[8]:


for i in range(3):
    for item in uniT:
        if item == "\n":
            uniT.remove(item)
uniT.remove('[<tbody>\n')
uniT.remove('\n</tbody>]')
print(uniT)


# In[26]:


class University:

    def __init__(self, name, arts, science, commerce, engineering):
        self.name = name
        self.arts = arts
        self.science = science
        self.commerce = commerce
        self.engineering = engineering

    def setVariables():
        disallowed_characters = "-%qwertyuiopasdfghjklzxcvbnm,)(QWERTYUIOPASDFGHJKLZXCVBNM;"

        for character in disallowed_characters:
            iarts = arts.replace(character, "")
            iscience = science.replace(character, "")
            icommerce = commerce.replace(character, "")
            iengineering = engineering.replace(character, "")

        if (len(arts)==2):
            iarts = float(iarts)
        if (len(arts) == 3):
            iarts = float(iarts)
        if (len(arts ==4)):
            iarts = []
            iarts = [float(iarts[0]+iarts[1]), float(iarts[2]+iarts[3])]

    def show():
        return ("University : " + self.university + " " + iarts)


# In[38]:


ulist = []
el = 0
for i in range(70):
    uni = University(uniT[el], uniT[el+1], uniT[el+2], uniT[el+3], uniT[el+4])
    ulist.append(uni)
    el= el + 5

for i in range(len(ulist)):
    ulist[i].setVariables
    ulist[i].show


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




