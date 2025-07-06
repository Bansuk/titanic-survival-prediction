"""
Titanic model preprocessor module.

This module provides a `PreProcessor` class for transforming passenger input data
into a format suitable for prediction, including feature engineering, missing value
imputation, encoding, and scaling.
"""

import pandas as pd
import numpy as np


class PreProcessor:
    """
    PreProcessor for preparing passenger data for prediction.

    Provides methods to:
    - Convert a passenger data instance to a DataFrame.
    - Preprocess raw passenger data using pre-fitted encoders and scalers.
    - Scale the final feature set.
    """

    def __init__(self):
        self.preprocessor = None

    def dataclass_to_dataframe(self, data) -> pd.DataFrame:
        """
        Convert a PassengerData instance to a single-row DataFrame.

        Args:
            data (PassengerData): Information about the passenger.

        Returns:
            pd.DataFrame: A single-row DataFrame with passenger details.
        """
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
        """
        Perform feature engineering and preprocessing on raw passenger DataFrame.

        This includes:
        - Extracting title for age imputation.
        - Filling missing age and embarkation values.
        - Creating a 'HasCabin' feature.
        - Encoding categorical variables.
        - Adding dummy variables for embarked ports.
        - Dropping irrelevant columns.
        - Scaling numerical features.

        Args:
            df (pd.DataFrame): Raw passenger data.
            pp (dict): Dictionary containing pre-fitted encoders, scalers,
                       and other preprocessing artifacts.

        Returns:
            np.ndarray: Preprocessed and scaled feature array ready for prediction.
        """

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

        bool_cols = X.select_dtypes(include=['bool']).columns
        X[bool_cols] = X[bool_cols].astype(int)

        X_scaled = self.scale_data(X, pp)

        return X_scaled

    def scale_data(self, X, pp):
        """
        Scale the input feature DataFrame using the provided scaler.

        Args:
            X (pd.DataFrame): Feature DataFrame to scale.
            pp (dict): Dictionary containing the pre-fitted scaler.

        Returns:
            np.ndarray: Scaled feature array.
        """

        return pp['scaler'].transform(X)
