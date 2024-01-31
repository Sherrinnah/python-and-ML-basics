from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#from the net
url = "https://raw.githubusercontent.com/jbrownlee/datasets/master/iris.csv"
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
dataset = read_csv(url, names=names)

#shape/number of rows and columns
print (dataset.shape)
#see details of the first 20 rows
print (dataset.head(20))
#see details of the last 5 rows
print (dataset.tail(5))
#get a summary of all statistical values of the dataset
print (dataset.describe())
#number of rows for each class
print(dataset.groupby('class').size())

#intervariant plotting(plots many variables)
dataset.plot(kind='box',subplots= True, layout=(2,2), sharex= False, sharey=False)
pyplot.show()

#plot histogram
dataset.hist()
scatter_matrix(dataset)
pyplot.show()

print("")
#SPLIT-OUT VALIDATION DATASET
array = dataset.values
x = array[:,0:4] #learn to manipulate arrays in python
y = array[:,4]
x_train,x_validation,y_train, y_validation = train_test_split(x,y, test_size=0.20, random_state=1,shuffle=True)

#spot check Algorithms 
models = []
models.append(('LR',LogisticRegression(solver='liblinear',multi_class = 'ovr')))
models.append(('LDA',LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

results=[]
names=[]
for name, model in models:
    kfold=StratifiedKFold(n_splits=10,random_state=1,shuffle=True)
    cv_results=cross_val_score(model,x_train,y_train,cv=kfold,scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    print('%s: %f(%f)' %(name,cv_results.mean(),cv_results.std()))
    
#Compare Algorithms
pyplot.boxplot(results,labels=names)
pyplot.title("ALGORITHM COMPARISON")
pyplot.show()

#Make prediction on Validation Set
model=SVC(gamma='auto')
model.fit(x_train,y_train)
predictions=model.predict(x_validation)

#evaluate predictions
print(accuracy_score(y_validation,predictions))
print(confusion_matrix(y_validation,predictions))
print(classification_report(y_validation,predictions))






