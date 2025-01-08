import streamlit as st
import random
st.title("나의 첫번째 앱")
st.title("랜덤 명언 생성기")

# 명언 리스트
quotes = [
    "삶이 있는 한 희망은 있다. - 키케로",
    "산다는것 그것은 치열한 전투이다. - 로망로랑",
    "하루에 3시간을 걸으면 7년 후에 지구를 한바퀴 돌 수 있다. - 사무엘존슨",
    "언제나 현재에 집중할수 있다면 행복할것이다. - 파울로 코엘료",
    "진정으로 웃으려면 고통을 참아야 하며 , 나아가 고통을 즐길 줄 알아야 해 - 찰리 채플린"
]

if st.button("명언 생성하기"):
    random_quote = random.choice(quotes)
    st.write(random_quote)

st.write("이 앱은 버튼을 클릭할 때마다 랜덤한 명언을 보여줍니다.")

