'''
Yêu cầu:
Nhập vào một năm bất kỳ, kiểm tra năm đó có phải năm nhuần hay không. Biết
rằng: Năm nhuần là năm chia hết cho 4 nhưng không chia hết cho 100 hoặc chia
hết cho 400
'''
print("Chương trình kiểm tra năm nhuần")
year=int(input("Mời bạn nhập vào một năm: "))
if(year%4 ==0 and year % 100 !=0) or year % 400 ==0:
    print("Năm ",year,"là năm nhuần.")
else:
    print("Năm ",year,"không là năm nhuần")