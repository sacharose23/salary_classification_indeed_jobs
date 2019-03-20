
# Fit Logistic Baseline Model 
from logisticmodel import logisticmodel
y_test, y_test_pred = logisticmodel()

# Evaluate Logistic Baseline Model
from evaluations import evaluations
evaluations(y_test, y_test_pred)

# Fit Logistic Modified Model
from logisticmodel2 import logisticmodel_matrixinput
y_test, y_test_pred = logisticmodel_matrixinput()

# Evaluate Logistic Modified Model
from evaluations2 import evaluations
evaluations(y_test, y_test_pred)