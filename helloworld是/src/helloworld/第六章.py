def gender_features(word):
    return{'last_letter':word[-1]}
"print(gender_features('smith'))"
from nltk.corpus import names
import random
names = ([(name,'male')for name in names.words('male.txt')]+
         [(name1,'female')for name1 in names.words('female.txt')])
print(random.shuffle(names))