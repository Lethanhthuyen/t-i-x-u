import streamlit as st
from predict import predict_next

st.set_page_config(page_title="Phân Tích Cầu Tài Xỉu", page_icon="🎲", layout="centered")

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='color: #ff4b4b;'>Phân Tích Cầu Tài Xỉu 🎲</h1>
        <p style='font-size: 18px;'>Dự đoán kết quả tiếp theo dựa trên lịch sử</p>
    </div>
    """, unsafe_allow_html=True
)

# Nhập kết quả gần đây
input_text = st.text_input("Nhập chuỗi kết quả gần đây (T hoặc X, ví dụ: TXXTTX):")

if st.button("Phân tích ngay"):
    if input_text:
        with st.spinner("Đang phân tích..."):
            result = predict_next(input_text.strip().upper())
            st.success(f"Dự đoán tiếp theo: **{result}**")
    else:
        st.warning("Vui lòng nhập chuỗi kết quả trước khi phân tích.")
