import requests

headers={
	'Accept': 'application/json',
	'authorization': 'Bearer <token>'
}

def get_user(tag):
	#return user profile info
	response=requests.get('https://api.clashofclans.com/v1/players/%'+tag[1:], headers=headers)
	user_json=response.json()
	info=f'''Name: {user_json['name']}
Tag: #{user_json['tag'][1:]}
TH: {str(user_json['townHallLevel'])}
Attack Wins: {str(user_json['attackWins'])} '''
	for hero in user_json['heroes']:
		info=info+f'''
{hero['name']}: {str(hero['level'])}'''
	return info

def search_clan():
	#submit a clan search
	response=requests.get('https://api.clashofclans.com/v1/clans?name=Friendly%20clan', headers=headers)
	clan_json=response.json()
	for clan in clan_json['items']:
		print(clan['name'] + ":" + str(clan['clanLevel']))
 
