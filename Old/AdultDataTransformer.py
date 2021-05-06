import pandas as pd
import numpy as np

from sklearn.base import BaseEstimator, TransformerMixin

class TransformAdultData(BaseEstimator, TransformerMixin):
    
    def __init__(self):
        self.bool_true = True
        self.object_cols = []
        self.native_country_new = None
    
    def fit(self, dataset, *args):
        df = dataset.copy()
        
        for i, enum in enumerate(df.dtypes):
            if enum=='object':
                self.object_cols.append(i)

        for i, _ in enumerate(self.object_cols):
            self.object_cols[i] = df.dtypes.index[self.object_cols[i]]
            
        
        return df
    
    
    
    def get_country(self, name):
        if name not in self.native_country_new or name=='?':
            return "Others"
        else:
            return name

    
    def change_edu_level(self, name):
        if name=="HS-grad":
            return "High School"
        elif name in ["Bachelors","Some-college"]:
            return "Bachelors"
        elif name in ["11th", "9th", "7th-8th", "5th-6th", "10th", "1st-4th", "12th", "Preschool"]:
            return "Compulsory"
        elif name in ["Assoc-acdm", "Assoc-voc"]:
            return "Associate"
        else:
            return name
    
    def correct_names(self, name):
        if name.startswith(" ") or name.endswith(" "):
            return name.strip(" ")
        else:
            return name

    
    def remove_qm(self, name):
        if name == '?':
            return 'Other-service'
        else:
            return name
    
    
    def transform(self, dataset, *args):
        df = dataset.copy()
        
        for i in self.object_cols:
            df[i] = df[i].apply(self.correct_names)
            
        if not self.native_country_new:    
            # self.native_country_new = df[df['Salary']==">50K"]['native-country'].value_counts().index[:10]
            self.native_country_new = df['native-country'].value_counts().index[:10]
        
        df['native-country'] = df['native-country'].apply(self.get_country)
                
        df['education'] = df['education'].apply(self.change_edu_level)
        
        df['workclass'] = df['workclass'].apply(self.remove_qm)
        df['occupation'] = df['occupation'].apply(self.remove_qm)
                
        return df
    
    def fit_transform(self, dataset, *args):
        if not self.object_cols:
            self.fit(dataset)
        return self.transform(dataset)