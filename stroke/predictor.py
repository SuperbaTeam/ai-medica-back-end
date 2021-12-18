import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")
pd.set_option("display.max_colwidth", None)
pd.set_option("max_rows", None)

from sklearn.preprocessing import LabelBinarizer
from sklearn.impute import SimpleImputer
from sklearn.utils import resample
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


class AIModel:
    def __init_(self):
        self.Dataset = None

    def reading_dataset(self):
        self.Dataset = pd.read_csv("assets/stroke.csv")
        self.Dataset = self.Dataset.drop(["id"], axis=1)

    def data_encoding(self):
        one_hot_encoder = LabelBinarizer()

        self.Dataset["gender"] = self.Dataset["gender"].apply(
            lambda x: 1 if x == "Male" else (0 if x == "Female" else np.nan)
        )
        self.Dataset["Residence_type"] = self.Dataset["Residence_type"].apply(
            lambda x: 1 if x == "Urban" else (0 if x == "Rural" else np.nan)
        )
        self.Dataset["ever_married"] = self.Dataset["ever_married"].apply(
            lambda x: 1 if x == "Yes" else (0 if x == "No" else np.nan)
        )

        smoking_status = self.Dataset["smoking_status"]
        smoking_status_encoded = one_hot_encoder.fit_transform(smoking_status)
        self.Dataset["smoking_Unknown"] = smoking_status_encoded[:, 0]
        self.Dataset["smoking_formerly_smoked"] = smoking_status_encoded[:, 1]
        self.Dataset["smoking_never_smoked"] = smoking_status_encoded[:, 2]
        self.Dataset["smoking_smokes"] = smoking_status_encoded[:, 3]
        self.Dataset = self.Dataset.drop(["smoking_status"], axis=1)

        work_type = self.Dataset["work_type"]
        work_type_encoded = one_hot_encoder.fit_transform(work_type)
        self.Dataset["work_Govt_job"] = work_type_encoded[:, 0]
        self.Dataset["work_Never_worked"] = work_type_encoded[:, 1]
        self.Dataset["work_Private"] = work_type_encoded[:, 2]
        self.Dataset["work_Self-employed"] = work_type_encoded[:, 3]
        self.Dataset["work_children"] = work_type_encoded[:, 4]
        self.Dataset = self.Dataset.drop(["work_type"], axis=1)

        self.Dataset = self.Dataset[
            [
                "age",
                "bmi",
                "avg_glucose_level",
                "gender",
                "ever_married",
                "Residence_type",
                "heart_disease",
                "hypertension",
                "smoking_Unknown",
                "smoking_formerly_smoked",
                "smoking_never_smoked",
                "smoking_smokes",
                "work_Govt_job",
                "work_Never_worked",
                "work_Private",
                "work_Self-employed",
                "work_children",
                "stroke",
            ]
        ]

    def data_imputing(self):
        imp2 = SimpleImputer(strategy="mean")

        age = self.Dataset["age"]
        age = np.array(age)
        age = age.reshape(-1, 1)
        age_imputed = imp2.fit_transform(age)
        self.Dataset["age"] = age_imputed

        bmi = self.Dataset["bmi"]
        bmi = np.array(bmi)
        bmi = bmi.reshape(-1, 1)
        bmi_imputed = imp2.fit_transform(bmi)
        self.Dataset["bmi"] = bmi_imputed

        avg_glucose_level = self.Dataset["avg_glucose_level"]
        avg_glucose_level = np.array(avg_glucose_level)
        avg_glucose_level = avg_glucose_level.reshape(-1, 1)
        avg_glucose_level_imputed = imp2.fit_transform(avg_glucose_level)
        self.Dataset["avg_glucose_level"] = age_imputed

        gender = self.Dataset["gender"]
        gender = np.array(gender)
        gender = gender.reshape(-1, 1)
        gender_imputed = imp2.fit_transform(gender)
        self.Dataset["gender"] = gender_imputed

    def outlires_dealing(self):
        guilty = self.Dataset["avg_glucose_level"]

        guilty = np.array(guilty)

        q25, q75 = np.percentile(guilty, [25, 75])
        inter_quartile_range = q75 - q25
        l = q25 - (inter_quartile_range * 1.5)  # l : lower boundary
        u = q75 + (inter_quartile_range * 1.5)
        index_of_outlier = np.where((guilty > u) | (guilty < l))
        index_of_outlier = index_of_outlier[0]
        not_guilty_avg_glucose_level = np.delete(guilty, index_of_outlier, axis=0)
        self.Dataset["avg_glucose_level"][0:5110] = not_guilty_avg_glucose_level

    def data_sampling(self):
        df_majority = self.Dataset[self.Dataset.iloc[:, 17] == 1]
        df_minority = self.Dataset[self.Dataset.iloc[:, 17] == 0]
        df_majority_downsampled = resample(df_majority, replace=False, n_samples=249)
        df_minority_upsampled = resample(df_minority, replace=True, n_samples=249)
        self.Dataset = pd.concat([df_majority_downsampled, df_minority_upsampled])

    def data_splitting(self):
        features = self.Dataset.drop(["stroke"], axis=1)
        target = self.Dataset["stroke"]
        X_train, X_test, y_train, y_test = train_test_split(
            features,
            target,
            test_size=0.15,
        )
        return X_train, X_test, y_train, y_test

    def predict(self, data):
        self.reading_dataset()
        self.data_encoding()
        self.data_imputing()
        self.outlires_dealing()
        self.data_sampling()
        X_train, X_test, y_train, y_test = self.data_splitting()
        model = LogisticRegression(C=0.01, penalty="l2", random_state=1)
        model = model.fit(X_train, y_train)
        return model.predict([data])
