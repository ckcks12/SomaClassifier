
# coding: utf-8

# 

# In[112]:

from sklearn.externals import joblib


# In[113]:


clf = joblib.load('classify.model')
cate_dict = joblib.load('cate_dict.dat')
vectorizer = joblib.load('vectorizer.dat')


# In[114]:

joblib.dump(clf,'n_classify.model')


# In[115]:

joblib.dump(cate_dict,'n_cate_dict.dat')
joblib.dump(vectorizer,'n_vectorizer.dat')


# In[116]:

cate_id_name_dict = dict(map(lambda (k,v):(v,k),cate_dict.items()))


# In[117]:

pred = clf.predict(vectorizer.transform(['[신한카드5%할인][서우한복] 아동한복 여자아동 금나래 (분홍)']))[0]
print cate_id_name_dict[pred]


# In[111]:

from konlpy.tag import Twitter
import re
twitter = Twitter()
def clean(str):
    #str = re.sub(r"([\[\(\{].*?[\]\)\}])", "", str)
    str = unicode(str, "utf-8")
    str = re.sub(r"[`~!@#$%^&*()\-_=+\\|;:\[\]{'\"},<.>\/?]", " ", str)
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
                stack.append(ss[0])
    if stack:
        str2 += u" " + u" ".join(stack)
        
    return str + u" " + u" ".join(twitter.nouns(str))


# In[ ]:

from bottle import route, run, template,request,get, post


import  time
from threading import  Condition
_CONDITION = Condition()
@route('/classify')
def classify():
    #now() # print the time.
    #img = request.GET.get('img','')
    name = request.GET.get('name', '') 
    #pred = clf.predict(vectorizer.transform([name]))[0]
    #return {'cate':cate_id_name_dict[pred]}
    
    cate = t(name)
    
    # debug
    return {"cate": cate}


run(host='0.0.0.0', port=8887, quiet=True)


#  * 추후 여기 docker 에서 뭔가 python package 설치할게 있으면 
#  * /opt/conda/bin/pip2 install bottle 이런식으로 설치 가능
