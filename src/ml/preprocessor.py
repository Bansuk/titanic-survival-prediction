import pandas as pd
import numpy as np


class PreProcessor:

    def __init__(self):
        self.preprocessor = None

    def dataclass_to_dataframe(self, data) -> pd.DataFrame:
        df = pd.DataFrame([{
            'Name': data.name,
            'Pclass': data.ticket_class,
            'Sex': data.sex,
            'Age': data.age,
            'SibSp': data.number_siblings_spouses,
            'Parch': data.number_parents_children,
            'Cabin': data.cabin,
            'Ticket': data.ticket,
            'Fare': data.fare,
            'Embarked': data.embarked
        }])
        return df

    def preprocess_new_data(self, df, pp):
        df = df.copy()

        df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)

        def fill_age(row):
            val = pp['age_medians'].get(
                (row['Sex'], row['Pclass'], row['Title'],
                 row['SibSp'], row['Parch']),
                np.nan
            )
            if pd.isnull(val):
                val = pp['age_medians_overall'].get(
                    (row['Sex'], row['Pclass']), np.nan)
            return row['Age'] if not pd.isnull(row['Age']) else val

        df['Age'] = df.apply(fill_age, axis=1)
        df = df.drop('Title', axis=1)
        df.loc[df['Embarked'].isnull() & (df['Pclass'] == 1),
               'Embarked'] = pp['embarked_mode_pclass1']
        df['HasCabin'] = df['Cabin'].notnull().astype(int)
        df['Sex'] = pp['sex_encoder'].transform(df['Sex'])

        embarked_dummies = pd.get_dummies(
            df['Embarked'], prefix='Embarked', drop_first=True)
        for col in pp['embarked_cols']:
            if col not in embarked_dummies:
                embarked_dummies[col] = 0
        embarked_dummies = embarked_dummies[pp['embarked_cols']]
        df = pd.concat([df, embarked_dummies], axis=1)
        df = df.drop(columns=['Embarked'])

        X = df.drop(columns=['PassengerId', 'Ticket', 'Name',
                    'Cabin', 'Survived'], errors='ignore')

        X_scaled = pp['scaler'].transform(X)

        return X_scaled
