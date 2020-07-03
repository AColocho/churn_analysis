from sklearn.metrics import f1_score,accuracy_score,precision_score,recall_score
import pandas as pd
import numpy as np

def ModelCompare(algos,X_train,y_train,X_test,y_test):
    """
    Parameters:
        algos: Dictionary of all algorithms from sklearn to fit
        X_train: X training data
        y_train: y training data
        X_test: X testing data
        y_test: y testing data
    returns:
        data frame with training and testing accuracy scores and f1 scores
    """
    algo = []
    trainAccuracy = []
    testAccuracy = []
    f1Train = []
    f1Test = []

    for i in algos.keys():
        algo.append(i)
        model = algos.get(i)
        model.fit(X_train,y_train)

        train = model.predict(X_train)
        test = model.predict(X_test)

        trainAccuracy.append(accuracy_score(y_train,train))
        testAccuracy.append(accuracy_score(y_test,test))
        f1Train.append(f1_score(y_train,train))
        f1Test.append(f1_score(y_test,test))

    return pd.DataFrame({'Models':algo,'Training Accuracy':trainAccuracy,'Test Accuracy':testAccuracy,'F1 Train':f1Train,'F1 Test':f1Test})

def BenchmarkModel(algos, X_train,y_train,X_test,y_test,metrics):
    """
    Parameters:
        algos: Dictionary of all algorithms from sklearn to fit
        X_train: X training data
        y_train: y training data
        X_test: X testing data
        y_test: y testing data
        metrics: Dictionary of all metrics to run. Must take in (y_true,y_pred) in that order
    returns:
        dictionary with the name of algorithms and their metrics
    """
    benchmarks = {}
    for i in algos.keys():
        model = algos.get(i)
        model.fit(X_train,y_train)
        pred = model.predict(X_test)
        
        score = []
        for i in metrics.keys():
            scorer = metrics.get(i)
            score.append(scorer(y_test,pred))
        
        benchmarks.update({i:score})
    
    return benchmarks

def Benchmarks(y_test,pred,benchmarks):
    metrics = []
    for i in benchmarks:
        metrics.append(i(y_test,pred))
    
    return metrics