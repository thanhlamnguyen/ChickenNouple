#các thư việc cần thiết
import folder_op, web_op

def start():
    #Nhóm các biến toàn cục cung cấp thông số cho chương trình
    url_lis = ["https:'vietnamnet.vn"]  #Chứa các đường link sẽ được duyêth
    history = []    #Chứa các đường link đã duyệt
    max_pge = 1000  #Quy định số lượng trong web được tải về
    count = 0   #Đếm số lượng trang web được tải về
    data_folder = "C:\\Users\\DELL\\Downloads\\crawl"

    #Kịch bả tải các trang web
    while (count < max_page) and (len(url_list)):
        url = url_list.pop(0)
        page = web_op.doc_noi-dung(url)
        links = web_op.lay_cac_duong_link(page)
        for item in links:  #duyệt từng đường link thu được để kiểm tra tính hợp lệ
            if web_op.kiem_tra_limk(item):  #Nếu đường link là hợp lệ thì tiếp thực hiện đoạn lệnh
                item = web_op.chinh_sua_link(item)  #Chỉnh sửa nếu thiếu phần https:\\...
                if not((item in url_list) and (item in history)):   #Nếu đường link mới vào danh sách chờ duyệt
                    url_list.append(item)#Thêm đường link mới vào danh sách chờ duyệt
        folder_op.luu_noi_dung_xuong_file(page, data_folder)
        history.append(url)
        count += 1


#Press the green buton in the gutter to run the script.
if _name_=="__main__":
    start()

# See pycharm help at https://www.jetbrains.com/help/pycharm/