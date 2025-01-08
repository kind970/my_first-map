import streamlit as st
import random
st.title("나의 첫번째 앱")
# 사용자 정의 CSS 스타일 적용
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        font-size: 16px;
    }
    .quote-text {
        font-size: 24px;
        font-style: italic;
        color: #333;
        margin: 20px 0;
    }
    .author {
        font-size: 18px;
        color: #666;
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)
st.title("랜덤 명언 생성기")

# 명언 리스트
quotes = [
    "삶이 있는 한 희망은 있다. - 키케로",
    "산다는것 그것은 치열한 전투이다. - 로망로랑",
    "하루에 3시간을 걸으면 7년 후에 지구를 한바퀴 돌 수 있다. - 사무엘존슨",
    "언제나 현재에 집중할수 있다면 행복할것이다. - 파울로 코엘료",
    "진정으로 웃으려면 고통을 참아야 하며 , 나아가 고통을 즐길 줄 알아야 해 - 찰리 채플린",
    "성공으로 가는 엘리베이터는 고장입니다. 당신은 계단을 이용해야만 합니다. 한계단 한계단씩 – 조 지라드",
    "먹고 싶은것을 다 먹는 것은 그렇게 재미있지 않다 . 인생을 경계선 없이 살면 기쁨이 덜하다 . 먹고싶은대로 다 먹을 수있다면 먹고싶은 것을 먹는데 무슨 재미가 있겠나 – 톰행크스",
    "인생을 다시 산다면 다음번에는 더 많은 실수를 저지르리라 – 나딘 스테어",
    " 문제는 목적지에 얼마나 빨리 가느내가 아니라 그 목적지가 어디냐는 것이다. -메이벨 뉴컴버",
    "You are never too old to set another goal or to dream a new dream. -c.s루이스",
    " The best revenge is massive success. -프랭크 시나트라"
]

if st.button("명언 생성하기"):
    random_quote = random.choice(quotes)
    st.write(random_quote)

st.write("이 앱은 버튼을 클릭할 때마다 랜덤한 명언을 보여줍니다.")

