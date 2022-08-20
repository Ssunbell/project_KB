import pandas as pd
import streamlit as st
# st.__version__ 1.11.0
import json


# 다합친 json이 에러가남.
# with open(file_path,'r') as f:
#     data = json.load(f)

add_selectbox01 = st.sidebar.selectbox(
    "문서 카테고리",
    ('홈','법령','예금/적금 조항')
)

if add_selectbox01 == '법령':
    input_sents01 = st.text_input('키워드를 적어주세요.','')

    # title list

    if input_sents01:
        # model

        # example selected json
        file_path = 'C:/Users/User/Desktop/git_repo/KB/data/law/str_data/개인정보 보호법 시행령.json'
        f = open(file_path, encoding="utf-8")
        raw_data = json.loads(f.read())
        doc_name = list(raw_data.keys())[0]
        raw_data[doc_name].keys()

        add_selectbox02 = st.selectbox(
            f'{doc_name}이 추천 되었습니다.',
            raw_data[doc_name].keys()
        )

        if add_selectbox02:
            add_selectbox03 = st.selectbox(
                f'조항입니다.',
                raw_data[doc_name][add_selectbox02].keys()
            )
            st.text_area('Contents',f'{raw_data[doc_name][add_selectbox02][add_selectbox03]}')


elif add_selectbox01 == '예금/적금 조항':
    input_sents02 = st.text_input('키워드를 적어주세요.','')

    # load all doc
    file_path = 'C:/Users/User/Desktop/git_repo/KB/nayeon/data/terms.json'
    with open(file_path, 'r', encoding='utf-8') as f:
        f = f.read()
        data = json.loads(f)

    # example 0 index
    if input_sents02:
        add_selectbox02 = st.selectbox(
            f'{list(data.keys())[0]}이 추천 되었습니다.',
            data[list(data.keys())[0]].keys()
        )

        st.text_area('Contents',data[input_sents02][add_selectbox02])

else:
    st.header('문서 추천 시스템')
    st.text('''
기존의 pdf 형식의 약관 내용을 텍스트형식으로 변환하여 호출방식을 개선했습니다.
일반 검색시 단순히 문서 제목만 추적하여 내용을 보여주는것이 아니라
문서내부 키워드를 작성하여 코사인유사도를 통한 문서 추천을 진행합니다.''')