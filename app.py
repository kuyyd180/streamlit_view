import streamlit as st
print('Hello!')

view = [100, 150, 30]
st.write('# view')
st.write('## raw')
view
st.write('## bar chart')
st.bar_chart(view)
import pandas as pd
sview = pd.Series(view)
sview