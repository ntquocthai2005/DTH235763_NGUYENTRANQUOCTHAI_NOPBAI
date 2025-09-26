def la_nam_nhuan(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

def so_ngay_trong_thang(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        return 29 if la_nam_nhuan(nam) else 28
    else:
        return 0

def tim_ngay_ke_tiep(ngay, thang, nam):
    so_ngay = so_ngay_trong_thang(thang, nam)

    ngay += 1

    if ngay > so_ngay:
        ngay = 1
        thang += 1
        if thang > 12:
            thang = 1
            nam += 1
            
    return ngay, thang, nam

try:
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))

    if 1 <= thang <= 12 and 1 <= ngay <= so_ngay_trong_thang(thang, nam):
        ngay_ke_tiep, thang_ke_tiep, nam_ke_tiep = tim_ngay_ke_tiep(ngay, thang, nam)
        print(f"Ngày kế sau ngày {ngay}/{thang}/{nam} là: {ngay_ke_tiep}/{thang_ke_tiep}/{nam_ke_tiep}")
    else:
        print("Ngày, tháng hoặc năm không hợp lệ. Vui lòng kiểm tra lại.")

except ValueError:
    print("Dữ liệu nhập không phải là số. Vui lòng nhập lại.")