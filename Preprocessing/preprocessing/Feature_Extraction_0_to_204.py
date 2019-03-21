# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# Feature Extraction
import pickle
import re

f = open('2.1_data.pkl', 'rb')
data = pickle.load(f)
f.close()

f = open('features_0_to_203.pkl', 'rb')
fmat = pickle.load(f)
f.close()

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

for i in range(len(data)):
    if data[i]["salary_range"]>169:
        data[i]["salary_range"] = 183
        print(data[i]["salary_range"])

for i in range(len(data)):
    fmat[i].append(data[i]["salary_range"])

print(fmat[0])
print(fmat[10])
print(fmat[20])

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

f = open('features_0_to_204.pkl', 'wb')
pickle.dump(fmat,f,-1)
f.close()
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----