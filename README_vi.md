# honkai-star-rail-helper

honkai-star-rail-helper là một tiện ích được thiết kế để quản lý và xử lý dữ liệu nhân vật, kỹ năng và đề xuất di vật cho trò chơi điện tử [Honkai: Star Rail](https://en.wikipedia.org/wiki/Honkai:_Star_Rail). Nó đọc các tệp đầu vào, xử lý các thuộc tính như thông tin nhân vật và bộ kỹ năng, và xuất kết quả theo định dạng tổ chức. Dữ liệu đầu vào được lấy từ các gói cập nhật chính thức trong kho lưu trữ [StarRailData](https://github.com/Dimbreath/StarRailData/tree/master) và đầu ra được lưu trữ trong các thư mục phân theo phiên bản để dễ dàng quản lý.

## Bảng Nhân Vật Mới Nhất
<!-- CHARACTER_TABLE_START -->
| DAMAGE_TYPE | RARITY | DESTRUCTION        | THE_HUNT | ERUDITION | HARMONY | NIHILITY      | PRESERVATION | ABUNDANCE |
| ----------- | ------ | ------------------ | -------- | --------- | ------- | ------------- | ------------ | --------- |
| PHYSICAL    | 5      | clara|player|yunli | boothill | argenti   | robin   |               |              |           |
| PHYSICAL    | 4      |                    | sushang  |           | hanya   | luka          |              | natasha   |
| FIRE        | 5      | sam                | topaz    | himeko    |         | jiaoqiu       | player2      | lingsha   |
| FIRE        | 4      | hook               |          |           | asta    | guinaifen     |              | gallagher |
| ICE         | 5      | jingliu            | yanqing  |           | ruanmei |               | gepard       |           |
| ICE         | 4      | misha              |          | herta     |         | pela          | mar7th       |           |
| LIGHTENING  | 5      |                    |          | jingyuan  |         | acheron|kafka |              | bailu     |
| LIGHTENING  | 4      | arlan              | moze     | serval    | tingyun |               |              |           |
| WIND        | 5      | blade              | feixiao  |           | bronya  | blackswan     |              | huohuo    |
| WIND        | 4      |                    | danheng  |           |         | sampo         |              |           |
| QUANTUM     | 5      |                    | seele    | jade      | sparkle | silverwolf    | fuxuan       |           |
| QUANTUM     | 4      | xueyi              |          | qingque   |         |               |              | lynx      |
| IMAGINARY   | 5      | danhengil          | drratio  |           | player3 | welt          | aventurine   | luocha    |
| IMAGINARY   | 4      |                    | mar7th2  |           | yukong  |               |              |           |
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
