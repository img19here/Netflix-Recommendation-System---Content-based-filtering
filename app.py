import pandas as pd
import pickle
import streamlit as st


import os
print(os.listdir("."))

movies = pickle.load(open('movies_dict.pkl' , mode = 'rb'))