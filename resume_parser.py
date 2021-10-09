import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import nltk
from pyresparser import ResumeParser

df = pd.read_csv('./ResumeSkill.csv')

frontEnd = list(df['Front_End'])
back_End = list(df['Back_End'])
Android = list(df['Android_Developer'])
Machine_Learning = list(df['Machine_Learning'])

data = ResumeParser('./Atruba_OldTemp.pdf').get_extracted_data()
skills=data['skills']


f_end=0
b_end=0
android=0
ml=0

for i in skills:
    if i in frontEnd:
        f_end+=1
for i in skills:
    if i in back_End:
        b_end+=1 
for i in skills:
    if i in Machine_Learning:
        ml+=1
for i in skills:
    if i in Android:
        android+=1

domain_list = []
domain_list.append(f_end)
domain_list.append(b_end)
domain_list.append(ml)
domain_list.append(android)

domain_val = 0
domain_max = max(f_end,b_end,ml,android)
for i in range(len(domain_list)):
    if domain_max == domain_list[i]:
        domain_val = i
if domain_val==0:
    domain = "FrontEnd Developer"
elif domain_val==1:
    domain = "BackEnd Developer"
elif domain_val==2:
    domain = "Machine Learning"
elif domain_val==3:
    domain = "Android Developer"        

print(domain)