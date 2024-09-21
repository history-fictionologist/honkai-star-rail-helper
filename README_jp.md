# honkai-star-rail-helper

honkai-star-rail-helperは、ビデオゲーム [Honkai: Star Rail](https://en.wikipedia.org/wiki/Honkai:_Star_Rail) のキャラクターデータ、スキル、および遺物の推奨を管理および処理するためのユーティリティです。入力ファイルを読み取り、キャラクター情報やスキルセットなどのさまざまな属性を処理し、結果を整理された形式で出力します。入力データは、[StarRailData](https://github.com/Dimbreath/StarRailData/tree/master) リポジトリの公式アップデートパッケージから取得され、出力はバージョン別のフォルダに保存され、管理が容易です。

## 最新のキャラクターテーブル
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

## 主な機能
- キャラクターデータ、CV、スキルセット、遺物の推奨を自動的にダウンロード。
- データをバージョンごとに整理された入力/出力ディレクトリに処理。
- 各新しいアップデート用のバージョン番号をコマンドラインで設定可能。

## 必要条件

以下を確認してください:
- **Python 3.8以上** ( `python3 --version` で確認)。
- `requirements.txt` に記載されている必要なPythonパッケージ。

## インストール

1. **リポジトリをクローン:**
   ```bash
   git clone https://github.com/yourusername/hsr-helper.git
   cd hsr-helper
   ```

2. **(オプション) 仮想環境を作成して有効化:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windowsの場合: venv\Scriptsctivate
   ```

3. **依存関係をインストール (現在は追加の依存関係は不要):**
   ```bash
   # 現時点では依存関係をインストールする必要はありませんが、将来的に必要な場合は以下を実行します:
   # pip install -r requirements.txt
   ```

## 使用方法

### ツールの実行
   `src/` ディレクトリに移動し、希望するバージョン番号でメインスクリプトを実行します:
   ```bash
   cd src
   python3 main.py --version <version_number> [--skip-download]
   ```

   - `<version_number>` を現在のバージョンに置き換えます (例: `2.5`)。
   - ファイルのダウンロードをスキップしたい場合は、 `--skip-download` フラグを追加します。

   入力ファイルは `input/{version}` フォルダにダウンロードされ、出力は `output/{version}` フォルダに保存されます。

### 使用例

- バージョン `2.5` でスクリプトを実行し、ファイルをダウンロードする場合:
  ```bash
  python3 main.py --version 2.5
  ```

- バージョン `2.5` でスクリプトを実行し、ファイルのダウンロードをスキップする場合:
  ```bash
  python3 main.py --version 2.5 --skip-download
  ```

- バージョン `2.5` でスクリプトを実行し、特定の言語 (例: ENとJP) のファイルをダウンロードする場合:
  ```bash
  python3 main.py --version 2.5 --languages EN JP
  ```

## コントリビュート

貢献を歓迎します! 次のことが可能です:
- 新機能やバグ修正のプルリクエストを提出する。
- 問題トラッカーを介して問題を報告する。
- すべての貢献にはテストおよび関連するドキュメントを含めてください。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。詳細については [LICENSE](LICENSE) ファイルを参照してください。
