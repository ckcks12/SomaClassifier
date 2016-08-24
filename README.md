# SomaClassifier

이 머신러닝은 네이브베이즈가 하듯이 공백을 기준으로 단어별로 빈도수에 따라 출현을 시킨다.

그러므로 상품명에서 최대한 많은 단어를 추출하는 것이 목표였다.



### 원본의 띄어쓰기를 최우선적으로 생각하였다.
왜냐하면 사람이 쓴 띄어쓰기만큼 정확할 수 없기 때문이다.
다시말해, 띄어쓰기를 안할 순 있어도 실수로 하는 경우는 매우 드물기 때문이다.



그리고 띄어쓰기로 분리된 단어들은 곧 feature이기 때문에 이 feature를 살리기위해

```str = re.sub(r"[`~!@#$%^&*()\-_=+\\|;:\[\]{'\"},<.>\/?]", " ", str)```

위와 같은 정규식을 통해 특문이나 괄호등을 없애는 것이 아니라 **공백**으로 치환하였다

또한 더 많은 특징을 위해 이에다가 원본을 split한 뒤 형태소에 따라 간단히 스택을 이용해 묶음 처리하기도 하였다.

아래의 소스와 같다.

```
from konlpy.tag import Twitter
import re
twitter = Twitter()
def clean(str):
    #str = re.sub(r"([\[\(\{].*?[\]\)\}])", "", str)
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
        
    return str + u" " + str2 + u" " + u" ".join(twitter.nouns(str))
```
