from typing import Text
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import json

import numpy as np


Social_media=[]
Specialitys=[]
Prices=[]
Symptoms_treated=[]



html_text=requests.get('https://mdlnext.mdlive.com/').text
soup=BeautifulSoup(html_text,'lxml')
    
for a in soup.find_all('a',attrs={'class':'sc-fFubgz Footer__SocialHyperlink-sc-1vwei4j-9 slRiJ iLuaBb'}):
    socials=a.get('href').replace(" ",'')
    Social_media.append(socials)


for b in soup.find_all('div',attrs={'class':'sc-dlfnbm WhatWeTreat__ResponsiveCol-sc-1j7d4y8-11 bgtdbM dLQtFj'}):

    Speciality=b.find_next('h4',class_='sc-fubCfw sc-pFZIQ WhatWeTreat__RootHeading-sc-1j7d4y8-2 WhatWeTreat__StyledHeadingH4-sc-1j7d4y8-4 ipbctO giKbLZ fhOVsP dKJKPA')
    Price=Speciality.find_next_sibling('h4').text.replace(" ",'')
    Prices.append(Price)
    Specialitys.append(Speciality.text)

    Symptoms=b.find('p',class_='WhatWeTreat__StyledParagraph-sc-1j7d4y8-10 WhatWeTreat__Symptom-sc-1j7d4y8-12 hMa-dJK fRLkfO')
    Symptoms_=""
    Symptoms_=Symptoms_+(Symptoms.text.replace(" ",''))
    for s in Symptoms.find_next_siblings('p'):
        Symptoms_=Symptoms_+'\n'
        Symptoms_=Symptoms_+(s.text.replace("",''))
    Symptoms_treated.append(Symptoms_)

   
for c in soup.find_all('div',attrs={'class':'sc-dlfnbm WhatWeTreat__ResponsiveCol-sc-1j7d4y8-11 bgtdbM UNHFu'}):
    Speciality=c.find('h4',class_='sc-fubCfw sc-pFZIQ WhatWeTreat__RootHeading-sc-1j7d4y8-2 WhatWeTreat__StyledHeadingH4-sc-1j7d4y8-4 ipbctO giKbLZ fhOVsP dKJKPA')
    Price=Speciality.find_next_sibling('h4').text.replace(" ",'')
    Prices.append(Price)
    Specialitys.append(Speciality.text)
    Symptoms=c.find('p',class_='WhatWeTreat__StyledParagraph-sc-1j7d4y8-10 WhatWeTreat__Symptom-sc-1j7d4y8-12 hMa-dJK fRLkfO')
    Symptoms_=""
    Symptoms_=Symptoms_+(Symptoms.text.replace(" ",''))
    for s in Symptoms.find_next_siblings('p'):
        Symptoms_=Symptoms_+'\n'
        Symptoms_=Symptoms_+(s.text.replace("",''))

    
    Symptoms_treated.append(Symptoms_)



#include extra remarks

  
Titles=[]
Dates=[]
Bloglinks=[]
Summarys=[]
html_text= 'https://www.mdlive.com/blog/page/'
for i in range(2,10):
    req = requests.get(html_text + str(i) + '/')
    soup=BeautifulSoup(req.text,'html.parser')
    
    for z in soup.find_all('div',attrs={'class':'site-content'}):
        for x in z.find_all('article'):
            Title=x.find('div',class_='content-wrapper')
            
            Ti=Title.find('header',class_='entry-header')
            T=Ti.find('h2',class_='entry-title')
            Date=Ti.find('time',class_='entry-date').text.replace("\n",'')
            Dates.append(Date)
            link=T.find('a').get('href').replace(" ",'')
            Bloglinks.append(link)
            Titles.append(T.text.replace("\n",'').replace("â€™",' ').replace("â€“",' ').replace("â€¦",' ').replace("Â",' ').replace("â€™s",'s').replace("â€™re",'re').replace("â€™t",'t').replace("â€“",'').strip())
            Summary=Title.find('div',class_='entry-summary').text.replace("\n",'').replace("â€™",' ').replace("â€“",' ').replace("â€¦",' ').replace(" Â%",'').replace("â€™s",'s').replace("â€™re",'re').replace("â€™t",'t').replace("â€“",'').replace("â€™ve",'ve').replace("â€¦Click",'Click').strip()
            Summarys.append(Summary)
