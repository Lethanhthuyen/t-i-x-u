def predict_next(sequence):
    if not sequence or len(sequence) < 3:
        return "Không đủ dữ liệu"

    last = sequence[-1]
    count_T = sequence.count("T")
    count_X = sequence.count("X")

    if count_T > count_X:
        return "T"
    elif count_X > count_T:
        return "X"
    else:
        return last
