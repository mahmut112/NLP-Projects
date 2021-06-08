import pandas as pd 
import numpy as np

from preprocces.helper import get_absolute_path
from preprocces.tokenizer import stopwords_punc
from preprocces.text_cleaner import cleaner

from sklearn.model_selection import train_test_split




class pre_data():
    def __init__(self, path:str):
        self.cleaner = cleaner()
        self.df = pd.read_csv(path,decimal=",")        
        
    def label_to_str(self, class_name:str):
        
        self.df[class_name].astype(float)
        conditions = [(self.df["point"] >= 0) & (self.df["point"] < 2), (self.df["point"] >= 2) & (self.df["point"] < 3), (self.df["point"] >= 3) & (self.df["point"] <= 5)]
        choices = ["0", "1", "2"]
        res = np.select(conditions, choices)
        self.df["point"] = res
        self.df.drop("film_name",axis=1,inplace=True)
        
        return self.df
    
    def clean_stopwords(self, dataframe, class_name:str):
        clean_texts = [self.cleaner.clean(i) for i in dataframe[class_name]]
        stop_data = [stopwords_punc(i) for i in clean_texts]
        self.df["comment"] = stop_data
        return self.df
    
    def train_valid_test_split(self, train, test):
        X_train, X_test, y_train, y_test = train_test_split(train, test, 
                                                        train_size=0.67, 
                                                        random_state=42,
                                                        stratify=test)

        X_test, X_valid, y_test, y_valid = train_test_split(X_test, y_test, 
                                                        train_size=0.5, 
                                                        random_state=42,
                                                        stratify=y_test)
        
        train = pd.concat([X_train, y_train], axis=1, join="inner")
        valid = pd.concat([X_valid, y_valid], axis=1, join="inner")
        test = pd.concat([X_test, y_test], axis=1, join="inner")

        return train, valid, test


