from slacker import Slacker
import json, requests
import slackbot_settings

welcomeMessage = """
Welcome kosen11s:+1:\n
#general , #profile , #logo チャンネルには必ず入ってね:heart:\n
他にも #github , #muscle , #nsfw , #skype があるよ！適当に入ってね:raryosu:\n
それとこれが最後！以下のリンクのスキルシートに記入をお願いしてるから記入お願いします！\n
URLはひ・み・つ♡\n
それじゃよろしくね:octocat:
"""

class Member(object):
	memberCount = 0
	def setMember(self):
		data = getJson()
		self.memberCount = len(data['channel']['members'])

def getJson():
	url = 'https://slack.com/api/channels.join'
	parameters = {
					'token' : slackbot_settings.API_TOKEN_TEAM,
					'name' : 'random'}
	r = requests.get(url, params = parameters)
	data = json.loads(r.text)
	mem = Member()
	if mem.memberCount == 0:
		mem.memberCount = len(data['channel']['members'])
	return data

def welcomePost(user):
	slack = Slacker(slackbot_settings.API_TOKEN)
	slack.chat.post_message(
		'random',
		'Hi! ' + user + " " + welcomeMessage,
		as_user = True
	)

if __name__ == '__main__':
	mem = Member()
	mem.setMember()
	while True:
		jsonChannel = getJson()
		if mem.memberCount < len(jsonChannel['channel']['members']):
			print(mem.memberCount)
			mem.memberCount = len(jsonChannel['channel']['members'])
			url = 'https://slack.com/api/users.info'
			parameters = {
							'token' : slackbot_settings.API_TOKEN_TEAM,
							'user' : jsonChannel['channel']['members'][mem.memberCount - 1]}
			r_2 = requests.get(url, params = parameters)
			jsonUser = json.loads(r_2.text)
			welcomePost(jsonUser['user']['name'])
