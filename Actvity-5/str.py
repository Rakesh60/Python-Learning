import streamlit as st
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3],'B':[4,5,6]})
df.set_index('A',inplace=True)
st.write(df)