from bs4 import BeautifulSoup
import requests

#import own_resume_parser
#For resume skill extraction
#job_title = own_resume_parser.domain

job_title = input("Enter your preffered choice for job : ")
job_title.replace(" ","%20")
location = input("Enter your preferred Location : ")


url = "https://in.indeed.com/jobs?q={}&l={}&start=10".format(job_title,location)
page = requests.get(url)
#print(page.status_code)
#url2=[]
#for i in range(10,51,10):
#    url2.append("https://in.indeed.com/jobs?q=software%20developer%20fresher&l=Maharashtra&start={}".format(i))

    
soup = BeautifulSoup(page.content,'lxml')
upper = soup.find_all("h2",class_="jobTitle")
#print(upper)
title=[]
desc=[]
companies=[]
location=[]
salary=[]

def job_link_form(href):
    comp = []
    comp = href.split('/')
    #print(comp)
    if len(comp)<4:
        link = "https://in.indeed.com/viewjob?"
        cmp2 = comp[-1].split('?')
        cmp3 = cmp2[-1].split('&')
        #print(cmp3)
        key = cmp3[0]
        vjs = cmp3[-1]
        link = "https://in.indeed.com/viewjob?{}&from=serp&{}".format(key,vjs)
        return link
    else:
        c_name = comp[2]
        cmp2 = comp[-1].split('-')
        #print(cmp2)
        role = cmp2[0]+"+"+cmp2[1]
        #print("Role : ",role)
        cmp3 = cmp2[-1].split("?")
        key = cmp3[0]
        link = "https://in.indeed.com/viewjob?cmp={}&t={}&jk={}&vjs=3".format(c_name,role,key)
        return link

for i in upper:
    tit=i.find('span')
    title.append(tit.get('title'))

for i in range(len(title)):
    if title[i]== None:
        title[i]="Software Developer"


for i in soup.find_all("span",class_='companyName'):
    companies.append(i.text.strip()) 


"""for i in soup.find_all("span",class_="salary-snippet"):
    salary.append(i.text.strip())

print(salary)"""
for i in soup.find_all("div",class_="companyLocation"):
    location.append(i.text)

job_snip = soup.find_all("div",class_="job-snippet")
for i in job_snip:
    job_desc=i.find('li')
    desc.append(job_desc.text.strip())


link=[]
for i in soup.find_all("a",class_="fs-unmask"):
    job_link = i.get('href')
    job_lnk = job_link_form(job_link)
    link.append(job_lnk)

#print(len(link))

for i in range(len(link)):
    print("Title : {}".format(title[i]))
    print("Comapny Name : {}".format(companies[i]))
    print("Job Description : {}".format(desc[i]))
    print("Location : {}".format(location[i]))
    print("Apply Link : {}".format(link[i]))
    print("-----------------------------------------------------------")



