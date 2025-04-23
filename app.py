import streamlit as st
from predict_next_tai_xiu import predict_next, thong_ke_chuoi_cau

st.set_page_config(page_title="Phân tích cầu Tài Xỉu", layout="centered")

st.title("Dự đoán & Thống kê cầu Tài Xỉu")
st.write("Nhập kết quả gần đây (T = Tài, X = Xỉu), phân cách bằng dấu phẩy.")

user_input = st.text_input("Nhập chuỗi kết quả:", "T,X,T,X,X,T,T,T,X")

if st.button("Phân tích"):
    inputs = [i.strip().upper() for i in user_input.split(",") if i.strip().upper() in ["T", "X"]]

    if not inputs:
        st.warning("Vui lòng nhập đúng định dạng chuỗi gồm T và X.")
    else:
        # Dự đoán kết quả tiếp theo
        du_doan = predict_next(inputs)
        st.subheader(f"**Dự đoán kết quả tiếp theo:** {du_doan}")

        # Thống kê chuỗi
        thong_ke = thong_ke_chuoi_cau(inputs)
        st.subheader("**Thống kê chuỗi Tài/Xỉu liên tiếp:**")
        for kq, sl in thong_ke:
            loai = "TÀI" if kq == "T" else "XỈU"
            st.write(f"{loai} liên tiếp: {sl} lần")
