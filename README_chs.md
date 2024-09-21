# honkai-star-rail-helper

`honkai-star-rail-helper` 是一个用于管理和处理角色数据、技能和遗物推荐的实用工具，适用于视频游戏 [Honkai: Star Rail](https://en.wikipedia.org/wiki/Honkai:_Star_Rail)。它读取输入文件，处理各种属性，如角色信息和技能集，并以有组织的格式输出结果。输入数据来自于 [StarRailData](https://github.com/Dimbreath/StarRailData/tree/master) 仓库的官方更新包，输出文件则存储在版本特定的文件夹中以便于管理。

## 最新角色表
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

## 主要功能
- 自动下载角色数据、CV、技能集和遗物推荐。
- 将数据处理并组织到版本化的输入/输出目录中。
- 每次更新时可以通过命令行配置版本号。

## 要求

确保你有以下内容：
- **Python 3.8+**（使用 `python3 --version` 确认）。
- `requirements.txt` 中列出的必要 Python 包。

## 安装

1. **克隆仓库：**
   ```bash
   git clone https://github.com/yourusername/hsr-helper.git
   cd hsr-helper
   ```

2. **（可选）创建并激活虚拟环境：**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scriptsctivate
   ```

3. **安装依赖（当前不需要额外依赖）：**
   ```bash
   # 暂时不需要安装依赖，但如果将来需要：
   # pip install -r requirements.txt
   ```

## 使用

### 运行工具
   进入 `src/` 目录，并使用所需的版本号运行主脚本：
   ```bash
   cd src
   python3 main.py --version <version_number> [--skip-download]
   ```

   - 将 `<version_number>` 替换为当前版本（如 `2.5`）。
   - 如果你想跳过文件下载，添加 `--skip-download` 选项。

   输入文件将下载到 `input/{version}` 文件夹，输出将保存到 `output/{version}` 文件夹。

### 使用示例

- 使用版本 `2.5` 并下载文件：
  ```bash
  python3 main.py --version 2.5
  ```

- 使用版本 `2.5` 并跳过文件下载：
  ```bash
  python3 main.py --version 2.5 --skip-download
  ```

- 使用版本 2.5 并为特定语言下载文件（如 EN 和 JP）：
  ```bash
  python3 main.py --version 2.5 --languages EN JP
  ```

## 贡献

欢迎贡献！你可以：
- 提交新功能或修复错误的 Pull Request。
- 通过 Issue 追踪器报告任何问题。
- 确保所有贡献都包含测试和相关文档。

## 许可证

此项目基于 MIT 许可证。更多信息请参见 [LICENSE](LICENSE) 文件。
