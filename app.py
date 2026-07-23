from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <div style='text-align: center; padding: 50px; font-family: Arial; background-color: #eef2f5; min-height: 100vh;'>
        <h1 style='color: #0d6efd;'>HỆ THỐNG QUẢN LÝ PHÂN CÔNG CÔNG VIỆC</h1>
        <h3 style='color: #198754;'>Nhóm thực hiện: Nhóm 1</h3>
        <p>Sprint 1 - Milestone 1: Khởi tạo dự án thành công</p>
        <hr style='width: 40%; margin: 20px auto;'>
        <a href='/about' style='background: #0d6efd; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;'>Xem thông tin nhóm</a>
    </div>
    """

@app.route("/about")
def about():
    return """
    <div style='text-align: center; padding: 50px; font-family: Arial;'>
        <h2>TRANG GIỚI THIỆU DỰ ÁN</h2>
        <p>Bài thực hành 01 - Lập trình Python (Flask Framework)</p>
        <br>
        <a href='/'>← Quay lại Trang chủ</a>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)