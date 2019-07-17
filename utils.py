import json
import requests


def progress_reporter(text, slack_url="https://hooks.slack.com/services/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"):
	'''該当slackチャンネルにメッセージを送信する
	'''
	data = json.dumps({"text": text, "username": 'progress_report'})
	requests.post(slack_url, data=data)
	return