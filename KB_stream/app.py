import streamlit as st
import LawSearch
import TermsSearch

ls = LawSearch.LawSearcher()
ts = TermsSearch.TermsSearcher()

st. set_page_config(layout="wide")

add_selectbox01 = st.sidebar.selectbox(
    "문서 카테고리",
    ('홈','법령','예금/적금 약관', '비교')
)

if add_selectbox01 == '법령':
    st.title('법령 검색')
    input_sents01 = st.text_input('키워드를 입력해 주세요.','')

    if input_sents01:
        # model
        ls.find_law(input_sents01)

elif add_selectbox01 == '예금/적금 약관':
    st.title('약관 검색')
    input_sents02 = st.text_input('키워드를 입력해 주세요.','')

    if input_sents02:
        ts.find_term(input_sents02)
    
elif add_selectbox01 == '비교':
    col1, col2 = st.columns(2)

    with col1:
        st.title('법령 검색')
        law_input = st.text_input('키워드를 입력해 주세요.','', key='법령')
        
        if law_input:
            ls.find_law(law_input)

    with col2:
        st.title('약관 검색')
        term_input = st.text_input('키워드를 입력해 주세요.','', key='약관')
        
        if term_input:
            ts.find_term(term_input)

else:
    st.header('문서 추천 시스템')
    st.text('''
기존의 pdf 형식의 약관 내용을 JSON 형식으로 변환하여 호출방식을 개선했습니다.
검색시 단순히 문서 제목만 추적하여 내용을 보여주는 것이 아니라
문서 내용과 검색어 사이의 코사인 유사도를 측정하여 문서 추천을 진행합니다.''')