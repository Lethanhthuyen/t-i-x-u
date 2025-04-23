def predict_next(results):
    """
    Dự đoán kết quả tiếp theo dựa trên chuỗi kết quả trước đó.
    Đây chỉ là mô phỏng đơn giản, bạn có thể nâng cấp thuật toán sau.

    Args:
        results (list of str): Danh sách kết quả trước đó. Ví dụ: ['T', 'X', 'T', 'T']

    Returns:
        str: 'T' hoặc 'X' - kết quả dự đoán tiếp theo
    """
    if not results:
        return 'T'  # Mặc định nếu không có dữ liệu

    # Đếm số lần xuất hiện của Tài và Xỉu
    tai_count = results.count('T')
    xiu_count = results.count('X')

    # Dự đoán ngược lại nếu một bên xuất hiện quá nhiều (kiểu lật kèo)
    if tai_count > xiu_count:
        return 'X'
    elif xiu_count > tai_count:
        return 'T'
    else:
        # Nếu bằng nhau thì random
        import random
        return random.choice(['T', 'X'])
