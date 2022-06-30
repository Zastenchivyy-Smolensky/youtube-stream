import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image
st.title("Stremlit入門")

st.write("Display Image")

"Start!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)
"Done!!"

left_column, right_column = st.beta_columns(2)

button = left_column.button("右からむに表示")

if button:
    right_column.write("ここは右からむ")


expander = st.beta_expander('問い合わせ')
expander.write("問い合わせ内容を書く")

# text = st.text_input("あなたの趣味を教えてください")


# condition = st.slider("あなたの今の調子は?",0,100,50)
# "あなたの好きな趣味は",text,"です"
# "コンディション",condition

# if st.checkbox("show image"):
#     img=Image.open("sample.jpeg")
#     st.image(img, caption="sample", use_column_width=True)



