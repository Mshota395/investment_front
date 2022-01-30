from flask import session
import streamlit as st
import random
import requests
import json

st.set_page_config(layout="wide")


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


# selected_analysis = st.form_submit_button(label = "分析内容の選択")


st.sidebar.title("事業部名選択")
with st.sidebar.form(key = "investment_plan"):
    #分析内容の選択
    analysis_cat = ["稟議", "発注", "検収"]
    selected_analysis = st.selectbox("分析項目", analysis_cat)
    # 事業部名一覧取得
    div_factory_url = 'http://127.0.0.1:8000/div_factorys'

    res = requests.get(div_factory_url)
    div_factorys = res.json()
    # st.write(res.status_code)
    divnames = {}
    factorys = {}
    for div in div_factorys:
        divnames[div['div_name']] = div['div_id']
    for factory in factorys:
        factorys[factory["factory_name"]] = factory["factory_id"]
        
    selected_div = st.selectbox("事業部を選択してください", divnames.keys())
    selected_factory = st.selectbox("工場を選択してください", factorys.keys())
    # if res.status_code == 200:
    #     st.success("成功")
    # st.json(res.json())
    div_select_button = st.form_submit_button(label = "分析内容と事業部選択")


regi_div = st.sidebar.button("事業部登録画面")

if regi_div:
    st.session_state.count = 1

if st.session_state.count > 0:
    st.write("##事業部登録")
    with st.form(key="divs"):
        div_name : str = st.text_input("事業部名", max_chars=12)
        # tag_name : str = st.text_input("部門名(例:フォトニクス事業部→OPM,LDなど", max_chars=12)
        div_data = {
            'div_name': div_name,
            # 'tag_name': tag_name
        }
        factory_name : str = st.text_input("工場名", max_chars=12)
        # tag_name : str = st.text_input("部門名(例:フォトニクス事業部→OPM,LDなど", max_chars=12)
        factory_data = {
            'factory_name': factory_name,
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