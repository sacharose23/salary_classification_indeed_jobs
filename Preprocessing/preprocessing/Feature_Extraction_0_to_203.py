# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# Feature Extraction
import pickle
import re

f = open('2.1_data.pkl', 'rb')
data = pickle.load(f)
f.close()

f = open('features_27+_13.pkl', 'rb')
fmat = pickle.load(f)
f.close()

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

#1
#patterns = ["nodejs", "ios", "android", "iot", "electron", "react", "linux", "macos", "watchos", "jvm", "amazon web services", "aws", "ipfs"]
#2
#patterns = ["fuse", "heroku", "raspberry pi", "qt", "webextensions", "rubymotion", "gnome", "net", "amazon alexa", "alexa", "digitalocean", "ibm"]
#3
#patterns = ["firebase", "flutter", "npm", "swift", "python", "rust", "go", "scala", "haskell", "clojure", "elixir", "elm", "erlang", "julia"]
#4
#patterns = ["lua", "git", "c", "c#", "r", "css3", "rstudio", "d", "perl", "common lisp", "groovy", "dart", "java", "kotlin", "ocaml", "coldfusion"]
#5
#patterns = ["fortran", "php", "delphi", "assembler", "autoit", "crystal", "frege", "cmake", "actionscript", "eta", "idris", "ada", "spark", "q#"]
#6
#patterns = ["es6", "css", "polymer", "angular", "backbone", "html5", "svg", "canvas", "knockoutjs", "dojo", "meteor", "bem", "flexbox", "d3"]
#7
#patterns = ["jquery", "cyclejs", "vuejs", "marionettejs", "aurelia", "charting", "ionic framework", "chrome devtools", "postcss", "draftjs"]
#8
#patterns = ["choo", "redux", "sass", "less", "webgl", "preact", "nextjs", "hyperapp", "jamstack", "flask", "docker", "vagrant", "pyramid"]
#9
#patterns = ["cakephp", "laravel", "rails", "nginx", "kubernetes", "lumen", "serverless framework", "serverless", "apache", "vertx", "terraform"]
#10
#patterns = ["vapor", "dash", "nlp", "ruby", "tensorflow", "hadoop", "vim", "sublime text", "emacs", "atom", "visual studio code", "dotfiles"]
#11
#patterns = ["plugins", "dev env", "shell", "fish", "github", "ssh", "foss", "database", "mysql", "sqlalchemy", "influxdb", "neo4j", "mongodb"]
#12
#patterns = ["rethinkdb", "tinkerpop", "postgresql", "couchdb", "hbase", "nosql", "javascript", "php", "theravada", "inspectit", "captcha"]
#13
#patterns = ["jupyter", "magento", "markdown", "chatops", "dtrace", "steam", "markov", "latex", "vulkan", "vorpal", "tap", "django", "wagtail"]
#14
patterns = ["drupal", "ux", "slack", "json", "rest", "quora", "graphql", "opengl", "katas"]


print("28 to ... Field of Study")
for i in range(len(data)):

    sentences = []
    for j in range(len(data[i]['text'])):
        for word in data[i]['text'][j].split():
            sentences.append(word)
    #print(sentences)

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
    #print()

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
print(fmat[0])
print(len(fmat[0]))

f = open('features_27+_14.pkl', 'wb')
pickle.dump(fmat,f,-1)
f.close()
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----