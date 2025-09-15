'''
Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python.
'''
-Các lỗi:
    + Lỗi cú pháp: xảy ra khi Python không hiểu được cú pháp của một dòng nào đó
    + Lỗi ngoại lệ: xảy ra trong quá trình thực thi chương trình, sau khi chương trình được thông dịch
    + Lỗi logic: là lỗi nghiêm trọng nhất, vì chương trình chạy bình thường, không báo lỗi hay ngoại lệ nào, nhưng kết quả cho ra sai lệch với yêu cầu
- Cách bắt lỗi:
    Dùng khối lệnh try...except
        + try:chứa đoạn mã mà nghi ngờ gây ra Lỗi\
        + except: nếu lỗi xảy ra trong khối try, chương trình sẽ chạy khối except trương ứng với lỗi đó.Có thể có nhiều khối except với mỗi lỗi khác nhau
        