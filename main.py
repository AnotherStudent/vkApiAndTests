from urllib.request import urlopen
from urllib.error import *
import json
import pprint

def getUsers(users):
	users = list(users)

	result = list()

	for id in users:
		request = "https://api.vk.com/method/users.get?user_ids={id}&fields=nickname,sex,city,site&v=5.69".format(id = id)

		request_obj = urlopen(request)
		result.append(json.loads(request_obj.read()))

	return result


def main():
	try:
		users = getUsers(['1', '2', '3']);
		pprint.pprint(users)
	# fails
	except URLError:
		print('url error')
	except HTTPError:
		print('uhttp error')
	except:
		print('Unhandled exception')


if __name__ == '__main__':
	main()
