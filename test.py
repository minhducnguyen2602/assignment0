du_lieu_sach = [
    {
        "bookname": "Dế Mèn Phiêu Lưu Ký",
        "author": "Tô Hoài",
        "publishyear": 1980,
        "category": "Truyện ngắn"
    },
    {
        "bookname": "Anna Karenina",
        "author": "Leo Tolstoy",
        "publishyear": 1877,
        "category": "Tiểu thuyết"
    },
    {
        "bookname": "Dấu Chân Trên Cát",
        "author": "Nguyễn Ngọc Thuần",
        "publishyear": 2003,
        "category": "Tạp chí"
    },
    {
        "bookname": "Số Đỏ",
        "author": "Hồ Chí Minh",
        "publishyear": 1969,
        "category": "Chính trị"
    },
    {
        "bookname": "Harry Potter và Hòn Đá Phù Thủy",
        "author": "J.K. Rowling",
        "publishyear": 1997,
        "category": "Fantasy"
    },
    {
        "bookname": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publishyear": 1960,
        "category": "Tiểu thuyết"
    },
    {
        "bookname": "Sherlock Holmes",
        "author": "Arthur Conan Doyle",
        "publishyear": 1887,
        "category": "Truyện trinh thám"
    },
    {
        "bookname": "Nhà Giả Kim",
        "author": "Paulo Coelho",
        "publishyear": 1988,
        "category": "Tâm lý - Tâm linh"
    },
    {
        "bookname": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publishyear": 1925,
        "category": "Tiểu thuyết"
    },
    {
        "bookname": "1984",
        "author": "George Orwell",
        "publishyear": 1949,
        "category": "Chính trị"
    }
]


du_lieu_nguoi_dung = [
    {
        "username": "Nguyễn Văn A",
        "dateofbirth": "1990-05-15"
    },
    {
        "username": "Trần Thị B",
        "dateofbirth": "1985-09-22"
    },
    {
        "username": "Lê Văn C",
        "dateofbirth": "1995-03-10"
    },
    {
        "username": "Phạm Thị D",
        "dateofbirth": "1980-12-05"
    },
    {
        "username": "Ngô Minh E",
        "dateofbirth": "1992-08-18"
    }
]
import requests
base_url = "http://localhost:8000"

def them_nguoi_dung(api_url, data):
    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        print("Thêm người dùng thành công!")
    else:
        print("Thêm người dùng thất bại. Mã trạng thái:", response.status_code)
        print("Nội dung lỗi:", response.text)

def them_sach(api_url, data):
    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        print("Thêm sách thành công!")
    else:
        print("Thêm sách thất bại. Mã trạng thái:", response.status_code)
        print("Nội dung lỗi:", response.text)

# Đường dẫn API để thêm người dùng và sách
duong_dan_them_nguoi_dung = f"{base_url}/registering"
duong_dan_them_sach = f"{base_url}/add_book"

# Thêm người dùng
for user_data in du_lieu_nguoi_dung:
    them_nguoi_dung(duong_dan_them_nguoi_dung, user_data)

# # Thêm sách
# for book_data in du_lieu_sach:
#     them_sach(duong_dan_them_sach, book_data)