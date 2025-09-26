'''
Nhập vào 2 giá trị a, b và phép toán +, -, *, / . Hãy xuất kết quả theo
đúng phép toán đã nhập.
'''

try:
    a=int(input("Nhập một số a: "))
    b=int(input("Nhập một số b: "))
    phep_toan=str(input("Nhập một phép tính: "))
    if phep_toan=="+":
        ket_qua=a+b
        print(f"Kết quả phép tính {a}+{b} = {ket_qua}")
    elif phep_toan=="-":
        ket_qua=a-b
        print(f"Kết quả phép tính {a}-{b} = {ket_qua}")
    elif phep_toan=="*":
        ket_qua=a*b
        print(f"Kết quả phép tính {a}*{b} = {ket_qua}")
    elif phep_toan=="/":
        if b==0:
            print("không thể chia cho 0.Vui lòng nhập số khác.")
        else:
            ket_qua=a/b
            print(f"Kết quả phép tính {a}/{b} = {ket_qua}")
except ValueError:
    print("Bạn nhập không phải số.Vui lòng nhập lại.")
