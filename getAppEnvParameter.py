import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.mgmt.web import WebSiteManagementClient

# .envファイルから環境変数を読み込む
load_dotenv()

# 認証情報とサブスクリプションIDを取得
credential = DefaultAzureCredential()
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")

# WebSiteManagementClientの初期化
web_client = WebSiteManagementClient(credential, subscription_id)

# App Service名とリソースグループ名を指定
resource_group_name = "Test"
app_service_name = "TESTABC"

# アプリケーション設定（環境変数）を取得
app_settings = web_client.web_apps.list_application_settings(resource_group_name, app_service_name)
settings = app_settings.properties

# 環境変数を出力
print("Azure App Service 環境変数:")
for key, value in settings.items():
    print(f"{key}: {value}")
    

# 環境変数を登録
env_settings = {
    "ENV1": "value1",
    "ENV2": "value2",
    "ENV3": "value3",   
}

# 既存の環境変数と入れ替えてしまう
update_settings = {"properties": env_settings}

# 環境変数を設定
web_client.web_apps.update_application_settings(resource_group_name, app_service_name, update_settings)
