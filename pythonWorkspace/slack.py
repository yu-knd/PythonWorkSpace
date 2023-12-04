import requests
import json
import os

# --環境変数の読み込み--
from dotenv import load_dotenv
load_dotenv()

# --定数--
# APIの基本URL
SLACK_URL = 'https://slack.com/api/'
# postMessageAPIのURL
SLACK_POST_MESSAGE_URL = SLACK_URL + 'chat.postMessage'
# Slack API利用用トークン(.envに定義)
SLACK_APP_TOKEN = os.environ.get('SLACK_APP_TOKEN','')
if SLACK_APP_TOKEN=='':raise ValueError('環境変数[SLACK_APP_TOKEN]が設定されていません。')
# Slack デフォルト送信先チャンネル(.envに定義)
SLACK_SEND_DEFAULT_CHID = os.environ.get('SLACK_SEND_DEFAULT_CHID','')
if SLACK_APP_TOKEN=='':raise ValueError('環境変数[SLACK_SEND_DEFAULT_CHID]が設定されていません。')

# SlackのPostMessageAPI呼び出し処理
# @param msg     :送信メッセージ
# @param chId    :(任意)送信先チャンネルID
# @param username:(任意)表示名
# @return APIからのレスポンス情報
def postMsg(msg,
            chId=os.environ.get('SLACK_SEND_DEFAULT_CHID'),
            username='江永さん',
          ):

  # 引数チェック
  if msg=='':raise ValueError('メッセージ未設定')

  # API呼び出しパラメータ設定
  headers = {
    'Authorization': 'Bearer '+SLACK_APP_TOKEN,
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  data = {
      'channel': chId,
      'text': msg,
      'username':username
  }

  # API呼び出し実行
  response = requests.post(SLACK_POST_MESSAGE_URL, headers=headers, data=data)
  res = response.json()

  # API呼び出しに失敗していた場合エラーとする
  if res.get('ok') != True:
      raise ValueError('FailSlackPostMsg:'+res.get('error'))

  return res

if __name__=="__main__":
    postMsg(msg='Slack送信テスト')