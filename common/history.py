import streamlit as st

from common.show import show_msg

def init_history() -> None:
    # 이력 데이터를 저장하기 위해서
    if "history" not in st.session_state:
        # 선언! ==> 초기화
        st.session_state.history = []

    for h in st.session_state.history:
        show_msg(**h, is_history=True)