
# coding: utf-8

# 

# In[39]:

from sklearn.externals import joblib


# In[40]:


clf = joblib.load('classify.model')
cate_dict = joblib.load('cate_dict.dat')
vectorizer = joblib.load('vectorizer.dat')


# In[41]:

joblib.dump(clf,'n_classify.model')


# In[42]:

joblib.dump(cate_dict,'n_cate_dict.dat')
joblib.dump(vectorizer,'n_vectorizer.dat')


# In[43]:

cate_id_name_dict = dict(map(lambda (k,v):(v,k),cate_dict.items()))


# In[44]:

pred = clf.predict(vectorizer.transform(['[신한카드5%할인][서우한복] 아동한복 여자아동 금나래 (분홍)']))[0]
print cate_id_name_dict[pred]


# In[ ]:

from bottle import route, run, template,request,get, post


import  time
from threading import  Condition
_CONDITION = Condition()
@route('/classify')
def classify():
    now() # print the time.
    #img = request.GET.get('img','')
    name = request.GET.get('name', '')
    
    #pred = clf.predict(vectorizer.transform([name]))[0]
    #return {'cate':cate_id_name_dict[pred]}
    
    cate = t(name)
    
    # debug
    print name
    print cate
    print ""
    return {"cate": cate}


run(host='0.0.0.0', port=8887, quiet=True)


#  * 추후 여기 docker 에서 뭔가 python package 설치할게 있으면 
#  * /opt/conda/bin/pip2 install bottle 이런식으로 설치 가능

# In[17]:

from konlpy.tag import Twitter


# In[18]:

twitter = Twitter()


# In[20]:

print(twitter.nouns(u'단독입찰보다 복수입찰의 경우'))


# In[1]:

from konlpy.tag import Twitter
twitter = Twitter()

def t(name):
    #name = re.sub(r"([\[\(\{].*?[\]\)\}])", "", name)
    name = clean(name)
    return cate_id_name_dict[clf.predict(vectorizer.transform([name]))[0]]



    #name_list = twitter.nouns(unicode(name, "utf-8"))
    name_list = name.split()
    p_list = []
    for n in name_list:
        p = clf.predict(vectorizer.transform([n]))[0]
        p_list.append(p)
    max = 0
    p_max = 0
    for p in p_list:
        cnt = p_list.count(p)
        if cnt > max:
            max = cnt
            p_max = p
    return cate_id_name_dict[p_max]


# In[2]:

str = "[신한카드5%할인][서우한복] 아동한복 여자아동 금나래 (분홍)"


# In[3]:

t("[신한카드5%할인][늘사랑] 금박 꽃수 당의(1380-07 아동여)")


# In[4]:

print "A"


# In[5]:

name = re.sub(r"([\[\(\{].*?[\]\)\}])", "", name)
print name


# In[6]:

from datetime import timedelta
print (datetime.datetime.now() + datetime.timedelta(hours=9)).time()


# In[7]:

from datetime import timedelta, datetime
import datetime
def now():
    print (datetime.datetime.now() + datetime.timedelta(hours=9)).time()


# In[8]:

now()


# In[18]:

from konlpy.tag import Twitter
import re
twitter = Twitter()
def clean(str):
    #str = re.sub(r"([\[\(\{].*?[\]\)\}])", "", str)
    str = re.sub(r"[`~!@#$%^&*()\-_=+\\|;:\[\]{'\"},<.>\/?]", " ", unicode(str, "utf-8"))
    stack = []
    str2 = u""
    for s in str.split():
        s2 = twitter.pos(s)
        for ss in s2:
            #if ss[1] == u"Noun": # if noun then just put it.
            if ss[1] != u"Alpha" and ss[1] != u"Number" and ss[1] != u"Punctuation":
                str2 += u" " + u" ".join(stack)
                str2 += u" " + ss[0]
                stack = []
            else:
                if ss[1] != u"Number":
                    stack.append(ss[0])
    if stack:
        str2 += u" " + u"".join(stack)
        
    return str2


# In[28]:

from konlpy.tag import Twitter
import re
twitter = Twitter()
def clean(str):
    #str = re.sub(r"([\[\(\{].*?[\]\)\}])", "", str)
    str = unicode(str, "utf-8")
    str = str.replace("(", " ").replace(")", " ")
    str = str.replace("[", " ").replace("]", " ")
    str = str.replace("/", " ").replace(",", " ")
    str = str.replace("{", " ").replace("}", " ")
    stack = []
    str2 = u""
    for s in str.split():
        s2 = twitter.pos(s)
        for ss in s2:
            #if ss[1] == u"Noun": # if noun then just put it.
            if ss[1] != u"Alpha" and ss[1] != u"Number" and ss[1] != u"Punctuation":
                str2 += u" " + u"".join(stack)
                str2 += u" " + ss[0]
                stack = []
            else:
                stack.append(ss[0])
    if stack:
        str2 += u" " + u"".join(stack)
        
    return str2


# In[38]:

from konlpy.tag import Twitter
import re
twitter = Twitter()
def clean(str):
    #str = re.sub(r"([\[\(\{].*?[\]\)\}])", "", str)
    #str = re.sub(r"[`~!@#$%^&*()\-_=+\\|;:\[\]{'\"},<.>\/?]", " ", str)
    str = str.replace("(", " ").replace(")", " ")
    str = str.replace("[", " ").replace("]", " ")
    str = str.replace("/", " ").replace(",", " ")
    str = str.replace("{", " ").replace("}", " ")
    stack = []
    str2 = u""
    str = unicode(str, "utf-8")
    for s in str.split():
        s2 = twitter.pos(s)
        for ss in s2:
            #if ss[1] == u"Noun": # if noun then just put it.
            if ss[1] != u"Alpha" and ss[1] != u"Number" and ss[1] != u"Punctuation":
                str2 += u" " + u" ".join(stack)
                str2 += u" " + ss[0]
                stack = []
            else:
                if ss[1] != u"Number":
                    stack.append(ss[0])
    if stack:
        str2 += u" " + u"".join(stack)
        
    return str2


# In[ ]:



