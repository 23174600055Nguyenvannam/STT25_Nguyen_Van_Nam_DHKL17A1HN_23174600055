import json

def hien_thi_sach_noi_bat():
    try:
        conn = __import__('http.client').HTTPSConnection("jsonplaceholder.typicode.com")
        conn.request("GET", "/comments?postId=1")
        response = conn.getresponse()
        if response.status == 200:
            data = json.loads(response.read())
            hien_thi_thong_tin_sach_noi_bat(data)
        else:
            print(f"Không thể kết nối đến API. Mã lỗi: {response.status}")
        conn.close()
    except Exception as e:
        print(f"Lỗi kết nối: {e}")

def hien_thi_thong_tin_sach_noi_bat(data):
    # In danh sách bài post nổi bật
    print("Danh sách các bài post nổi bật:\n")

    # Hiển thị thông tin của mỗi bài post (giới hạn chỉ hiển thị 3 bài đầu)
    for i, post in enumerate(data[:3], 1):
        print(f"Bài Post {i}:")
        print(f"   - Tên: {post['name']}")
        print(f"   - Email: {post['email']}")
        print(f"   - Nội dung: {post['body']}\n")

if __name__ == "__main__":
    print("Đang tải thông tin sách nổi bật từ API...\n")
    hien_thi_sach_noi_bat()
