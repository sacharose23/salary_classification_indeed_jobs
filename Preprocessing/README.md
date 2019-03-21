# Data Details

Creator : @PySastha

Editor : @sacharose23

## Data Dictionary

##### File name : data/data_dictionary.pkl

| Key          | Value Description                                            |
| ------------ | ------------------------------------------------------------ |
| job_title    | string of job title searched under                           |
| city         | string of job location                                       |
| salary_range | float of salary range for job                                |
| primary_key  | string url of source of job post                             |
| unique       | boolean (unique in scraping process)                         |
| text         | array of strings tokenized by lines preprocessing to be lowercase without punctuations |



## Data Matrix

##### File name : data/data_matrix.pkl

### Rows : 

* Each row corresponds to each job posting.

### Columns :

Col 0: city

Col 1: job title

Col 2: years of experience

Col 3: bachelors

Col 4: masters

Col 5: phd

Col 6: computer science

Col 7: computer engineering

Col 8: software engineering

Col 9: web development

Col 10: web design

Col 11: information systems

Col 12: information technology

Col 13: system administration

Col 14: mathematics

Col 15: statistics

Col 16: engineering

Col 17: civil

Col 18: electrical

Col 19: mechanical

Col 20: business

Col 21: accounting

Col 22: finance

Col 23: marketing

Col 24: science

Col 25: biology

Col 26: chemistry

Col 27: physics


Col 28-202 (list of technologies) : 

[ nodejs, Ios, android, Iot, electron, react, linux, macos, watchos, jvm, amazon web services, aws, ipfs, fuse, heroku, raspberry pi, qt, webextensions, rubymotion, gnome, net, amazon alexa, alexa, digitalocean, ibm, firebase, flutter, npm, swift, python, rust, go, scala, haskell, clojure, elixir, elm, erlang, julia, lua, git, c, c#, r, css3, rstudio, d, perl, common lisp, groovy, dart, java, kotlin, ocaml, coldfusion, fortran, php, delphi, assembler, autoit, crystal, frege, cmake, actionscript, eta, idris, ada, spark, q#, es6, css, polymer, angular, backbone, html5, svg, canvas, knockoutjs, dojo, meteor, bem, flexbox, d3, jquery, cyclejs, vuejs, marionettejs, aurelia, charting, ionic framework, chrome devtools, postcss, draftjs, choo, redux, sass, less, webgl, preact, nextjs, hyperapp, jamstack, flask, docker, vagrant, pyramid, cakephp, laravel, rails, nginx, kubernetes, lumen, serverless framework, serverless, apache, vertx, terraform, vapor, dash, nlp, ruby, tensorflow, hadoop, vim, sublime text, emacs, atom, visual studio code, dotfiles, plugins, dev env, shell, fish, github, ssh, foss, database, mysql, sqlalchemy, influxdb, neo4j, mongodb, rethinkdb, tinkerpop, postgresql, couchdb, hbase, nosql, javascript, php, theravada, inspectit, captcha, jupyter, magento, markdown, chatops, dtrace, steam, markov, latex, vulkan, vorpal, tap, django, wagtail, drupal, ux, slack, json, rest, quora, graphql, opengl, katas ]

Col 203: salary range