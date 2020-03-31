import requests


secret = "man0FSkj7cMy0bsMEvoNGqljU6s"
App_id = "5gzPGdfoQpiZwA"
uname = "pilTrader"
pwd = "V!hiymfB38zU46t"
base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': uname, 'password': pwd}
auth = requests.auth.HTTPBasicAuth(App_id, secret)
r = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': 'APP-NAME by REDDIT-USERNAME'},
		  auth=auth)
d = r.json()

token = 'bearer ' + d['access_token']

base_url = 'https://oauth.reddit.com'

headers = {'Authorization': token, 'User-Agent': 'APP-NAME by REDDIT-USERNAME'}
response = requests.get(base_url + '/api/v1/me', headers=headers)

if response.status_code == 200:
    print(response.json()['name'], response.json()['comment_karma'])

fields = list()
fields = ('display_name',
          'title',
          'active_user_count',
          'display_name_prefixed',
          'subscribers', ' name ',
          'public_description',
          'submit_text')
# Searching for keywords
keyword = input("Search Keyword: ")
payload = {'q': keyword, 'limit': 10, 'sort': 'new'}
response = requests.get(base_url + '/subreddits/search', headers=headers, params=payload)
values = response.json()
# print(response.text)
for i in range(len(values['data']['children'])):
    # for j in range(values['data']['children'][i]['data']):
        # print(values['data']['children'][i]['data'][j])
    # print(values['data']['children'][i])
    for j in values['data']['children'][i]['data']:
        item_key = j
        key_value = values['data']['children'][i]['data'][j]
        if item_key in fields and (key_value!="" or key_value == "None"):
            print("  ", item_key , ":" , key_value )
        # print(j)

    # print(values['data']['children'][i]['data']['header_title'])

# for content in response:
#     print(response.t)
