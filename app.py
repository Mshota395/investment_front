from email.policy import default
from flask import session
import streamlit as st
import random
import requests
import json
from sqlalchemy.orm import Session
from sql_app import models, schemas



from zmq import NULL

st.set_page_config(layout="wide")


if "count" not in st.session_state:
    st.session_state.count = 0

st.sidebar.title("事業部名選択")
with st.sidebar.form(key = "investment_plan"):
    #分析内容の選択
    analysis_cat = ["稟議", "発注", "検収"]
    selected_analysis = st.selectbox("分析項目", analysis_cat)
    # 事業部名一覧取得
    div_factory_url = 'http://127.0.0.1:8000/div_factorys'

    res = requests.get(div_factory_url)
    # データ登録がなかったら。を入れる
    # st.write(res)
            
    div_factorys = res.json()
    # st.write(res.status_code)
    div_factory_datas = {}
    # div_datas = {}

    # factorys = {}
    for div_factory in div_factorys:
        div_factory_datas[div_factory['div_name']] = {
            'factory_id' : div_factory["factory_id"],
            'factory_name' : div_factory["factory_name"],
            'div_cat_name' : div_factory["div_cat_name"]
            }
    # st.write(div_factory_datas)
    # st.write(div_factory_datas)
    selected_div = st.selectbox("事業部を選択してください", div_factory_datas.keys())
    # st.write(div_factory_datas[selected_div]["factory_name"])
    selected_factory = st.write("工場名 : ", div_factory_datas[selected_div]["factory_name"])
    # if res.status_code == 200:
    #     st.success("成功")
    # st.json(res.json())
    div_select_button = st.form_submit_button(label = "分析内容と事業部選択")

if div_select_button:
    st.write("登録内容")
    st.json(div_factory_datas)
    st.write("レスポンス結果")
    url = 'http://127.0.0.1:8000/div_factorys'
    res = requests.get(
        url,
        div_datas = json.dumps(div_factory_datas)
    )
    if res.status_code == 200:
        st.success("成功")
    st.json(res.json())



regi_div = st.sidebar.button("事業部登録画面")

with st.sidebar.form(key="up_div"):
    url = 'http://127.0.0.1:8000/div_factorys'
    res = requests.get(url)
    div_factorys = res.json()
    div_factorys_names = {}
    for div_factory in div_factorys:
        div_factorys_names[div_factory["div_name"]] = {
            "div_name":div_factory["div_name"],
            "div_cat_name":div_factory["div_cat_name"],
            "factory_name":div_factory["factory_name"],
            "factory_id":div_factory["factory_id"]
        }
         
    # st.write(div_factorys)

    update_div_factory = st.selectbox("修正番号",div_factorys_names.keys())
    update_div = st.form_submit_button("登録データ更新")

if regi_div:
    st.session_state.count = 1

if st.session_state.count == 1:
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

st.write(st.session_state.count)
if update_div:
    st.session_state.count = 2

if st.session_state.count == 2:
    st.write("##事業部更新")
    with st.form(key="update_divs"):
        
        factory_id : str = div_factorys_names[update_div_factory]["factory_id"]
        div_name : str = st.text_input("事業部名", max_chars=12, value = div_factorys_names[update_div_factory]["div_name"])
        div_cat_name : str = st.text_input("部門名(例:フォトニクス事業部→OPM,LDなど", max_chars=12,value = div_factorys_names[update_div_factory]["div_cat_name"])
        factory_name : str = st.text_input("工場名", max_chars=12, value = div_factorys_names[update_div_factory]["factory_name"])
        
        div_factory_data = {
            "factory_id": factory_id,
            'div_name': div_name,
            'div_cat_name':div_cat_name,
            'factory_name':factory_name
        }
        update_submit_bottun = st.form_submit_button(label="更新実行")
    if update_submit_bottun:
        st.write("更新内容")
        st.json(div_factory_data)
        st.write("レスポンス結果")
        url = 'http://127.0.0.1:8000/div_update'
        res = requests.put(
            url,
            data = json.dumps(div_factory_data)
        )
        st.write(res.status_code)
        if res.status_code == 200:
            st.success("成功")
        st.json(res.json())