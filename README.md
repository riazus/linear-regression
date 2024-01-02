# Subject
The objective is to implement a simple linear regression with a single feature, from scratch. The choice of programming language is free, but should suitable for visualizing data. Using librairies is authorized, except for the ones that does all the work. For example, using python’s numpy.polynomial() function or scikit-learn library would be considered as cheating.

Dataset to train
Monovariate : Car mileage as inputs, car price as output [data.csv](./data.csv)

### Mandatory Part

A **first program** `mileage.py` is predicting the price of a car for a given mileage. The prediction is based on the following model **hypothesis** :

`estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)`

Parameters **thetas** are set to 0 by default, if training did not occur yet.

A **second program** `linear_regression.py` is training the model, from a ```data.csv``` train set. According to the hypothesis, both parameters **thetas** are updated with **gradient-descent** algorithm.

The two programs cannot directly communicate. Model parameters issued from training dataset, should be stored and be accessible independently of runtime (**Data persistency**).

### Bonus part

• Plotting the data into a graph to see repartition.

• Plotting the line resulting from linear regression training into the same graph.

• Calculating the precision of the implemented algorithm.

• Any feature that is making sense  

# Usage
- `make training` - trains model and save thetas
- `make data` - shows data on the graph
- `make line` - plots the line from linear regression
- `make precise` - makes precision
- `make predict` - executes the first program and predicts the price
- `make clean` - cleans thetas.txt 
