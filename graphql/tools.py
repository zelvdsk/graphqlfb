import requests
import re, json
from .utils import payload, Response
from .config import graphql_url
from typing import Union

class Tools:
    def __init__(self, session: object=None, cookie: Union[str, dict]=None) -> None:
        self.session = session or requests.session()

        if cookie:
            if isinstance(cookie, dict): self.session.cookies.update(cookie)
            elif isinstance(cookie, str): self.session.cookies['cookie'] = cookie

    def search_people(self, name: str, cursor: str=None) -> Response:
        source = self.session.get('https://web.facebook.com/search/people/?q='+ name, allow_redirects=True).text
        data = payload(source=source)
        data.update({'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'SearchCometResultsPaginatedResultsQuery','doc_id': '8787212811373588','variables': json.dumps({"allow_streaming":False,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":False,"high_confidence_config":None,"intercept_config":None,"sts_disambiguation":None,"watch_config":None},"context":{"bsid":"c2981a03-c5df-4e5f-8582-add003504b0b","tsid":None},"experience":{"client_defined_experiences":["ADS_PARALLEL_FETCH"],"encoded_server_defined_params":None,"fbid":None,"type":"PEOPLE_TAB"},"filters":[],"text": name},"count":5,"cursor": cursor,"feedLocation":"SEARCH","feedbackSource":23,"fetch_filters":True,"focusCommentID":None,"locale":None,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"search_results_page","scale":3,"stream_initial_count":0,"useDefaultActor":False,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":False,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":True,"__relay_internal__pv__IsWorkUserrelayprovider":False,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":False,"__relay_internal__pv__IsMergQAPollsrelayprovider":False,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":False,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":False,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":True,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":False,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":False})})

        post = self.session.post(graphql_url, data=data).text
        open('/sdcard/x.htm', 'w').write(str(post))
        if 'ENTITY_USER' in post:
            id = list(set(re.findall(r'User","id":"(.*?)"', post)))
            name = list(set(re.findall(r'url":".*?","name":"(.*?)"', post)))
            images = re.findall(r'"profile_picture":{"uri":"(.*?)"', post)

            data = [{'id': id__, 'name': name__, 'images': img__, 'url': 'https://www.facebook.com/'+ id__} for id__, name__, img__ in zip(id, name, images)]
            return Response(success=True, data=data, message=None, cursor=re.search(r'end_cursor":"(.*?)"', post).group(1))
        else:
            return Response(success=False, message='AttributeError! please check your account.')
    
    def search_group(self, name: str, public: bool=False, cursor: str=None) -> Response:
        source = self.session.get('https://web.facebook.com/search/people/?q='+ name, allow_redirects=True).text
        data = payload(source=source)
        filters = [{"name":"public_groups","args":""}] if public is True else []
        variables = {"allow_streaming":False,"args":{"callsite":"comet:groups_search","config":{"exact_match":False,"high_confidence_config":None,"intercept_config":None,"sts_disambiguation":None,"watch_config":None},"context":{"bsid":"03b28844-4746-4d17-9113-b3b898784c37","tsid":"0.43653449329620897"},"experience":{"client_defined_experiences":["ADS_PARALLEL_FETCH"],"encoded_server_defined_params":None,"fbid":None,"type":"GROUPS_TAB_GLOBAL_GROUPS"},"filters":filters,"text":name},"count":5,"cursor":cursor,"feedLocation":"SEARCH","feedbackSource":23,"fetch_filters":True,"focusCommentID":None,"locale":None,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"search_results_page","scale":3,"stream_initial_count":0,"useDefaultActor":False,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":False,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":False,"__relay_internal__pv__IsWorkUserrelayprovider":False,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":False,"__relay_internal__pv__IsMergQAPollsrelayprovider":False,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":True,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":False,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":True,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":False,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":False}
        data.update({'fb_api_req_friendly_name': 'SearchComietResultsPaginatedResultsQuery','variables': json.dumps(variables),'doc_id': '8787212811373588'})

        string = self.session.post(graphql_url, data=data).text
        resp = Response(**json.loads(string))
        if 'ENTITY_GROUPS' in string:
            data = [{'id': profiles.relay_rendering_strategy.view_model.profile.id, 'url': profiles.relay_rendering_strategy.view_model.profile.url, 'name': profiles.relay_rendering_strategy.view_model.profile.name, 'images': profiles.relay_rendering_strategy.view_model.profile.profile_picture.uri, 'desc_text': profiles.relay_rendering_strategy.view_model.primary_snippet_text_with_entities.text} for profiles in resp.data.serpResponse.results.edges]
            return Response(success=True, data=data, message=None, cursor=re.search(r'end_cursor":"(.*?)"', string).group(1))
        else:
            return Response(success=False, message='AttributeError! please check your account.')

if __name__ == "__main__":
    c = 'dpr=2.278899669647217; sb=b3tWZ4BY77fFaq5mHMkdo0aA; ps_l=1; ps_n=1; datr=NcRWZ0yByL9QJ6G-jUORCEZj; wd=967x1842; c_user=61569828290586; xs=24%3AlW3_m8qabUHlXQ%3A2%3A1733833856%3A-1%3A-1; fr=1B08EMH5sze4WW9ss.AWXZ0u8838rFwQ0ab_Js5UH_20M.BnVsQ6..AAA.0.0.BnWDSC.AWW9zwSRoBQ; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1733833864558%2C%22v%22%3A1%7D'
    x = Tools(cookie=c)
    print(x.search_people(name='Anggi'))
