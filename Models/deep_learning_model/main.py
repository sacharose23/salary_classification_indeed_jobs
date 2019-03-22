import numpy
import pandas
df = pandas.read_csv('NN_pred_true_values.csv')
df = numpy.asarray(df)
y_test = df[:,1]
y_test_pred = df[:,0] 

# Evaluate Deep Learning
from evaluations import evaluations
evaluations(y_test, y_test_pred)
