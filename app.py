import streamlit as st

from common.show import show_msg
from common.constants import ROLE
from common.history import init_history
from common.ai import get_msg_of_ai
st.title("ChatBot Service")

init_history()


user_input = st.chat_input("메시지 입력해주세요.")

if user_input : # 만약 사용자 인풋이 있다면 화면에 프린트 해줘
    show_msg(**{
        "role" : ROLE.user,
        "msg" : user_input
    })

    show_msg(**{
        "role" : ROLE.assistant,
        "msg" : get_msg_of_ai(user_input)
    })
