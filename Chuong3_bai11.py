'''
Yêu cầu:
Cho biểu thức toán học sau:
Viết chương trình cho phép nhập x, n và xuất ra kết quả của biểu thức.
'''
while True:
    n=int(input("Nhập một số nguyên dương: "))
    dem=0
    for i in range (1,n+1):
        if n%i==0:
            dem+=1
    if dem==2:
        print(n,"Là số nguyên tố")
    else:
        print(n,"Không là số nguyên tố")
    hoi=input("Bạn có muốn tiếp tục?(c/k):")
    if hoi is "k":
        break
    print("BYE!")