#general FAQS            
Questions=[]
Answers=[]
Answerlinks=[]
html_text=requests.get('https://www.mdlive.com/patients/faqs/').text
soup=BeautifulSoup(html_text,'lxml')
for r in soup.find_all('div',attrs={'class':'vc_tta-panel'}): 
    Question=r.find('h4',class_='vc_tta-panel-title vc_tta-controls-icon-position-right').text
    Questions.append(Question)
    Answer=r.find('div',class_='vc_tta-panel-body').text.replace("\n",'')
    Answers.append(Answer)
    AnsweLink=r.find('a').get('href')
    Answerlinks.append("https://www.mdlive.com/patients/faqs/"+AnsweLink)
#Dermatology FAQS
DermatologyQuestions=[]
DermatologyAnswers=[]
DermatologyAnswerlinks=[]
html_text=requests.get('https://www.mdlive.com/dermatology/').text
soup=BeautifulSoup(html_text,'lxml')
for r in soup.find_all('div',attrs={'class':'vc_tta-panel'}): 
    DermatologyQuestion=r.find('h4',class_='vc_tta-panel-title vc_tta-controls-icon-position-right').text
    DermatologyQuestions.append(DermatologyQuestion)
    DermatologyAnswer=r.find('div',class_='vc_tta-panel-body').text.replace("\n",'')
    DermatologyAnswers.append(DermatologyAnswer)
    DermatologyAnsweLink=r.find('a').get('href')
    DermatologyAnswerlinks.append("https://www.mdlive.com/dermatology/"+DermatologyAnsweLink)

html_text=requests.get('https://www.mdlive.com/contact-us/').text
soup=BeautifulSoup(html_text,'lxml')
for u in soup.find_all('div',attrs={'class':'vc_tta-panel'}): 
    Question=u.find('h4',class_='vc_tta-panel-title vc_tta-controls-icon-position-right').text
    Questions.append(Question)
    Answer=u.find('div',class_='vc_tta-panel-body').text.replace("\n",'')
    Answers.append(Answer)
    AnsweLink=u.find('a').get('href')
    Answerlinks.append("https://www.mdlive.com/patients/faqs/"+AnsweLink)
Contactfors=[]
Contacts=[]

for n in soup.find_all('div',attrs={'class':'whiteShadow wpb_column vc_column_container vc_col-sm-4'}):  
    Contactfor=n.find_all('h5',class_='head_sm_light blue')
    for C in Contactfor:
        
        Contactfors.append(C.text)
    Conatct=n.find_all('p')
    for C in Conatct:
        

        Contacts.append(C.text)
#Behavioural Health FAQS
behavioralhealthQuestions=[]
behavioralhealthAnswers=[]
html_text='https://mdlnext.mdlive.com/behavioral-health'
response = requests.post(html_text)
soup=BeautifulSoup(response.content,'html.parser')

for k in soup.find("script",attrs={'type':'application/json'}):
    Text=k.string
    data = json.loads(Text)
    for n in  range(0,10):
        behavioralhealthQuestion=data["props"]["pageProps"]["faqsSection"]["FAQList"][n]['question']
        behavioralhealthQuestions.append(behavioralhealthQuestion)
        behavioralhealthAnswer=data["props"]["pageProps"]["faqsSection"]["FAQList"][n]['answer']
        behavioralhealthAnswers.append(behavioralhealthAnswer)
   # for b in k.find_all('button',class_='sc-fodVxV FAQContainer__ItemButton-sc-860ilc-1 drhNYx yvzuv'):
        
    
      

abc = {'Social_media':Social_media,'Prices':Prices,'Specialitys':Specialitys,'Symptoms_treated':Symptoms_treated,
'behavioralhealthQuestions':behavioralhealthQuestions,
'behavioralhealthAnswers':behavioralhealthAnswers,
'DermatologyQuestions':DermatologyQuestions,'DermatologyAnswers':DermatologyAnswers,
'DermatologyAnswerlinks':DermatologyAnswerlinks,'Questions':Questions,
'Answers':Answers,'AnswersLink':Answerlinks,'Titles':Titles,'Date':Dates,'BlogLink':Bloglinks,
 'Contactfor':Contactfors,'Contacts':Contacts,
}
df = pd.DataFrame.from_dict(abc, orient='index')
df = df.transpose() 
df.to_csv('MDLIVE.csv', index=False, encoding='utf-8')
