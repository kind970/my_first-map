import streamlit as st
import random
st.title("나의 첫번째 앱")

st.txt('\n\n')
st.write('안녕하세요, 저는 이 계정의 관리자, charles입니다.')
st.write('저의 이메일 주소는 24_10101@daejin.sen.hs.kr입니다.')

st.button("Reset", type="primary")
if st.button("난수 생성"):
    st.write(random.randint(1,1000))
else:
    st.write('안녕')
