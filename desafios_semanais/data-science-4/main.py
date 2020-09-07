#!/usr/bin/env python
# coding: utf-8

# # Desafio 6
# 
# Neste desafio, vamos praticar _feature engineering_, um dos processos mais importantes e trabalhosos de ML. Utilizaremos o _data set_ [Countries of the world](https://www.kaggle.com/fernandol/countries-of-the-world), que contém dados sobre os 227 países do mundo com informações sobre tamanho da população, área, imigração e setores de produção.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Setup_ geral

# In[47]:


import pandas as pd
import numpy as np
import seaborn as sns
import sklearn as sk
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.preprocessing import KBinsDiscretizer, Binarizer, OneHotEncoder, MinMaxScaler, StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.datasets import fetch_20newsgroups


# In[2]:


# # Algumas configurações para o matplotlib.
# %matplotlib inline

# from IPython.core.pylabtools import figsize


# figsize(12, 8)

# sns.set()


# In[2]:


countries = pd.read_csv("countries.csv")


# In[3]:


new_column_names = [
    "Country", "Region", "Population", "Area", "Pop_density", "Coastline_ratio",
    "Net_migration", "Infant_mortality", "GDP", "Literacy", "Phones_per_1000",
    "Arable", "Crops", "Other", "Climate", "Birthrate", "Deathrate", "Agriculture",
    "Industry", "Service"
]

countries.columns = new_column_names

countries.head(5)


# ## Observações
# 
# Esse _data set_ ainda precisa de alguns ajustes iniciais. Primeiro, note que as variáveis numéricas estão usando vírgula como separador decimal e estão codificadas como strings. Corrija isso antes de continuar: transforme essas variáveis em numéricas adequadamente.
# 
# Além disso, as variáveis `Country` e `Region` possuem espaços a mais no começo e no final da string. Você pode utilizar o método `str.strip()` para remover esses espaços.

# ## Inicia sua análise a partir daqui

# In[4]:


# Sua análise começa aqui.
countries.shape


# In[5]:


countries.describe()


# In[11]:


countries.notna().sum()


# ## Questão 1
# 
# Quais são as regiões (variável `Region`) presentes no _data set_? Retorne uma lista com as regiões únicas do _data set_ com os espaços à frente e atrás da string removidos (mas mantenha pontuação: ponto, hífen etc) e ordenadas em ordem alfabética.

# In[4]:


countries.replace(',', '.', regex=True, inplace=True)


# In[38]:


def q1():
    regions = [x.strip() for x in countries['Region'].unique()]
    regions.sort()
    return regions


# ## Questão 2
# 
# Discretizando a variável `Pop_density` em 10 intervalos com `KBinsDiscretizer`, seguindo o encode `ordinal` e estratégia `quantile`, quantos países se encontram acima do 90º percentil? Responda como um único escalar inteiro.

# In[57]:


def q2():
    kbd = KBinsDiscretizer(n_bins=10, encode='ordinal')
    pop_density = kbd.fit_transform(np.array(countries['Pop_density']).reshape(-1, 1))
    return int((pop_density >= 9).sum())
q2()


# # Questão 3
# 
# Se codificarmos as variáveis `Region` e `Climate` usando _one-hot encoding_, quantos novos atributos seriam criados? Responda como um único escalar.

# In[68]:


def q3():
    return countries['Region'].unique().size + countries['Climate'].unique().size
q3()


# ## Questão 4
# 
# Aplique o seguinte _pipeline_:
# 
# 1. Preencha as variáveis do tipo `int64` e `float64` com suas respectivas medianas.
# 2. Padronize essas variáveis.
# 
# Após aplicado o _pipeline_ descrito acima aos dados (somente nas variáveis dos tipos especificados), aplique o mesmo _pipeline_ (ou `ColumnTransformer`) ao dado abaixo. Qual o valor da variável `Arable` após o _pipeline_? Responda como um único float arredondado para três casas decimais.

# In[5]:


