'''
Yêu cầu:
Nhập bán kính đường tròn r. Tính và xuất chu vi, diện tích đường tròn tương ứng.
HD: cv=2*π*r và dt=π*r*r
'''
try:
    r=float(input("Moi ban nhap ban kinh hinh tron: "))
    cv=2*math.pi*r
    dt=r**2
    print("Chu vi= ",cv)
    print("Dien tich= ",dt)
except:
    print("Loi roi!")