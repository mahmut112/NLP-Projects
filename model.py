#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd

import xgboost as xgb
from xgboost import XGBClassifier

from sklearn import metrics
from sklearn.metrics import precision_score, recall_score, accuracy_score, roc_auc_score

from sklearn.metrics import confusion_matrix, f1_score
from sklearn.model_selection import GridSearchCV, train_test_split,cross_val_score

import matplotlib.pyplot as plt

def modelfit(alg, dtrain, predictors,useTrainCV=True, cv_folds=5, early_stopping_rounds=100):
    
    if useTrainCV:
        xgb_param = alg.get_xgb_params()
        xgtrain = xgb.DMatrix(dtrain[predictors].values, label=dtrain["point"].values)
        cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=alg.get_params()['n_estimators'], nfold=cv_folds,
            metrics='auc', early_stopping_rounds=early_stopping_rounds, verbose_eval = True)
        alg.set_params(n_estimators=cvresult.shape[0])
    
    
    alg.fit(dtrain[predictors], dtrain['point'],eval_metric='auc')
        
    
    dtrain_predictions = alg.predict(dtrain[predictors])
    dtrain_predprob = alg.predict_proba(dtrain[predictors])
        
    
    print("\nModel Report")
    print ("Accuracy : %.4g" % accuracy_score(dtrain['point'].values, dtrain_predictions))
    print ("AUC Score (Train): %f" % roc_auc_score(dtrain['point'], dtrain_predprob ,multi_class='ovo',average='weighted'))
    
    print("Precision Score : ",precision_score(dtrain['point'],dtrain_predictions,average='weighted'))
    print("Recall Score :" , recall_score(dtrain['point'], dtrain_predictions, average='weighted') )
    
    
    print("f1_score :", f1_score(dtrain["point"], dtrain_predictions, average='weighted'))
    
    feat_imp = pd.Series(alg.feature_importances_)
    
    
    feat_imp.plot(kind='bar', title='Feature Importances')
    plt.ylabel('Feature Importance Score')


# In[10]:


predictors = [x for x in df_tra_na.columns if x not in ["point"] ]
xgb1 = XGBClassifier(
 learning_rate =0.1,
 num_class=3,
 n_estimators=1000,
 max_depth=5,
 min_child_weight=1,
 gamma=0,
 subsample=0.8,
 colsample_bytree=0.8,
 objective= 'multi:softprob',
 nthread=4,
 scale_pos_weight=1,
 seed=27)
modelfit(xgb1, df_tra_na, predictors)


# In[ ]:


from sklearn.metrics import precision_score, recall_score, accuracy_score, roc_auc_score, confusion_matrix, f1_score

print ("Accuracy : %.4g" % accuracy_score(y_test, test_prediction))
print ("AUC Score (Train): %f" % roc_auc_score(y_test, test_predictionproba ,multi_class='ovo',average='weighted'))
print ("f1_score : %f"%f1_score(y_test,test_prediction,average="macro"))


# In[ ]:


import pickle

pickle.dump(xgb1, open(get_absolute_path("models_params","model.pickle"), "wb"))


# In[ ]:


import pickle
from preprocces.helper import get_absolute_path

xgb_model_loaded = pickle.load(open(get_absolute_path("models_params","model.pickle"), "rb"))


# In[ ]:


test_prediction = xgb_model_loaded.predict(x_test)
test_predictionproba = xgb_model_loaded.predict_proba(x_test)

