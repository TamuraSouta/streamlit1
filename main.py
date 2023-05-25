from cgitb import text
from multiprocessing import Condition
from socket import fromfd
from turtle import right
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
#streamlit使い方
"""
# 最初すること
```python
streamlit run main.py
```
"""

st.title("aaaaa")

st.write("dataFream")

df = pd.DataFrame({
    "一列目":[1,2,3,4],
    "二列目":[10,20,30,40]
})

st.write(df)
#表のサイズを調整できる
st.dataframe(df,width=100,height=100)
#表の最大値を色付けできる
st.dataframe(df.style.highlight_max(axis=0))
#静的なデータを表示したい時
st.table(df.style.highlight_max(axis=0))

#マークダウン
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

#グラフの表示
df = pd.DataFrame(
    np.random.rand(20,3),
    columns=["a","b","c"]
)
st.line_chart(df,width=100,height=100)
st.area_chart(df,width=100,height=100)

#マップの表示
df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.60,139.70],
    columns=["lat","lon"]
)
st.map(df)

#画像表示
img = Image.open("お酒1.jpeg")
st.image(img,caption="osake",use_column_width=True)

#チェックボックス
if st.checkbox("show image"):
    img = Image.open("お酒1.jpeg")
    st.image(img,caption="osake",use_column_width=True)

#セレクトボックス
option = st.selectbox(
    "あなたの好きな数字を教えてください",
    list(range(1,11))
)
"あなたの好きな数字は",option,"です"



#テキスト表示
text = st.sidebar.text_input(
    "あなたの好きな趣味を教えてください"
)
"あなたの好きな趣味は",text,"です"

Condition = st.sidebar.slider(
    "あなたの好きな趣味を教えてください",0,100,50
)
"あなたの好きな趣味は",Condition,"です"

st.write("プログレスバーの表示")
"start"
latest_ireration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_ireration.text(f"Itelation {i}")
    bar.progress(i+1)
    time.sleep(0.1
)

st.write("プログレスバーの表示")
left_columns,right_colums = st.columns(2)
button = left_columns.button("右colum")
if button:
    right_colums.write("ここはからむ")

expander = st.beta_expander("問い合わせ")
expander.write("問い合わせ内容を各")