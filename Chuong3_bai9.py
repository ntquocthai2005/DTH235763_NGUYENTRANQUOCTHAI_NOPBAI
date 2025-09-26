'''
 Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm.
 '''
try:
    thang=int(input("Nhập một tháng: "))
    if thang in [1,2,3]:
        print(f"Tháng {thang} nằm ở quý 1")
    elif thang in [4,5,6]:
        print(f"Tháng {thang} nằm ở quý 2")
    elif thang in [7,8,9]:
        print(f"Tháng {thang} nằm ở quý 3")
    elif thang in [10,11,12]:
        print(f"Tháng {thang} nằm ở quý 4")
    else:
        print("Tháng không hợp lệ.Vui lòng nhập lại.")
except ValueError:
    print("Bạn nhập không phải tháng.Vui lòng nhập lại.")