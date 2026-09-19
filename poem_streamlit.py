import streamlit as st
import time
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

st.title("_AI 시인_ :sunglasses:") #_xx_ 는 italic 체를 의미
title = st.text_input("시의 주제를 입력하세요", "단풍")
st.write("시의 주제 : ", title)

if st.button("시 작성"):
    with st.spinner("Wait for it..."):#, show_time=True):
        # time.sleep(5)
    #st.success("Done!")
    
        #llm 작성
        model = init_chat_model(
        "gpt-5.5",
        # Kwargs passed to the model:
        # temperature=0.7, #GPT 5.5 이상에서는 temperature 사용 못함
        timeout=120,
        max_tokens=1000,
        max_retries=6,  # Default; increase for unreliable networks
        api_key = api_key
        )

        #프롬프트 작성
        prompt = ChatPromptTemplate.from_messages([
        ('system',"당신은 친절하고 유용한 AI 어시스턴트입니다."),
        ('user',"{input}")
        ])

        #output + chain
        output_parser = StrOutputParser()
        chain = prompt | model | output_parser

        #chain.invoke + response 출력
        response = chain.invoke({"input":title+"에 대한 시를 써줘"})
        # print(response)
        st.write(title)
        st.write(response)
