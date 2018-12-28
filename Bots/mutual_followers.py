import json
import time
import os.path
import logging
import argparse
from pprint import pprint

try:
    from instagram_private_api import (
        Client, __version__ as client_version)
except ImportError:
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from instagram_private_api import (
        Client, __version__ as client_version)


if __name__ == '__main__':

    logging.basicConfig()
    logger = logging.getLogger('instagram_private_api')
    logger.setLevel(logging.WARNING)

    # Example command:
    # python examples/savesettings_logincallback.py -u "yyy" -p "zzz" -settings "test_credentials.json"
    parser = argparse.ArgumentParser(description='Mutual follower finder')
    parser.add_argument('-u', '--username', dest='username', type=str, required=True)
    parser.add_argument('-p', '--password', dest='password', type=str, required=True)
    parser.add_argument('-debug', '--debug', action='store_true')
    parser.add_argument('-u1', '--user1', dest='user1', type=str, required=True)
    parser.add_argument('-u2', '--user2', dest='user2', type=str, required=True)
    
    args = parser.parse_args()
    if args.debug:
        logger.setLevel(logging.DEBUG)

    print('Client version: {0!s}'.format(client_version))
    api = Client(args.username, args.password)
    user1 = (api.username_info(args.user1))
    user1_pk = (user1['user']['pk'])
    #print (user1_pk)
    user2 = (api.username_info(args.user2))
    user2_pk = (user2['user']['pk'])
    #print (user2_pk)
    print("Fetching first user's followers.")

    user_id = str((user1['user']['pk']))
    print ((user_id))
    user1_followers = []
    rank_token = Client.generate_uuid()
    results = api.user_followers(user_id, rank_token)
    user1_followers.extend(results.get('users', []))

    next_max_id = results.get('next_max_id')
    while next_max_id:
        results = api.user_followers(user_id, rank_token, max_id=next_max_id)
        user1_followers.extend(results.get('users', []))
        #if len(user1_followers) >= 600:       # get only first 600 or so
        #    break
        next_max_id = results.get('next_max_id')

    user1_followers.sort(key=lambda x: x['pk'])
    # print list of user IDs

    with open('user1.txt', 'w') as g:
        for u in user1_followers:
     #       print(str(u['pk']))
            g.write("%s\n" % str(u['pk']))


    print("Fetching second user's followers.")
    user_id = str((user2['user']['pk']))
    #print ((user_id))
    user2_followers = []
    rank_token = Client.generate_uuid()
    results2 = api.user_followers(user_id, rank_token)
    user2_followers.extend(results2.get('users', []))

    next_max_id = results2.get('next_max_id')
    while next_max_id:
        try:
            results2 = api.user_followers(user_id, rank_token, max_id=next_max_id)
        except Exception as e:
            time.sleep(5)
            results2 = api.user_followers(user_id, rank_token, max_id=next_max_id)
        
        user2_followers.extend(results2.get('users', []))
        #if len(user2_followers) >= 600:       # get only first 600 or so
        #    break
        next_max_id = results2.get('next_max_id')

    user2_followers.sort(key=lambda x: x['pk'])
    # print list of user IDs
    with open('user2.txt', 'w') as f:
        for u in user2_followers:
            print(str(u['pk']))
            f.write("%s\n" % str(u['pk']))
#    print(json.dumps([u['pk'] for u in followers], indent=2))
    print("MUTUAL LIST-------------------")
    mutual_followers = user1_followers  + user2_followers

    dupes = [x for n, x in enumerate(mutual_followers) if x in mutual_followers[:n]]
    with open('mutuals.txt', 'w') as h:
        for user in dupes:
            print(str(user['pk']) + ", " + str(user['username']))
            h.write("%s, %s\n", str(user['pk'], str(user['username'])))






#    pprint(followers)