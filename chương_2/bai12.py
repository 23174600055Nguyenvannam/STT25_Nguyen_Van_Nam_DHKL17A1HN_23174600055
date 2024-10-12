import json

def hien_thi_sach_tu_api():
    conn = __import__('http.client').HTTPSConnection("jsonplaceholder.typicode.com")
    conn.request("GET", "/posts")
    response = conn.getresponse()

    if response.status == 200:
        data = json.loads(response.read())
        hien_thi_thong_tin_sach(data)
    else:
        print(f"Không thể kết nối đến API. Mã lỗi: {response.status}")
    conn.close()

def hien_thi_thong_tin_sach(data):
    print(f"Tổng số bài post: {len(data)}\n")
    for post in data:
        print(f"userID: {post['userId']}")
        print(f"id: {post['id']}")
        print(f"title: {post['title']}")
        print(f"body: {post['body']}\n")

if __name__ == "__main__":
    print("Đang tải thông tin sách từ API...\n")
    hien_thi_sach_tu_api()
