# author : Yue Wang (github @tinyleap)

from bs4 import BeautifulSoup
import urllib.request
import os
import time

def job_scraper(title, city, lower, upper):
    raw = 'https://www.indeed.com/jobs?q=title:"{0}"+${1},000+-+${2},000&l={3}&radius=100&jt=fulltime'
    webpage = raw.format('+'.join(title.split()), lower, upper, '+'.join(city.split()))
    print(webpage)
    websource = urllib.request.urlopen(webpage)
    soup = BeautifulSoup(websource, "html.parser")
    try:
        total = int(bottom(soup.find('div', {'id':"searchCount"}))[0].strip().split()[3])
    except:
        return -1
    print('total '+str(total))
    directory = '-'.join([title, city, str(lower), str(upper)])
    if not os.path.exists(directory):
        os.makedirs(directory)
    count = 0
    for i in range(total//10+1):
        for each in soup.findAll('a', {'data-tn-element':"jobTitle"}):
            # skip sponsored
            sponsor = each.parent.find('span', {'class':'sponsoredGray'})
            if (sponsor!=None):
                continue
            # create file
            count += 1
            print(count, end=' ')
            f = open(directory+'/'+str(count)+".txt", 'w')
            # get url
            url = 'https://www.indeed.com' + each.get('href')
            f.write(url+'\n')
            # get title
            f.write("".join(bottom(each))+'\n')
            # get description
            ws = urllib.request.urlopen(url)
            sp = BeautifulSoup(ws, "html.parser")
            try:
                f.write("\n".join(bottom(sp.find('div', {'class':"jobsearch-JobComponent-description icl-u-xs-mt--md"}))))
            except:
                print('fail')
                f2 = open(directory+"/fail.txt", 'a')
                f2.write(str(count)+'\n')
                f2.close()
            f.close()
        websource = urllib.request.urlopen(webpage+'&start='+str(count))
        soup = BeautifulSoup(websource, "html.parser")
    time.sleep(10)
    print()

def bottom(tag):
    result = []
    for each in tag.descendants:
        if isinstance(each, str):
            result.append(each)
        else:
            bottom(each)
    return result

title_list = ['Data Engineer', 'Data Scientist', 'Machine Learning Engineer', 'Database Administrator', 'Web Designer',
              'Back end Developer', 'Back end Engineer', 'Desktop Application Engineer', 'Embedded Systems Engineer', 
              'Front end Develope', 'Front end Engineer', 'Full stack developer', 'Full stack engineer', 
              'Mobile Application Developer', 'Mobile Application Engineer', 'Quality Assurance Developer', 
              'DevOps engineer', 'Site Reliability Engineer', 'Product manager', 'chief technology officer', 
              'chief information officer', 'System administrator']
city_list = ['San Francisco', 'Los Angeles', 'New York', 'Seattle', 'Austin', 'Charlotte', 'Boston', 'Provo', 
             'Boulder', 'San Diego']
lower_list = range(50, 300, 10)

for title in title_list:
    for city in city_list:
        for lower in lower_list:
            job_scraper(title, city, lower, lower+10)
