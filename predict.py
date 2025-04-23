def predict_next(inputs):
    # Dummy logic, trả về 'TÀI' nếu số lần 'TÀI' nhiều hơn, ngược lại 'XỈU'
    count_tai = inputs.count('T')
    count_xiu = inputs.count('X')
    return 'TÀI' if count_tai >= count_xiu else 'XỈU'
    count_T = sequence.count("T")
    count_X = sequence.count("X")

    if count_T > count_X:
        return "T"
    elif count_X > count_T:
        return "X"
    else:
        return last
