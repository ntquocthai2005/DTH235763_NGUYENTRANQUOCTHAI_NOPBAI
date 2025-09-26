'''
Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.
(vd: n=35 => Ba mươi lăm, n=5 => năm)
'''
don_vi=['không','một','hai','ba','bốn','năm','sáu','bảy','tám','chín']
hang_chuc=['mười','mười một','mười hai','mười ba','mười bốn','mười lăm','mười sáu','mười bảy','mười tám','mười chín']
chuc_tron=['','','hai mươi','ba mươi','bốn mươi','năm mươi','sáu mươi','bảy mươi','tám mươi','chín mươi']
try:
    so=int(input("Nhập một số nguyên có tối đa 2 chữ số: "))
    if 0<=so<=99:
        if 0<=so<=9:
            print(f"Số {so} đọc là: {don_vi[so]}")
        elif 10<=so<=19:
            print(f"Số {so} đọc là: {hang_chuc[so-10]}")
        else:
            so_chuc=so //10
            so_don_vi=so%10
            ket_qua=chuc_tron[so_chuc]
            if so_don_vi==0:
                print(f"Số {so} đọc là: {ket_qua}")
            elif so_don_vi==5:
                ket_qua+="lăm"
                print(f"Số {so} đọc là: {ket_qua}")
            elif so_don_vi>0:
                ket_qua+=" "+don_vi[so_don_vi]
                print(f"Số {so} đọc là: {ket_qua}")
    else:
        print("Số bạn nhập không hợp lệ.Vui lòng nhập số từ 0 đến 99")
except ValueError:
    print("Bạn nhập không phải số.Vui lòng nhập lại.")
