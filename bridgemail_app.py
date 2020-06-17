#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st

import numpy as np
import pandas as pd
import re


# In[3]:


st.title('-B-R-I-D-G-E-M-A-I-L-')


# In[128]:


# Import data
stranger_df = pd.DataFrame({'address': ['phillip.allen@enron.com', 'holden.salisbury@enron.com', 
                                        'darron.giron@enron.com', 'lisa.gang@enron.com'], 
                            'score': [5, 1, 4, 1]})
dict_i = {'prediction': ["recommend", "next", "quarter"]}
dict_j = {'prediction': ["validate", "model"]}


# Let the user choose a recipient from a dropdown menu
option = st.selectbox(
    "To:",
    ('', 'phillip.allen@enron.com', 'holden.salisbury@enron.com', 'darron.giron@enron.com', 'lisa.gang@enron.com'))

# Add text area
txt = st.text_area('Content:', height = 100)


# Stranger detector section
if option: 
   
    st.subheader("Stranger detector")
    
    stranger_score = int(stranger_df['score'][stranger_df['address']== option])
    st.write('Your stranger score: ' + str(stranger_score) + ' out of 5') 

    
    if (stranger_score > 3):
        # Jargon detector section and meaning section
        if txt: 

            st.subheader("Jargon detector")

            user_jargon = []
            for item in list(re.split(r'[,.\s]\s*', txt)):
                if item in ['CompanyX', 'powermarketers']: 
                    user_jargon.append(item) 

            jargon = user_jargon 
            if len(user_jargon) == 0: 
                st.write("Your email is jargon-free! Good Job!")
            else:
                st.write("Your recipient does not use the following word(s). You might want to provide definition(s) and/or context(s)", jargon)


            st.subheader("Context detector")

            to_compare_meaning = []

            for item in list(re.split(r'[,.?!\s]\s*', txt)):
                if item in ['prediction']: 
                    to_compare_meaning.append(item) 

            #to_compare_meaning = ['prediction']

            if len(to_compare_meaning) == 0: 
                st.write("We didn't find any words with potential meaning discrepancies.")
            else: 
                meaningwords_i = (dict_i.get(to_compare_meaning[0]))
                meaning_i = meaningwords_i
                meaningwords_j = (dict_j.get(to_compare_meaning[0]))
                meaning_j = meaningwords_j 
                #    word1_dict = to_compare_meaning[0]
                word1 = to_compare_meaning[0]

                st.write("You and your recipient seem to use the following word(s) differently:", word1)
                st.write("You tend to use", word1, "along with:", meaning_i)
                st.write("Your recipient tend to use", word1, "along with:", meaning_j)

send = st.button('Send')
if send:
    st.write('Message sent')



# In[ ]:




