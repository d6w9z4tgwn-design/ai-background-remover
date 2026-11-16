# ai-background-remover

rembgによる背景除去。初回モデル取得にネット接続が必要。

Remove backgrounds with rembg; first run downloads model weights.

## Setup / 起動
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py --help
python -m unittest -v
```

## Usage / 使用例
`python app.py photo.jpg --output output` — モデル推論未検証 / Model inference not verified.

Python 3.10+ recommended. AI-generated development assistance was used.
