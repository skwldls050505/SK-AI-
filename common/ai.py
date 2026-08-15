from groq import Groq
import streamlit as st
from dotenv import load_dotenv
from .constants import ROLE

#client는 인터넷 통신할 때 사용하는 용어
@st.cache_resource # 싱글톤 디자인 패턴 적용 
def get_client():
    load_dotenv() #.env 파일에 등록된 데이터 환경변수에 저장하는 함수
    return Groq()


def get_msg_of_ai(user_input:str, model_name:str="openai/gpt-oss-120b") -> str :

    messages =[
        {
        "role":history['role'].name, 
        "content":history['msg']
        } for history in st.session_state.history
    ]
    # t사용자 메세지 추가

    messages.append({
        "role" : ROLE.user.name, 
        "content": user_input 
    })


    client = get_client()
    response = client.chat.completions.create(
        messages=messages,
        model=model_name
    )

    return response.choices[0].message.content

