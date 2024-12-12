import requests
import re, json
from .utils import payload, Response
from .config import graphql_url
from typing import Union

class Action:
    def __init__(self, session: object=None, cookie: Union[str, dict]=None) -> None:
        self.session = session or requests.session()

        if cookie:
            if isinstance(cookie, dict): self.session.cookies.update(cookie)
            elif isinstance(cookie, str): self.session.cookies['cookie'] = cookie

    def add_friends(self, id: str) -> Response:
        source = self.session.get('https://web.facebook.com', allow_redirects=True).text
        data = payload(source=source)
        data.update({'fb_api_req_friendly_name': 'FriendingCometFriendRequestSendMutation','variables': json.dumps({"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,unexpected,1733913361721,706072,190055527696468,,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,tap_search_bar,1733913356378,947349,391724414624676,,","friend_requestee_ids":[id],"friending_channel":"PROFILE_BUTTON","warn_ack_for_ids":[],"actor_id":data['__user'],"client_mutation_id":"8"},"scale":3}),'doc_id': '9012643805460802',})

        post = self.session.post(graphql_url, data=data).text
        open('/sdcard/x.htm', 'w').write(str(post))

        if 'Batalkan Permintaan' in post:
            return Response(success=True, data={'id': id}, message=None)
        else:
            return Response(success=False, message='Response Error! please check target or your account.')

if __name__ == "__main__":
    c='dpr=2.278899669647217; sb=b3tWZ4BY77fFaq5mHMkdo0aA; ps_l=1; ps_n=1; datr=NcRWZ0yByL9QJ6G-jUORCEZj; c_user=61570113222056; xs=14%3A5xAhl0jN-CWghA%3A2%3A1733913047%3A-1%3A-1; fr=1CRPP6KDkKz4qfy6H.AWVPvD25ltxhqmEWK3HRAJe2_YQ.BnWWUW..AAA.0.0.BnWWnY.AWXPsxJQgzA; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1733913054024%2C%22v%22%3A1%7D; wd=967x1842'
    x = Action(cookie=c)
    x.add_friends(id='61565586448623')      