test_country = [
    'Test Country', 'NEAR EAST', -0.19032480757326514,
    -0.3232636124824411, -0.04421734470810142, -0.27528113360605316,
    0.13255850810281325, -0.8054845935643491, 1.0119784924248225,
    0.6189182532646624, 1.0074863283776458, 0.20239896852403538,
    -0.043678728558593366, -0.13929748680369286, 1.3163604645710438,
    -0.3699637766938669, -0.6149300604558857, -0.854369594993175,
    0.263445277972641, 0.5712416961268142
]


# In[29]:


def q4():
    countries_pipeline = Pipeline(steps=[("imputer", SimpleImputer(strategy="median")), ("standard_scaler", StandardScaler())])
    pipeline_transform = countries_pipeline.fit(countries[new_column_names[2:]])
    test_countries = pd.DataFrame([test_country], columns = countries.columns)
    pipeline_test = countries_pipeline.transform(test_countries[new_column_names[2:]])
    result = pd.DataFrame(pipeline_test, columns=new_column_names[2:])
    return float(result.Arable.round(3))
q4()


# ## Questão 5
# 
# Descubra o número de _outliers_ da variável `Net_migration` segundo o método do _boxplot_, ou seja, usando a lógica:
# 
# $$x \notin [Q1 - 1.5 \times \text{IQR}, Q3 + 1.5 \times \text{IQR}] \Rightarrow x \text{ é outlier}$$
# 
# que se encontram no grupo inferior e no grupo superior.
# 
# Você deveria remover da análise as observações consideradas _outliers_ segundo esse método? Responda como uma tupla de três elementos `(outliers_abaixo, outliers_acima, removeria?)` ((int, int, bool)).

# In[58]:


def q5():
    q1 = countries['Net_migration'].astype(float).quantile(0.25)
    q3 = countries['Net_migration'].astype(float).quantile(0.75)
    return (int((countries['Net_migration'].astype(float) < (q1 - 1.5 * (q3 - q1))).sum()),
            int((countries['Net_migration'].astype(float) > (q3 + 1.5 * (q3 - q1))).sum()),
            False)
q5()


# ## Questão 6
# Para as questões 6 e 7 utilize a biblioteca `fetch_20newsgroups` de datasets de test do `sklearn`
# 
# Considere carregar as seguintes categorias e o dataset `newsgroups`:
# 
# ```
# categories = ['sci.electronics', 'comp.graphics', 'rec.motorcycles']
# newsgroup = fetch_20newsgroups(subset="train", categories=categories, shuffle=True, random_state=42)
# ```
# 
# 
# Aplique `CountVectorizer` ao _data set_ `newsgroups` e descubra o número de vezes que a palavra _phone_ aparece no corpus. Responda como um único escalar.

# In[48]:


categories = ['sci.electronics', 'comp.graphics', 'rec.motorcycles']
newsgroup = fetch_20newsgroups(subset="train", categories=categories, shuffle=True, random_state=42)


# In[54]:


def q6():
    count_vectorizer = CountVectorizer()
    newsgroup_counts = count_vectorizer.fit_transform(newsgroup.data)
    words = pd.DataFrame(newsgroup_counts.toarray(), columns=count_vectorizer.get_feature_names())
    return int(words['phone'].sum())
q6()


# ## Questão 7
# 
# Aplique `TfidfVectorizer` ao _data set_ `newsgroups` e descubra o TF-IDF da palavra _phone_. Responda como um único escalar arredondado para três casas decimais.

# In[55]:


def q7():
    tfidf_vectorizer = TfidfVectorizer()
    newsgroups_tfidf_vectorized = tfidf_vectorizer.fit_transform(newsgroup.data)
    newsgroups_tfidf = pd.DataFrame(newsgroups_tfidf_vectorized.toarray(), columns=tfidf_vectorizer.get_feature_names())
    return float(round(newsgroups_tfidf['phone'].sum(), 3))
q7()


# In[ ]:




