# AI Background Remover

商品写真や人物写真から背景を取り除き、透過PNGを一括生成する画像処理ツールです。`rembg` のU²-Netモデルを利用し、元の画像を残したまま出力します。

## 主な機能

- JPG・PNGなど複数画像をまとめて処理
- 入力名に `_transparent.png` を付けた透過PNGを出力
- 同名ファイルがある場合は上書きを防止

## セットアップ
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py --help
python -m unittest -v
```

## 使い方

`python app.py photo.jpg product.png --output output` のように入力画像を並べて指定します。出力先フォルダは必要に応じて自動作成されます。

初回はモデル取得のためネット接続が必要です。人物・商品など前景が明確な画像での利用を想定しています。

Python 3.10+ 推奨。モデル推論は環境ごとに確認してください。
