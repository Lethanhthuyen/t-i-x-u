def predict_next(inputs):
    if not inputs or len(inputs) < 3:
        return "Không đủ dữ liệu"
    count_t = inputs.count('T')
    count_x = inputs.count('X')
    if count_t > count_x:
        return 'XỈU'
    elif count_x > count_t:
        return 'TÀI'
    else:
        return 'TÀI'

def thong_ke_chuoi_cau(inputs):
    if not inputs:
        return []
    ket_qua = []
    hien_tai = inputs[0]
    dem = 1
    for i in range(1, len(inputs)):
        if inputs[i] == hien_tai:
            dem += 1
        else:
            ket_qua.append((hien_tai, dem))
            hien_tai = inputs[i]
            dem = 1
    ket_qua.append((hien_tai, dem))
    return ket_qua
