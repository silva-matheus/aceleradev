import pandas as pd
import numpy as np
import requests
from sklearn import linear_model, ensemble, svm, tree, preprocessing

##################### Tranforming Categorical Features in Numerical Features #####################

def categorical_to_dummy(data):
    for category in categorical:
        df_encoded = pd.get_dummies(data[category], prefix=category)
        data = pd.concat([data, df_encoded], axis=1)
    data = data.drop(labels=categorical, axis=1)
    return data

##################### Replacing NaN values with the column's median #####################

def nan_to_median(clean_data, heads):
    for head in heads:
        clean_data[head] = clean_data[head].fillna(clean_data[head].median())    
    return clean_data

##################### Loading Datasets #####################

df_train = pd.read_csv('train.csv').fillna(0)
df = pd.read_csv('test.csv').fillna(0)

# df_train = pd.read_csv('train.csv')
# df = pd.read_csv('test.csv')


##################### Defining the Features #####################

cols = [
    # 'NU_INSCRICAO',

    'CO_UF_RESIDENCIA',
    'TP_ST_CONCLUSAO',
    'TP_PRESENCA_CN',
    'TP_PRESENCA_CH',
    'TP_PRESENCA_LC',
    'CO_PROVA_CN',
    'CO_PROVA_CH',
    'CO_PROVA_LC',
    'CO_PROVA_MT',
    'TP_SEXO',
    'Q001',
    'Q002',
    'Q006',
    'Q024',
    'Q025',
    'Q026',
    'Q027',
    'Q047',
    'NU_IDADE',
    'TP_COR_RACA',
    'TP_ANO_CONCLUIU',
    'TP_ESCOLA',
    'TP_ENSINO',
    'IN_TREINEIRO',
    'TP_DEPENDENCIA_ADM_ESC',
    'IN_BAIXA_VISAO',
    'IN_CEGUEIRA',
    'IN_SURDEZ',
    'IN_DISLEXIA',
    'IN_DISCALCULIA',
    'IN_SABATISTA',
    'IN_GESTANTE',
    'IN_IDOSO',
    'NU_NOTA_CN',
    'NU_NOTA_LC',
    'NU_NOTA_CH',
    'NU_NOTA_REDACAO'
]

categorical = [
    # 'NU_INSCRICAO',

    'TP_SEXO',
    'CO_PROVA_CN',
    'CO_PROVA_CH',
    'CO_PROVA_LC',
    'CO_PROVA_MT',
    'Q001',
    'Q002',
    'Q006',
    'Q024',
    'Q025',
    'Q026',
    'Q027',
    'Q047',
]

##################### Defining Test and Training Datasets #####################

x = df_train[cols]
x_test = df[cols]

y = df_train['NU_NOTA_MT']
# y = df_train['NU_NOTA_MT'].fillna(df_train['NU_NOTA_MT'].median())

##################### Combining the datasets for preprocessing #####################

x['test'] = 0
x_test['test'] = 1
combined = pd.concat([x, x_test])
combined['MEDIA_NOTAS'] = (combined['NU_NOTA_CN'] + combined['NU_NOTA_LC'] + combined['NU_NOTA_CH'] + combined['NU_NOTA_REDACAO'])/4

##################### Preprocessing Data #####################

combined = categorical_to_dummy(combined)
# combined = nan_to_median(combined, combined.head())

##################### Spliting datasets again #####################

x = combined[combined['test'] == 0]
x_test = combined[combined['test'] == 1]
del x['test']
del x_test['test']

##################### Regressions #####################

# Linear Regressor
# lm = linear_model.LinearRegression(normalize=True)
# model = lm.fit(x, y)
# print(lm.score(x, y))

# Tree Based Regressor
# tree_regressor = tree.DecisionTreeRegressor()
# model = tree_regressor.fit(x, y)
# print(tree_regressor.score(x, y))

# Random Forest Regressor
ensemble_regressor = ensemble.RandomForestRegressor(n_estimators=500)
model = ensemble_regressor.fit(x, y)
print(ensemble_regressor.score(x, y))

# SVM Regressor
# svm_regression = svm.SVR()
# model = svm_regression.fit(x, y)
# print(svm_regression.score(x, y))

# Gradient Boost Regressor
# gradient_boost_regressor = ensemble.GradientBoostingRegressor(n_estimators=250)
# model = gradient_boost_regressor.fit(x, y)
# print(gradient_boost_regressor.score(x, y))

##################### Predictions #####################

# Linear Regression Predict
# predictions = lm.predict(x_test)

# Tree Based Prediction
# predictions = tree_regressor.predict(x_test)

# Random Forest Predict
predictions = ensemble_regressor.predict(x_test)

# SVM Predict
# predictions = svm_regression.predict(x_test)

# Gradient Boost Predict
# predictions = gradient_boost_regressor.predict(x_test)

##################### Preparing the output file #####################

df['NU_NOTA_MT'] = predictions
df_answer = df[['NU_INSCRICAO', 'NU_NOTA_MT']]

##################### Output File #####################

df_answer.to_csv('answer.csv', index=False)
