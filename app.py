from flask import session
import streamlit as st
import random
import requests
import json

from zmq import NULL

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
    selected_analysis = st.sidebar.selectbox("分析項目", analysis_cat)
    # 事業部名一覧取得
    div_factory_url = 'http://127.0.0.1:8000/div_factorys'

    res = requests.get(div_factory_url)
    # if res is NULL:
    #     st.write("データがありません。")
    #     st.button("データ登録しますか？")

    # else:
    st.sidebar.write(res)
            
    div_factorys = res.json()
    # st.write(res.status_code)
    div_factory_datas = {}
    # div_datas = {}

    # factorys = {}
    for div_factory in div_factorys:
        div_factory_datas[div_factory['factory_name']] = {
            'factory_id' : div_factory["factory_id"],
            'div_name' : div_factory["div_name"],
            'div_cat_name' : div_factory["div_cat_name"]
            }
    # st.write(div_factory_datas)

    selected_div = st.sidebar.selectbox("事業部を選択してください", div_factory_datas.keys())
    selected_factory = st.sidebar.selectbox("工場を選択してください", div_factory_datas.keys())
    if res.status_code == 200:
        st.sidebar.success("成功")
    # st.json(res.json())
    div_select_button = st.sidebar.form_submit_button(label = "分析内容と事業部選択")

if div_select_button:
    st.write("登録内容")
    st.json(div_factory_datas)
    st.write("レスポンス結果")
    url = 'http://127.0.0.1:8000/div_factorys'
    res = requests.post(
        url,
        div_datas = json.dumps(div_factory_datas)
    )
    if res.status_code == 200:
        st.success("成功")
    st.json(res.json())



regi_div = st.sidebar.button("事業部登録画面")

if regi_div:
    st.session_state.count = 1

if st.session_state.count > 0:
    st.write("##事業部登録")
    with st.form(key="divs"):
        div_name : str = st.text_input("事業部名", max_chars=12)
        div_cat_name : str = st.text_input("部門名(例:フォトニクス事業部→OPM,LDなど", max_chars=12)
        factory_name : str = st.text_input("工場名", max_chars=12)
        
        div_factory_data = {
            'div_name': div_name,
            'div_cat_name':div_cat_name,
            'factory_name':factory_name
            # 'tag_name': tag_name
        }
        # factory_name : str = st.text_input("工場名", max_chars=12)
        # tag_name : str = st.text_input("部門名(例:フォトニクス事業部→OPM,LDなど", max_chars=12)
        # data = {
        #     'factory_name': factory_name,
        #     # 'tag_name': tag_name
        # }
        submit_bottun = st.form_submit_button(label="登録実行")
    if submit_bottun:
        st.write("登録内容")
        st.json(div_factory_data)
        st.write("レスポンス結果")
        url = 'http://127.0.0.1:8000/div_factorys'
        res = requests.post(
            url,
            data = json.dumps(div_factory_data)
        )
        if res.status_code == 200:
            st.success("成功")
        st.json(res.json())



    # st.write("##工場登録")
    # with st.form(key="factory"):

    #     submit_bottun = st.form_submit_button(label="登録実行")
    # if submit_bottun:
    #     st.write("登録内容")
    #     st.json(div_factory_data)
    #     st.write("レスポンス結果")
    #     url = 'http://127.0.0.1:8000/factorys'
    #     res = requests.post(
    #         url,
    #         data = json.dumps(div_factory_data)
    #     )
    #     if res.status_code == 200:
    #         st.success("成功")
    #     st.json(res.json())