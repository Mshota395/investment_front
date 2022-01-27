from flask import session
import streamlit as st
import random
import requests
import json



if "count" not in st.session_state:
    st.session_state.count = 0


# st.sidebar.title("実績選択画面")
# div = st.sidebar.selectbox("部門を選択してください",["PHT", "OPM", "LD"])
# if div == "OPM":
#     factory = st.sidebar.selectbox("工場を選択してください",["ALL", "本社","アポロ", "ワコー", "REDA", "RIST", "RCS_DP", "RSC_SS"])
# elif div == "LD":
#     factory = st.sidebar.selectbox("工場を選択してください",["ALL", "本社","ワコー","RCS"])
# else:
#     factory = "ALL"
    
# st.sidebar.title("確認画面")
# comfirmitem = st.sidebar.selectbox("確認項目を選択してください",["稟議", "発注", "検収"])
# if comfirmitem == "OPM":
#     factory = st.sidebar.selectbox("工場を選択してください",["ALL", "本社","アポロ", "ワコー", "REDA", "RIST", "RCS_DP", "RSC_SS"])
# elif comfirmitem == "LD":
#     factory = st.sidebar.selectbox("工場を選択してください",["ALL", "本社","ワコー","RCS"])
# else:
#     factory = "ALL"
st.sidebar.title("事業部名選択")
with st.sidebar.form(key = "investment_plan"):
    # 事業部名一覧取得
    div_url = 'http://127.0.0.1:8000/divs'

    res = requests.get(div_url)
    divs = res.json()
    st.write(res.status_code)
    divnames = {}
    for div in divs:
        divnames[div['div_name']] = div['div_id']
        
    selected_div = st.selectbox("事業部を選択してください", divnames.keys())
    # if res.status_code == 200:
    #     st.success("成功")
    # st.json(res.json())
    div_select_button = st.form_submit_button(label = "事業部選択")


regi_div = st.sidebar.button("事業部登録画面")

if regi_div:
    st.session_state.count = 1

if st.session_state.count > 0:
    st.write("##事業部画面")
    with st.form(key="divs"):
        div_name : str = st.text_input("事業部名", max_chars=12)
        # tag_name : str = st.text_input("部門名(例:フォトニクス事業部→OPM,LDなど", max_chars=12)
        data = {
            'div_name': div_name,
            # 'tag_name': tag_name
        }
        submit_bottun = st.form_submit_button(label="登録実行")
    if submit_bottun:
        st.write("登録内容")
        st.json(data)
        st.write("レスポンス結果")
        url = 'http://127.0.0.1:8000/divs'
        res = requests.post(
            url,
            data = json.dumps(data)
        )
        if res.status_code == 200:
            st.success("成功")
        st.json(res.json())


        regi_div = st.sidebar.button("事業部登録画面")

    st.write("##工場登録")
    with st.form(key="factory"):
        factory_name : str = st.text_input("工場名", max_chars=12)
        # tag_name : str = st.text_input("部門名(例:フォトニクス事業部→OPM,LDなど", max_chars=12)
        data = {
            'div_name': div_name,
            # 'tag_name': tag_name
        }
        submit_bottun = st.form_submit_button(label="登録実行")
    if submit_bottun:
        st.write("登録内容")
        st.json(data)
        st.write("レスポンス結果")
        url = 'http://127.0.0.1:8000/factorys'
        res = requests.post(
            url,
            data = json.dumps(data)
        )
        if res.status_code == 200:
            st.success("成功")
        st.json(res.json())