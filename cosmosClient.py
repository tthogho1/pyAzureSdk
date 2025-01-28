from azure.cosmos import CosmosClient
import json
import os
import dotenv 

# .envファイルから環境変数を読み込む
dotenv.load_dotenv()

# Cosmos DB接続情報
url = os.getenv("COSMOS_DB_URL")
key = os.getenv("COSMOS_DB_KEY")  
database_name = os.getenv("COSMOS_DB_DATABASE")
container_name = os.getenv("COSMOS_DB_CONTAINER")

# CosmosClientインスタンスの作成
client = CosmosClient(url, credential=key)

# データベースの取得
database = client.get_database_client(database_name)
#container = database.get_container_client("Prom")
container = database.get_container_client(container_name)

# データベース内の全コンテナのリストを取得
# containers_list = database.list_containers()
# containers_listのサイズをチェック
# container_count = sum(1 for _ in containers_list)
#print(f"コンテナ数: {container_count}")

#containers_names = [container['id'] for container in containers_list]

# 各コンテナからデータを取得し、ローカルに保存
#for container_name in containers_names:
query = "SELECT * FROM c"
items = list(container.query_items(query, enable_cross_partition_query=True))

file_name = f'{container_name}.json'
with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False)

print(f"{container_name} のデータのエクスポートが完了しました。ファイル名: {file_name}")
print("全てのコンテナからのデータのエクスポートが完了しました。")
