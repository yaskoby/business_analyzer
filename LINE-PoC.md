# LINE × Make × OpenAI × Google Sheets

## PoC（検証）実施内容まとめ

---

# ■ 1. 目的

LINEから入力された内容を自動で処理し、
顧客情報としてスプレッドシートへ登録する仕組みの検証を行う。

---

# ■ 2. 全体構成

```text
LINE
↓
Make（Webhook）
↓
OpenAI（情報抽出）
↓
JSON整形
↓
Parse JSON
↓
Google Sheets（データ保存）
```

---

# ■ 3. 実施ステップ

---

## ■ STEP1：MakeでWebhook作成

・Makeで新規Scenarioを作成
・Webhooks → Custom Webhookを選択
・Webhook URLを発行

👉 外部からデータを受け取る入口を作成

---

## ■ STEP2：Postmanによるテスト

・Webhook URLへPOST送信
・JSON形式でテストデータ送信

```json
{
  "text": "山田 太郎 ウイスキー好き"
}
```

👉 Webhookでデータ受信確認

---

## ■ STEP3：Webhookデータ確認

・MakeのRun onceで待機
・Postman送信
・Webhookの受信データを確認

👉 「text」が取得できることを確認

---

## ■ STEP4：OpenAI連携

・OpenAIモジュールを追加
・入力テキストを渡す

■ System設定（重要）

・JSON形式で出力させる
・コードブロック（```json）を禁止

👉 Parse JSONで扱える形式にするため

---

## ■ STEP5：JSON形式での出力

例：

```json
{
  "名前": "山田 太郎",
  "好み": "ウイスキー"
}
```

👉 データ構造を固定化

---

## ■ STEP6：Parse JSON設定

・JSONモジュール追加
・Schemaを生成
・OpenAI出力をパース

👉 データを個別項目として扱えるようにする

---

## ■ STEP7：Google Sheets連携

・Google Sheetsモジュール追加
・Add a rowを選択
・各カラムにJSONデータをマッピング

👉 スプレッドシートへ自動保存

---

## ■ STEP8：動作確認

・Run once実行
・Postman送信
・シートにデータ反映確認

👉 一連の流れが正常動作することを確認

---

## ■ STEP9：LINE連携

・LINE公式アカウント作成
・Messaging API有効化
・Webhook URLを設定

👉 LINEからMakeへデータ送信

---

## ■ STEP10：LINE入力データ処理

・LINEメッセージ構造を確認

```text
body.events[0].message.text
```

👉 OpenAI入力を修正

---

## ■ STEP11：LINE動作確認

・Run once実行
・LINEでメッセージ送信
・Makeで受信確認

👉 LINE → Makeの接続確認

---

## ■ STEP12：JSONエラー対応

問題：
・```json付きで返却される

対策：
・Systemプロンプトで禁止

👉 Parse JSONエラー解消

---

## ■ STEP13：Google Sheets反映確認

・LINE入力 → Sheets登録成功

👉 一連のフロー完成

---

# ■ 4. 技術的なポイント

---

## ■ JSON構造の重要性

・AI出力はそのまま使わない
・必ず構造化する

---

## ■ 中間処理の必要性

・OpenAI → Parse JSON → Sheets
👉 直接連携しない

---

## ■ Webhook理解

・外部入力の入口として機能

---

## ■ データパス理解

・text（Postman）
・body.events[0].message.text（LINE）

---

# ■ 5. トラブルと解決

---

## ■ JSONパースエラー

原因：
・コードブロック付き

対応：
・Systemで禁止

---

## ■ Sheetsに書き込まれない

原因：
・カラム未設定

---

## ■ Webhook受信できない

原因：
・Run once未実行

---

## ■ LINE連携できない

原因：
・応答メッセージON
・Webhook未設定

---

# ■ 6. 今後の課題

---

## ■ 音声入力対応

・音声 → 文字起こし（STT）
・精度問題あり

---

## ■ エラーハンドリング

・正常 / 要確認 / エラー分岐

---

## ■ データ精度

・名前 / 銘柄 / 会社名の誤認識

---

## ■ 配信機能

・出勤表配信
・セグメント配信

---

# ■ 7. 学び

---

・AIはそのまま使えない
・構造化が重要
・エラー前提で設計する
・小さく作ると確実に進む

---

# ■ 8. まとめ

今回のPoCで

👉 入力 → AI処理 → データ保存

の基本構造を実装できた

---

# ■ 最重要ポイント

👉 完璧を目指さない
👉 動くものを作る
👉 徐々に改善する

---

# ■ 一言

このPoCは

👉 実務システムの基礎そのもの
