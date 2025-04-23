import streamlit as st
from predict_next_tai_xiu import predict_next

st.set_page_config(page_title="Dự đoán Tài Xỉu", page_icon="🎲")

st.title("Dự đoán kết quả Tài Xỉu")

# Nhập chuỗi kết quả gần đây
results_input = st.text_input("Nhập chuỗi kết quả (T cho Tài, X cho Xỉu, viết liền không dấu cách):", "")

if st.button("Dự đoán"):
    if all(char in "TXtx" for char in results_input) and len(results_input) > 0:
        prediction = predict_next(results_input.upper())
        st.success(f"Kết quả dự đoán tiếp theo: **{prediction}**")
    else:
        st.error("Vui lòng chỉ nhập các ký tự T hoặc X.")
