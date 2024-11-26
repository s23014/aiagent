# 예측 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model=joblib.load('linear_regression_model (3).pkl')

# 2. 모델 설명
st.title('기대수명 예측 프로그램')
st.subheader('모델 설명')
st.write('-기계학습 알고리즘 : 선형회귀')
st.write('-학습데이터 출처 : http://www.kaggle.com/')
st.write('-훈련데이터 : 61건')
st.write('-테스트데이터 : 140건')
st.write('-모델 정확도 : 0.72')
# 3. 데이터시각화
col1,col2,col3=st.columns(3)
with col1:
 st.subheader('데이터 시각화1')
 st.image('시각화1 (2).png')
with col2:
 st.subheader('데이터 시각화2')
 st.image('시각화2 (2).png')
with col3:
 st.subheader('데이터 시각화3')
 st.image('시각화3.png')
# 4. 모델 활용
st.subheader('모델 활용')
st.write('기대수명을 예측해드립니다')

a=st.number_input('학습수준을 입력하세요',value=0)
b=st.number_input('국가의 물 접근성을 입력하세요.',value=0.0)
c=st.number_input('국가의 출산률을 입룍하세요',value=0.0)

if st.button('기대수명 예측'):
  input_data=[[a,b,c]]
  p=model.predict(input_data)
  st.write('기대수명은?',p)
