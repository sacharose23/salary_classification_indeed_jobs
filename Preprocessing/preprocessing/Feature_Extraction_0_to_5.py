# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# Feature Extraction
import pickle
import re

f = open('2.1_data.pkl', 'rb')
data = pickle.load(f)
f.close()

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print("______________________________________________________")
print("\nCreating Feature Matrix")
print("______________________________________________________")
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

# Creating 2D Array (Feature Matrix)
# Inner list can simply be extended by appending values :)
fmat = [[] for i in range(len(data))]

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

print("\n0 City")
print("1 Job Title")
for i in range(len(data)):
    fmat[i].append(data[i]['city'])
    fmat[i].append(data[i]['job_title'])
    pass

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

print("2 Experience")
for i in range(len(data)):
    if(data[i]['f1_value'] != 100):
        fmat[i].append(int(data[i]['f1_value']))
    else:
        fmat[i].append(None)
    pass

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

print("3 Bachelors")
patterns = ['ba', 'bs', 'bsc', 'bachelor', 'bachelor’s']
for i in range(len(data)):

    sentences = []
    for j in range(len(data[i]['text'])):
        for word in data[i]['text'][j].split():
            sentences.append(word)

    matches = []
    for j in range(len(sentences)):
        for pattern in patterns:
            if re.search(pattern, sentences[j]):
                if len(pattern) == len(sentences[j]):
                    matches.append(sentences[j])
    if(len(matches)) > 0:
        fmat[i].append(1)
    else:
        fmat[i].append(0)
    pass

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

print("4 Masters")
patterns = ['ma', 'ms', 'msc', 'master', 'master’s']
for i in range(len(data)):

    sentences = []
    for j in range(len(data[i]['text'])):
        for word in data[i]['text'][j].split():
            sentences.append(word)

    matches = []
    for j in range(len(sentences)):
        for pattern in patterns:
            if re.search(pattern, sentences[j]):
                if len(pattern) == len(sentences[j]):
                    matches.append(sentences[j])
    if(len(matches)) > 0:
        fmat[i].append(1)
    else:
        fmat[i].append(0)
    pass

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

print("5 Doctorate")
patterns = ['phd', 'doctorate']
for i in range(len(data)):

    sentences = []
    for j in range(len(data[i]['text'])):
        for word in data[i]['text'][j].split():
            sentences.append(word)

    matches = []
    for j in range(len(sentences)):
        for pattern in patterns:
            if re.search(pattern, sentences[j]):
                if len(pattern) == len(sentences[j]):
                    matches.append(sentences[j])
    if(len(matches)) > 0:
        fmat[i].append(1)
    else:
        fmat[i].append(0)
    pass

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print(fmat)

f = open('features_0_to_5.pkl', 'wb')
pickle.dump(fmat,f,-1)
f.close()
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----