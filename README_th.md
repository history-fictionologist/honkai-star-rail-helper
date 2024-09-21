# honkai-star-rail-helper

`honkai-star-rail-helper` เป็นยูทิลิตี้ที่ออกแบบมาเพื่อจัดการและประมวลผลข้อมูลตัวละคร ทักษะ และคำแนะนำเกี่ยวกับอาวุธโบราณสำหรับวิดีโอเกม [Honkai: Star Rail](https://en.wikipedia.org/wiki/Honkai:_Star_Rail) โดยจะอ่านไฟล์อินพุต ประมวลผลคุณลักษณะต่างๆ เช่น ข้อมูลตัวละครและชุดทักษะ จากนั้นส่งผลลัพธ์ออกมาในรูปแบบที่จัดระเบียบ ข้อมูลอินพุตจะถูกนำมาจากแพ็กเกจอัปเดตอย่างเป็นทางการในที่เก็บข้อมูล [StarRailData](https://github.com/Dimbreath/StarRailData/tree/master) และผลลัพธ์จะถูกจัดเก็บในโฟลเดอร์ตามเวอร์ชันเพื่อการจัดการที่ง่ายดาย

## ตารางตัวละครล่าสุด
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

## คุณสมบัติหลัก
- ดาวน์โหลดข้อมูลตัวละคร, CV, ชุดทักษะ และคำแนะนำเกี่ยวกับอาวุธโบราณโดยอัตโนมัติ
- ประมวลผลและจัดระเบียบข้อมูลลงในไดเร็กทอรีอินพุต/เอาต์พุตที่เวอร์ชันกำหนด
- กำหนดค่าหมายเลขเวอร์ชันผ่านบรรทัดคำสั่งสำหรับการอัปเดตใหม่แต่ละครั้ง

## ข้อกำหนด

ตรวจสอบให้แน่ใจว่าคุณมี:
- **Python 3.8+** (ยืนยันด้วย `python3 --version`).
- แพ็กเกจ Python ที่ระบุใน `requirements.txt`.

## การติดตั้ง

1. **โคลนที่เก็บข้อมูล:**
   ```bash
   git clone https://github.com/yourusername/hsr-helper.git
   cd hsr-helper
   ```

2. **(ทางเลือก) สร้างและเปิดใช้งานสภาพแวดล้อมเสมือน:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # บน Windows: venv\Scriptsctivate
   ```

3. **ติดตั้งแพ็กเกจที่จำเป็น (ยังไม่จำเป็นต้องติดตั้งแพ็กเกจเพิ่มเติม):**
   ```bash
   # ยังไม่จำเป็นต้องติดตั้งแพ็กเกจตอนนี้ แต่หากจำเป็นในอนาคต:
   # pip install -r requirements.txt
   ```

## วิธีใช้งาน

### รันเครื่องมือ
   ไปยังไดเร็กทอรี `src/` และรันสคริปต์หลักพร้อมหมายเลขเวอร์ชันที่ต้องการ:
   ```bash
   cd src
   python3 main.py --version <version_number> [--skip-download]
   ```

   - แทนที่ `<version_number>` ด้วยเวอร์ชันปัจจุบัน (เช่น `2.5`).
   - หากคุณต้องการข้ามการดาวน์โหลดไฟล์ ให้เพิ่มตัวเลือก `--skip-download`.

   ไฟล์อินพุตจะถูกดาวน์โหลดไปยังโฟลเดอร์ `input/{version}` และผลลัพธ์จะถูกบันทึกในโฟลเดอร์ `output/{version}`.

### ตัวอย่างการใช้งาน

- เพื่อรันสคริปต์ด้วยเวอร์ชัน `2.5` และดาวน์โหลดไฟล์:
  ```bash
  python3 main.py --version 2.5
  ```

- เพื่อรันสคริปต์ด้วยเวอร์ชัน `2.5` และข้ามการดาวน์โหลดไฟล์:
  ```bash
  python3 main.py --version 2.5 --skip-download
  ```

- เพื่อรันสคริปต์ด้วยเวอร์ชัน `2.5` และดาวน์โหลดไฟล์สำหรับภาษาที่ระบุ (เช่น EN และ JP):
  ```bash
  python3 main.py --version 2.5 --languages EN JP
  ```

## การสนับสนุน

เรายินดีรับการสนับสนุน! คุณสามารถ:
- ส่ง pull request สำหรับฟีเจอร์ใหม่หรือการแก้ไขบั๊ก.
- รายงานปัญหาผ่านตัวติดตามปัญหา.
- ตรวจสอบให้แน่ใจว่าการสนับสนุนทั้งหมดมีการทดสอบและเอกสารที่เกี่ยวข้อง.

## ใบอนุญาต

โครงการนี้ได้รับอนุญาตภายใต้ใบอนุญาต MIT ดูไฟล์ [LICENSE](LICENSE) สำหรับข้อมูลเพิ่มเติม.
