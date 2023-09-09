## Flask OCR App
### 概要
このアプリケーションは、FlaskとTesseract OCRを使用して、画像内のテキスト（英語と日本語）を認識する簡単な例です。

### 特徴
英語と日本語のテキスト認識をサポート
アップロードした画像を表示
Dockerでの簡単なデプロイ

### 環境
Python 3.9
Flask 2.0.1
Tesseract OCR
Docker

### セットアップ手順
レポジトリをクローンまたはダウンロードします。
```
git clone [your_repository_url]
```

Dockerイメージをビルドします。
```
docker build -t flask-ocr-app .
```

Dockerコンテナを実行します。
```
docker run -p 5000:5000 flask-ocr-app
```

ブラウザで http://localhost:5000 にアクセスします。

### 使用方法
- ブラウザで表示されたページにて「ファイルを選択」ボタンから画像を選びます。
- 「Upload」ボタンをクリックして画像をアップロードします。
- 画面にはアップロードした画像と、その画像から認識されたテキストが表示されます。

### ライセンス
MIT

このREADMEはあくまで一例です。プロジェクトのニーズに応じて適宜修正や追加を行ってください。