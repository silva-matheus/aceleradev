#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[18]:


import pandas as pd
import numpy as np


# In[19]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[ ]:


black_friday.info()


# In[ ]:


black_friday.describe()


# In[88]:


black_friday.head(20)


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[ ]:


def q1():
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[ ]:


def q2():
    return int(((black_friday['Age'] == '26-35') & (black_friday['Gender'] == 'F')).sum())


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[ ]:


def q3():
    return black_friday['User_ID'].nunique()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[30]:


def q4():
    return int(black_friday.dtypes.value_counts().count())


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[29]:


def q5():
    return float(black_friday.isnull().any(axis=1).sum() / black_friday.shape[0])


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[28]:


def q6():
    return int(black_friday.isna().sum().max())


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[31]:


def q7():
    return black_friday['Product_Category_3'].mode().loc[0]


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[25]:


def q8():
    normalized_df = (black_friday['Purchase'] - black_friday['Purchase'].min())                                 / (black_friday['Purchase'].max() - black_friday['Purchase'].min())
    return float(normalized_df.mean()) 


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[26]:


def q9():
    aux_df = (black_friday['Purchase'] - black_friday['Purchase'].mean()) / black_friday['Purchase'].std()
    return int(((aux_df >= -1) & (aux_df <= 1)).sum())


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[9]:


def q10():
    return True if black_friday[(black_friday['Product_Category_2'].isna())
        & (black_friday['Product_Category_3'].isna())].shape[0] \
        == black_friday[(black_friday['Product_Category_2'].isna())].shape[0] else False


# In[ ]:




