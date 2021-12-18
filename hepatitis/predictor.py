import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

np.random.seed(10)


class AIModel:
    def __init_(self):
        self.Dataset = None

    def reading_dataset(self):
        self.Dataset = pd.read_csv("assets/hepatitis.csv")

    def data_encoding(self):
        self.Dataset["sex"] = self.Dataset["sex"].apply(
            lambda x: 1 if x == "male" else (0 if x == "female" else np.nan)
        )
        self.Dataset["steroid"] = self.Dataset["steroid"].apply(
            lambda x: 1 if x == True else (0 if x == False else np.nan)
        )
        self.Dataset["antivirals"] = self.Dataset["antivirals"].apply(
            lambda x: 1 if x == True else (0 if x == False else np.nan)
        )
        self.Dataset["fatigue"] = self.Dataset["fatigue"].apply(
            lambda x: 1 if x == True else (0 if x == False else np.nan)
        )
        self.Dataset["malaise"] = self.Dataset["malaise"].apply(
            lambda x: 1 if x == True else (0 if x == False else np.nan)
        )
        self.Dataset["anorexia"] = self.Dataset["anorexia"].apply(
            lambda x: 1 if x == True else (0 if x == False else np.nan)
        )
        self.Dataset["liver_big"] = self.Dataset["liver_big"].apply(
            lambda x: 1 if x == True else (0 if x == False else np.nan)
        )
        self.Dataset["liver_firm"] = self.Dataset["liver_firm"].apply(
            lambda x: 1 if x == True else (0 if x == False else np.nan)
        )
        self.Dataset["spleen_palpable"] = self.Dataset["spleen_palpable"].apply(
            lambda x: 1 if x == True else (0 if x == "B" else np.nan)
        )
        self.Dataset["spiders"] = self.Dataset["spiders"].apply(
            lambda x: 1 if x == True else (0 if x == False else np.nan)
        )
        self.Dataset["ascites"] = self.Dataset["ascites"].apply(
            lambda x: 1 if x == True else (0 if x == False else np.nan)
        )
        self.Dataset["varices"] = self.Dataset["varices"].apply(
            lambda x: 1 if x == True else (0 if x == False else np.nan)
        )
        self.Dataset["histology"] = self.Dataset["histology"].apply(
            lambda x: 1 if x == True else (0 if x == False else np.nan)
        )
        self.Dataset["class"] = self.Dataset["class"].apply(
            lambda x: 1 if x == "live" else (0 if x == "die" else np.nan)
        )

    def data_imputing(self):
        imp1 = SimpleImputer(strategy="mean")
        self.Dataset[["bilirubin"]] = imp1.fit_transform(self.Dataset[["bilirubin"]])
        self.Dataset[["alk_phosphate"]] = imp1.fit_transform(
            self.Dataset[["alk_phosphate"]]
        )
        self.Dataset[["sgot"]] = imp1.fit_transform(self.Dataset[["sgot"]])
        self.Dataset[["albumin"]] = imp1.fit_transform(self.Dataset[["albumin"]])
        self.Dataset[["protime"]] = imp1.fit_transform(self.Dataset[["protime"]])
        imp2 = SimpleImputer(strategy="most_frequent")
        self.Dataset[["steroid"]] = imp2.fit_transform(self.Dataset[["steroid"]])
        self.Dataset[["antivirals"]] = imp2.fit_transform(self.Dataset[["antivirals"]])
        self.Dataset[["fatigue"]] = imp2.fit_transform(self.Dataset[["fatigue"]])
        self.Dataset[["malaise"]] = imp2.fit_transform(self.Dataset[["malaise"]])
        self.Dataset[["anorexia"]] = imp2.fit_transform(self.Dataset[["anorexia"]])
        self.Dataset[["liver_big"]] = imp2.fit_transform(self.Dataset[["liver_big"]])
        self.Dataset[["liver_firm"]] = imp2.fit_transform(self.Dataset[["liver_firm"]])
        self.Dataset[["spleen_palpable"]] = imp2.fit_transform(
            self.Dataset[["spleen_palpable"]]
        )
        self.Dataset[["spiders"]] = imp2.fit_transform(self.Dataset[["spiders"]])
        self.Dataset[["ascites"]] = imp2.fit_transform(self.Dataset[["ascites"]])
        self.Dataset[["varices"]] = imp2.fit_transform(self.Dataset[["varices"]])
        self.Dataset[["histology"]] = imp2.fit_transform(self.Dataset[["histology"]])

    def data_splitting(self):
        features = self.Dataset.drop(["class"], axis=1)
        target = self.Dataset["class"]
        

        
        x_train, x_test, y_train, y_test = train_test_split(
            features, target, test_size=0.25, stratify=target, random_state=1
        )
        return x_train, x_test, y_train, y_test

    def predict(self, data):
        self.reading_dataset()
        self.data_encoding()
        self.data_imputing()
        x_train, x_test, y_train, y_test = self.data_splitting()
        std = StandardScaler()
        pca = PCA(n_components=0.99)
        knn = KNeighborsClassifier(n_neighbors=4, n_jobs=-1)
        x_train_std = std.fit_transform(x_train)
        x_test_std = std.transform(x_test)
        features_reduced = pca.fit_transform(x_train_std)
        x_test = pca.transform(x_test_std)
        model = knn.fit(features_reduced, y_train)
        return model.predict([data])

'''''
instance = AIModel()
#sample=[0,0,1,0,1,1,1,10,11,125,5,5,5,6,29,4,16,67,      ]
print(instance.predict(sample))
'''
