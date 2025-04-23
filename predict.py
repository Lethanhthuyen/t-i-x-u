def analyze_pattern(results):
    if len(results) < 4:
        return "Không đủ dữ liệu để phân tích", "?"

    # Mô hình bệt
    if results[-1] == results[-2] == results[-3]:
        return "Cầu bệt", results[-1]

    # Mô hình 1-1
    if results[-1] != results[-2] and results[-2] != results[-3]:
        return "Cầu 1-1", 'T' if results[-1] == 'X' else 'X'

    # Mô hình 2-2
    if len(results) >= 4 and results[-1] == results[-2] and results[-3] == results[-4] and results[-1] != results[-3]:
        return "Cầu 2-2", results[-3]

    # Mặc định
    return "Không rõ cầu", results[-1]