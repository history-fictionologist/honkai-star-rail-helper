# honkai-star-rail-helper

`honkai-star-rail-helper` là một tiện ích được thiết kế để quản lý và xử lý dữ liệu nhân vật, kỹ năng và đề xuất di vật cho trò chơi điện tử [Honkai: Star Rail](https://en.wikipedia.org/wiki/Honkai:_Star_Rail). Nó đọc các tệp đầu vào, xử lý các thuộc tính như thông tin nhân vật và bộ kỹ năng, và xuất kết quả theo định dạng tổ chức. Dữ liệu đầu vào được lấy từ các gói cập nhật chính thức trong kho lưu trữ [StarRailData](https://github.com/Dimbreath/StarRailData/tree/master) và đầu ra được lưu trữ trong các thư mục phân theo phiên bản để dễ dàng quản lý.

## Bảng Nhân Vật Mới Nhất
<!-- CHARACTER_TABLE_START -->
|          |   | Hủy Diệt                 | Săn Bắn       | Tri Thức  | Hòa Hợp      | Hư Vô         | Bảo Hộ       | Trù Phú   |
| -------- | - | ------------------------ | ------------- | --------- | ------------ | ------------- | ------------ | --------- |
| Vật Lý   | 5 | Clara\|Nhà Khai Phá\|Yunli | Boothill      | Argenti   | Robin        |               |              |           |
| Vật Lý   | 4 |                          | Sushang       |           | Hanya        | Luka          |              | Natasha   |
| Hỏa      | 5 | Firefly                  | Topaz & Numby | Himeko    |              | Jiaoqiu       | Nhà Khai Phá | Lingsha   |
| Hỏa      | 4 | Hook                     |               |           | Asta         | Guinaifen     |              | Gallagher |
| Băng     | 5 | Jingliu                  | Yanqing       |           | Ruan Mei     |               | Gepard       |           |
| Băng     | 4 | Misha                    |               | Herta     |              | Pela          | March 7th    |           |
| Lôi      | 5 |                          |               | Jing Yuan |              | Acheron\|Kafka |              | Bailu     |
| Lôi      | 4 | Arlan                    | Moze          | Serval    | Tingyun      |               |              |           |
| Phong    | 5 | Blade                    | Feixiao       |           | Bronya       | Black Swan    |              | Huohuo    |
| Phong    | 4 |                          | Dan Heng      |           |              | Sampo         |              |           |
| Lượng Tử | 5 |                          | Seele         | Jade      | Sparkle      | Sói Bạc       | Fu Xuan      |           |
| Lượng Tử | 4 | Xueyi                    |               | Qingque   |              |               |              | Lynx      |
| Số Ảo    | 5 | Dan Heng - Ẩm Nguyệt     | Dr. Ratio     |           | Nhà Khai Phá | Welt          | Aventurine   | Luocha    |
| Số Ảo    | 4 |                          | March 7th     |           | Yukong       |               |              |           |
<!-- CHARACTER_TABLE_END -->

## Tính Năng Chính
- Tự động tải xuống dữ liệu nhân vật, CV, bộ kỹ năng và đề xuất di vật.
- Xử lý và tổ chức dữ liệu vào các thư mục đầu vào/đầu ra phân theo phiên bản.
- Cấu hình số phiên bản trên dòng lệnh cho mỗi bản cập nhật mới.

## Yêu Cầu

Đảm bảo bạn có các điều sau:
- **Python 3.8+** (xác nhận bằng `python3 --version`).
- Các gói Python yêu cầu được liệt kê trong `requirements.txt`.

## Cài Đặt

1. **Clone kho lưu trữ:**
   ```bash
   git clone https://github.com/yourusername/hsr-helper.git
   cd hsr-helper
   ```

2. **(Tùy chọn) Tạo và kích hoạt môi trường ảo:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Trên Windows: venv\Scriptsctivate
   ```

3. **Cài đặt các phụ thuộc (hiện tại không yêu cầu phụ thuộc bổ sung):**
   ```bash
   # Hiện tại không cần cài đặt phụ thuộc, nhưng nếu cần trong tương lai:
   # pip install -r requirements.txt
   ```

## Sử Dụng

### Chạy Công Cụ
   Điều hướng đến thư mục `src/` và chạy script chính với số phiên bản mong muốn:
   ```bash
   cd src
   python3 main.py --version <version_number> [--skip-download]
   ```

   - Thay thế `<version_number>` bằng phiên bản hiện tại (ví dụ: `2.5`).
   - Nếu bạn muốn bỏ qua việc tải xuống tệp, hãy thêm cờ `--skip-download`.

   Các tệp đầu vào sẽ được tải xuống thư mục `input/{version}`, và đầu ra sẽ được lưu vào thư mục `output/{version}`.

### Ví Dụ Sử Dụng

- Để chạy script với phiên bản `2.5` và tải xuống tệp:
  ```bash
  python3 main.py --version 2.5
  ```

- Để chạy script với phiên bản `2.5` và bỏ qua việc tải xuống tệp:
  ```bash
  python3 main.py --version 2.5 --skip-download
  ```

- Để chạy script với phiên bản `2.5` và tải xuống các tệp cho các ngôn ngữ cụ thể (ví dụ: EN và JP):
  ```bash
  python3 main.py --version 2.5 --languages EN JP
  ```

## Đóng Góp

Chúng tôi hoan nghênh các đóng góp! Bạn có thể:
- Gửi pull request cho các tính năng mới hoặc sửa lỗi.
- Báo cáo bất kỳ vấn đề nào qua trình theo dõi vấn đề.
- Đảm bảo rằng tất cả các đóng góp đều bao gồm kiểm tra và tài liệu liên quan.

## Giấy Phép

Dự án này được cấp phép theo Giấy Phép MIT. Xem tệp [LICENSE](LICENSE) để biết thêm thông tin.
