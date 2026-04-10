import anthropic
import os

# API Key設定（test_claude.pyと同じKeyを使用）
os.environ['ANTHROPIC_API_KEY'] = 'YOUR_API_KEY_HERE'

client = anthropic.Anthropic()

# あなたの実際の経験を基にした業務プロセス
process = """
半導体設計において、画素設計からフォトマスクデータ生成までの工程：

1. 設計者が画素レイアウトを設計（回路図からレイアウト作成）
2. DRC（Design Rule Check）を実行してデザインルール違反を確認
3. LVS（Layout vs Schematic）でレイアウトと回路図の一致を確認
4. GDSファイルを生成
5. マスクベンダーに送付

この工程でミスが頻発し、テープアウト後に問題が発覚することがあった。
特に、設計ルール違反の見逃し、データフォーマットの不整合、
バージョン管理ミスなどが主な原因。
"""

prompt = f"""
あなたは28年の半導体業界経験を持つ業務改善コンサルタントです。
過去にフォトマスクミス撲滅プロジェクトを成功させた実績があります。

以下の業務プロセスを分析し、下記を出力してください：

1. **潜在的なミス発生ポイント**（3-5個）
   各ポイントについて、なぜミスが起きやすいか理由も説明

2. **各ポイントに対するチェックリスト項目**
   実務で使える具体的なチェック項目

3. **業務改善の具体的提案**
   自動化、ツール導入、フロー改善など

業務プロセス：
{process}

出力は、エンジニアが実務で使えるよう、具体的かつ実践的な内容にしてください。
"""

print("=" * 70)
print("業務プロセス分析AIアシスタント")
print("=" * 70)
print("\n分析中...\n")

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=3000,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("=" * 70)
print("分析結果")
print("=" * 70)
print(message.content[0].text)
print("\n" + "=" * 70)
print("✅ 分析完了！")
print("=" * 70)