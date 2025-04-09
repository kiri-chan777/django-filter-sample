# Django従業員管理システム

Djangoを使ったシンプルな従業員管理システムのサンプルです。
フィルタリング機能とExcel出力機能を実装しています。

## 機能

- 従業員データの表示
- 複数条件での検索フィルタリング
- フィルタリングされたデータのExcel出力
- ページネーション

## 環境構築

1. リポジトリをクローンしてフォルダ移動
```bash
cd employee-manager
```

仮想環境を作成して有効化
```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
```

依存パッケージをインストール

```bash
pip install -r requirements.txt
```

マイグレーションを実行

```bash
python manage.py migrate
```

テストデータを作成（オプション）

```bash
python manage.py create_test_data
```

管理者ユーザーを作成

```bash
python manage.py createsuperuser
```
開発サーバーを起動

```bash
python manage.py runserver
```

### 使い方

- ブラウザで http://127.0.0.1:8000/ にアクセスして従業員一覧画面を表示
- フィルタフォームを使って検索条件を指定
- Excel出力ボタンでフィルタリングされたデータをExcel形式でダウンロード
- 管理画面は http://127.0.0.1:8000/admin/ でアクセス可能
