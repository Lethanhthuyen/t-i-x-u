import streamlit as st
from predict import analyze_pattern

st.title("Phân Tích Cầu Tài Xỉu")
st.markdown("**Nhập chuỗi kết quả gần đây (T cho Tài, X cho Xỉu)**")

user_input = st.text_input("Ví dụ: T,X,T,T,X")

if user_input:
    results = [x.strip().upper() for x in user_input.split(",") if x.strip().upper() in ['T', 'X']]
    if results:
        pattern, prediction = analyze_pattern(results)
        st.success(f"Phân tích: {pattern}")
        st.info(f"Dự đoán kết quả tiếp theo: **{prediction}**")
    else:
        st.warning("Chuỗi nhập vào không hợp lệ. Hãy dùng T hoặc X, cách nhau bởi dấu phẩy.")