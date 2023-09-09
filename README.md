## Flask OCRアプリ
### 概要
このアプリはFlaskとTesseract OCRを組み合わせた、画像内のテキスト（英語と日本語）を認識するシンプルなアプリケーションです。

### 特徴
- 英語と日本語のテキスト認識をサポート
- アップロードした画像を表示
- Dockerで簡単にデプロイ可能

### 環境
- Python 3.9
- Flask 2.0.1
- Tesseract OCR
- Docker

### セットアップ手順
1. レポジトリをクローンまたはダウンロードします。
    ```bash
    git clone https://github.com/hsasaki12/OCRApp.git
    ```
2. Dockerイメージをビルドします。
    ```bash
    docker build -t flask-ocr-app .
    ```
3. Dockerコンテナを起動します。
    ```bash
    docker run -p 5000:5000 flask-ocr-app
    ```
4. ブラウザで http://localhost:5000 にアクセスします。

### 使用方法
1. ブラウザで表示されたページで「ファイルを選択」ボタンをクリックして画像を選びます。
2. 「Upload」ボタンをクリックして画像をアップロードします。
3. 画面にはアップロードした画像と、その画像から認識されたテキストが表示されます。