import streamlit as st
import openai

st.title("GPT-4.1-mini 챗봇 웹앱")

# 1. API 키 입력 (비밀번호 형태)
api_key = st.text_input("OpenAI API Key를 입력하세요:", type="password")

# 2. 질문 입력
question = st.text_input("질문을 입력하세요:")

# 3. 요청 버튼
if st.button("질문하기"):
    if not api_key:
        st.warning("API Key를 입력해주세요.")
    elif not question:
        st.warning("질문을 입력해주세요.")
    else:
        try:
            # API 키 세팅
            openai.api_key = api_key
            
            # 최신 openai 라이브러리 호출 형식
            response = openai.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": question}]
            )
            
            answer = response.choices[0].message.content
            st.success("응답:")
            st.write(answer)
        except Exception as e:
            st.error(f"에러 발생: {e}")
