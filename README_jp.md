# honkai-star-rail-helper

`honkai-star-rail-helper`は、ビデオゲーム [Honkai: Star Rail](https://en.wikipedia.org/wiki/Honkai:_Star_Rail) のキャラクターデータ、スキル、および遺物の推奨を管理および処理するためのユーティリティです。入力ファイルを読み取り、キャラクター情報やスキルセットなどのさまざまな属性を処理し、結果を整理された形式で出力します。入力データは、[StarRailData](https://github.com/Dimbreath/StarRailData/tree/master) リポジトリの公式アップデートパッケージから取得され、出力はバージョン別のフォルダに保存され、管理が容易です。

## 最新のキャラクターテーブル
<!-- CHARACTER_TABLE_START -->
|    |   | {RUBY_B#かいめつ}壊滅{RUBY_E#}                          | {RUBY_B#じゅんしゅ}巡狩{RUBY_E#}  | {RUBY_B#ちえ}知恵{RUBY_E#}    | {RUBY_B#ちょうわ}調和{RUBY_E#} | {RUBY_B#きょむ}虚無{RUBY_E#}     | {RUBY_B#そんご}存護{RUBY_E#}    | {RUBY_B#ほうじょう}豊穣{RUBY_E#} |
| -- | - | ------------------------------------------------- | -------------------------- | ------------------------- | ------------------------ | --------------------------- | -------------------------- | ------------------------- |
| 物理 | 5 | {RUBY_B#ウンリ}雲璃{RUBY_E#}\|クラーラ\|開拓者                | ブートヒル                      | アルジェンティ                   | ロビン                      |                             |                            |                           |
| 物理 | 4 |                                                   | {RUBY_B#スショウ}素裳{RUBY_E#}   |                           | {RUBY_B#カンア}寒鴉{RUBY_E#}  | ルカ                          |                            | ナターシャ                     |
| 炎  | 5 | ホタル                                               | トパーズ&カブ                    | {RUBY_B#ひめこ}姫子{RUBY_E#}   |                          | {RUBY_B#ショウキュウ}椒丘{RUBY_E#}  | 開拓者                        | {RUBY_B#レイサ}霊砂{RUBY_E#}   |
| 炎  | 4 | フック                                               |                            |                           | アスター                     | {RUBY_B#ケイナイフン}桂乃芬{RUBY_E#} |                            | ギャラガー                     |
| 氷  | 5 | {RUBY_B#ケイリュウ}鏡流{RUBY_E#}                         | {RUBY_B#ゲンキョウ}彦卿{RUBY_E#}  |                           | ルアン・メェイ                  |                             | ジェパード                      |                           |
| 氷  | 4 | ミーシャ                                              |                            | ヘルタ                       |                          | ペラ                          | {RUBY_B#みつき}三月{RUBY_E#}なのか |                           |
| 雷  | 5 |                                                   |                            | {RUBY_B#ケイゲン}景元{RUBY_E#}  |                          | {RUBY_B#よみ}黄泉{RUBY_E#}\|カフカ |                            | {RUBY_B#ビャクロ}白露{RUBY_E#}  |
| 雷  | 4 | アーラン                                              | モゼ                         | セーバル                      | {RUBY_B#テイウン}停雲{RUBY_E#} |                             |                            |                           |
| 風  | 5 | {RUBY_B#ジン}刃{RUBY_E#}                             | {RUBY_B#ヒショウ}飛霄{RUBY_E#}   |                           | ブローニャ                    | ブラックスワン                     |                            | フォフォ                      |
| 風  | 4 |                                                   | {RUBY_B#タンコウ}丹恒{RUBY_E#}   |                           |                          | サンポ                         |                            |                           |
| 量子 | 5 |                                                   | ゼーレ                        | ジェイド                      | {RUBY_B#はなび}花火{RUBY_E#}  | {RUBY_B#ぎんろう}銀狼{RUBY_E#}    | {RUBY_B#フゲン}符玄{RUBY_E#}    |                           |
| 量子 | 4 | {RUBY_B#セツイ}雪衣{RUBY_E#}                           |                            | {RUBY_B#セイジャク}青雀{RUBY_E#} |                          |                             |                            | リンクス                      |
| 虚数 | 5 | {RUBY_B#タンコウ}丹恒{RUBY_E#}・{RUBY_B#インゲツ}飲月{RUBY_E#} | Dr.レイシオ                    |                           | 開拓者                      | ヴェルト                        | アベンチュリン                    | {RUBY_B#ラセツ}羅刹{RUBY_E#}   |
| 虚数 | 4 |                                                   | {RUBY_B#みつき}三月{RUBY_E#}なのか |                           | {RUBY_B#ギョクウ}御空{RUBY_E#} |                             |                            |                           |
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
