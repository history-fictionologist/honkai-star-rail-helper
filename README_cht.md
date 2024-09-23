# honkai-star-rail-helper

`honkai-star-rail-helper` 是一個用於管理和處理角色數據、技能和遺物推薦的實用工具，適用於視頻遊戲 [Honkai: Star Rail](https://en.wikipedia.org/wiki/Honkai:_Star_Rail)。它讀取輸入文件，處理各種屬性，如角色信息和技能集，並以有組織的格式輸出結果。輸入數據來自於 [StarRailData](https://github.com/Dimbreath/StarRailData/tree/master) 倉庫的官方更新包，輸出文件則存儲在版本特定的文件夾中以便於管理。

## 最新角色表
<!-- CHARACTER_TABLE_START -->
| DAMAGE_TYPE | RARITY | DESTRUCTION               | THE_HUNT  | ERUDITION | HARMONY   | NIHILITY                  | PRESERVATION       | ABUNDANCE  |
|-------------|--------|---------------------------|-----------|-----------|-----------|---------------------------|--------------------|------------|
| PHYSICAL    | 5      | clara\|player\|yunli      | boothill  | argenti   | robin     |                           |                    |            |
| PHYSICAL    | 4      |                           | sushang   |           | hanya     | luka                      |                    | natasha    |
| FIRE        | 5      | sam                       | topaz     | himeko    |           | jiaoqiu                   | player2            | lingsha    |
| FIRE        | 4      | hook                      |           |           | asta      | guinaifen                 |                    | gallagher  |
| ICE         | 5      | jingliu                   | yanqing   |           | ruanmei   |                           | gepard             |            |
| ICE         | 4      | misha                     |           | herta     |           | pela                      | mar7th             |            |
| LIGHTENING  | 5      |                           |           | jingyuan  |           | acheron\|kafka            |                    | bailu      |
| LIGHTENING  | 4      | arlan                     | moze      | serval    | tingyun   |                           |                    |            |
| WIND        | 5      | blade                     | feixiao   |           | bronya    | blackswann                |                    | huohuo     |
| WIND        | 4      |                           | danheng   |           |           | sampo                     |                    |            |
| QUANTUM     | 5      |                           | seele     | jade      | sparkle   | silverwolf                | fuxuan             |            |
| QUANTUM     | 4      | xueyi                     |           | qingque   |           |                           |                    | lynx       |
| IMAGINARY   | 5      | danhengil                 | drratio   |           | player3   | welt                      | aventurine         | luocha     |
| IMAGINARY   | 4      |                           | mar7th2   |           | yukong    |                           |                    |            |
<!-- CHARACTER_TABLE_END -->

## 主要功能
- 自動下載角色數據、CV、技能集和遺物推薦。
- 將數據處理並組織到版本化的輸入/輸出目錄中。
- 每次更新時可以通過命令行配置版本號。

## 要求

確保你有以下內容：
- **Python 3.8+**（使用 `python3 --version` 確認）。
- `requirements.txt` 中列出的必要 Python 包。

## 安裝

1. **克隆倉庫：**
   ```bash
   git clone https://github.com/yourusername/hsr-helper.git
   cd hsr-helper
   ```

2. **（可選）創建並激活虛擬環境：**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scriptsctivate
   ```

3. **安裝依賴（當前不需要額外依賴）：**
   ```bash
   # 暫時不需要安裝依賴，但如果將來需要：
   # pip install -r requirements.txt
   ```

## 使用

### 運行工具
   進入 `src/` 目錄，並使用所需的版本號運行主腳本：
   ```bash
   cd src
   python3 main.py --version <version_number> [--skip-download]
   ```

   - 將 `<version_number>` 替換為當前版本（如 `2.5`）。
   - 如果你想跳過文件下載，添加 `--skip-download` 選項。

   輸入文件將下載到 `input/{version}` 文件夾，輸出將保存到 `output/{version}` 文件夾。

### 使用示例

- 使用版本 `2.5` 並下載文件：
  ```bash
  python3 main.py --version 2.5
  ```

- 使用版本 `2.5` 並跳過文件下載：
  ```bash
  python3 main.py --version 2.5 --skip-download
  ```

- 使用版本 2.5 並為特定語言下載文件（如 EN 和 JP）：
  ```bash
  python3 main.py --version 2.5 --languages EN JP
  ```

## 貢獻

歡迎貢獻！你可以：
- 提交新功能或修復錯誤的 Pull Request。
- 通過 Issue 追蹤器報告任何問題。
- 確保所有貢獻都包含測試和相關文檔。

## 許可證

此項目基於 MIT 許可證。更多信息請參見 [LICENSE](LICENSE) 文件。
