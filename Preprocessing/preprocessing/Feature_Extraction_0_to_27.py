# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# Feature Extraction
import pickle
import re

f = open('2.1_data.pkl', 'rb')
data = pickle.load(f)
f.close()

f = open('features_0_to_5.pkl', 'rb')
fmat = pickle.load(f)
f.close()

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

print("6 to 27 Field of Study")
patterns = ["computer science", "computer engineering", "software engineering", "web development", "web design", "information systems" ,"information technology" ,"system administration" ,"mathematics" ,"statistics" ,"engineering" ,"civil" ,"electrical" ,"mechanical" ,"business" ,"accounting" ,"finance" ,"marketing" ,"science" ,"biology" ,"chemistry" ,"physics"]
for i in range(len(data)):

    sentences = []
    for j in range(len(data[i]['text'])):
        for word in data[i]['text'][j].split():
            sentences.append(word)
    print(sentences)

    for pattern in patterns:
        matches = []
        for j in range(len(sentences)):
            if re.search(pattern, sentences[j]):
                if len(pattern) == len(sentences[j]):
                    matches.append(sentences[j])
        if(len(matches)) > 0:
            fmat[i].append(1)
        else:
            fmat[i].append(0)
    pass
    print()

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print(fmat)

f = open('features_0_to_27.pkl', 'wb')
pickle.dump(fmat,f,-1)
f.close()
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----