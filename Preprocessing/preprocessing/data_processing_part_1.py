# Cleaning Data
import os
import pickle
from re import sub as re_sub

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# Functions
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

def clean(sentence):
    replace = {"`": " ", "˜": " ", "!": " ", "@": " ", "$": " ", "%": " ", "ˆ": " ", "&": " ", "*": " ","\'":" ",
               "(": " ", ")": " ", "-": " ", "_": " ", "+": " ", "|": " ", "\\": " ", "{": " ", "}": " ", "[": " ", "]": " ",
                ",":" ", "?":" ", "/":" ", "\"":" "}

    cleaned_sentence = "".join([replace.get(word,word)for word in sentence])
    cleaned_sentence = re_sub(' +',' ',cleaned_sentence)
    return cleaned_sentence

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\nAnalysing Data...")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

list_of_folders = os.listdir('Main_data')
list_of_folders.sort()
for i in range(len(list_of_folders)):
    list_of_folders[i] = list_of_folders[i].lower()

files_count = 0
for folder in list_of_folders:
    files = os.listdir("Main_data/"+folder)
    for file in files:
        files_count = files_count + 1
print("\tNo of Folders =", len(list_of_folders))
print("\tNo of Files = ",files_count)

job_title = []
city = []
salary_range = []

for i in range(len(list_of_folders)):
    raw = list_of_folders[i]
    temp = raw.split('-')
    job_title.append(temp[0])
    city.append(temp[1])

job_title = list(set(job_title))
city = list(set(city))
salary_range = ['50-60', '60-70', '70-80', '80-90', '90-100', '100-110', '110-120', '120-130', '130-140', '140-150', '150-160', '160-170', '170+']

job_title.sort()
city.sort()

print("\nPrimary Data Fields - List of Values")
print('\tJob titles: ',len(job_title))
print("\t\t", job_title)
print('\tCities: ',len(city))
print("\t\t", city)
print('\tSalary Ranges: ',len(salary_range))
print("\t\t", salary_range)

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\nBuilding 'data' - List of Dictionaries")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

data = [{} for i in range(files_count)]

counter = 0

for folder in list_of_folders:
    temp = folder.split('-')
    files = os.listdir("Main_data/"+folder)

    #print(counter)
    #print(temp)

    for file in files:

        data[counter]['job_title'] = temp[0]
        data[counter]['city'] = temp[1]
        if (int(temp[2]) > 169):    data[counter]['salary_range'] = 175.0
        else:   data[counter]['salary_range'] = (int(temp[2]) + int(temp[3])) / 2

        text_file = open("Main_data/" + folder + "/" + file, 'r',encoding='utf8', errors='ignore')

        data[counter]['primary_key'] = text_file.readline()
        data[counter]['unique'] = 0
        temp_txt_list = text_file.readlines()
        for i in range(len(temp_txt_list)):
            temp_txt_list[i] = clean(temp_txt_list[i])
            temp_txt_list[i] = temp_txt_list[i].lower()
        data[counter]['text'] = temp_txt_list
        text_file.close()

        counter = counter + 1

print("\tSample Data:")
print("\t", data[0])
print("\t", data[1000])

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\nIdentifying and Removing Duplicates")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

pkeys = []
ukeys = []

for i in range(files_count):
     pkeys.append(data[i]['primary_key'])

ucounter = 0
pcounter = 0
new_data = []

for i in range(len(data)):
    if pkeys[i] not in ukeys:
        ukeys.append(pkeys[i])
        data[i]['unique'] = 1
        ucounter = ucounter + 1
        new_data.append(data[i])

    else:
        data[i]['unique'] = 0
        pcounter = pcounter + 1

print("\tUnique Count:", ucounter)
print("\tDuplicate Count:", pcounter)
print("\tSample Data:\t\t", new_data[0], "\n\t\t", new_data[1000])

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\nPickling Data")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

f = open('0_job_title.pkl','wb')
pickle.dump(job_title,f,-1)
f.close()

f = open('0_city.pkl','wb')
pickle.dump(city,f,-1)
f.close()

f = open('0_salary_range.pkl','wb')
pickle.dump(salary_range,f,-1)
f.close()

f = open('1_data.pkl','wb')
pickle.dump(new_data,f,-1)
f.close()

f2 = open('1_data.pkl', 'rb')
data2 = pickle.load(f2)
f2.close()

print("\tVerifying Data (T/F):", (new_data == data2))

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----




