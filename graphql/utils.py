import re

'Output response Object' 
class Response:
    def __init__(self, **kwargs):
        self.__dict__.update({
            key: self._convert_to_response(value) 
            for key, value in kwargs.items()
        })

    def _convert_to_response(self, value):
        if isinstance(value, dict):
            return Response(**value)
        elif isinstance(value, list):
            return [self._convert_to_response(v) for v in value]
        return value

    def __setattr__(self, key, value):
        self.__dict__[key] = self._convert_to_response(value)

    def __repr__(self):
        return repr(self.__dict__)

'Scraping payload dari source yang diberikan'
def payload(source: str, id: str=None) -> dict:
    id = id or re.search(r'__user=(.*?)\&', source).group(1)
    data = {'av': id,'__aaid': '0','__user': id,'__a': '1','__req': '1w','__hs': re.search('"haste_session":"(.*?)"', source).group(1),'dpr': '3','__ccg': 'EXCELLENT','__rev': '1018714484','__s': 'lvnku4:p0cgbh:wl9j3f','__hsi': re.search(r'"hsi":"(.*?)"', source).group(1),'__dyn': '7xeXxaU5a5Q1ryaxG4Vp41twWwIxu13wFwnUW3q2ibwNw9G2Saw8i2S1DwUx60GE3Qwb-q7oc81EEc87m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewGwkUe9obrwh8lwuEjUlDw-wSU8o4Wm7-2K1yw9q2-VEbUGdG0HE88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13whEeE-3WVU-4EdrxG1fBG2-2K2G0JU','__csr': 'gcccNRgF4n2dNIjckYGdbOibtsBjPiOWH9b5pGcJXqlky7CArAitazlQDApQRnv9KA_bWFpQmGDQDXhFuJ5AhfJDVC7o-fkNQH-2O9UylppaoF2WGfwRUlKaBVfDyEgyEuxGUnCKu9BKEnCwGxa18xS2ebwywCxS3F0EwzG5U5C1aDyE4e7oW0ZE882ZBw6Iwj8c82_U0m7w8a00nHy3K07vA09Lwq82zwaW0bGw1ge04jo09ho0Ki','__comet_req': '15','fb_dtsg': re.search(r'"DTSGInitialData",\[\],\{"token":"(.*?)"', source).group(1),'jazoest': re.search(r'jazoest=(.*?)"', source).group(1),'lsd': re.search(r'\["LSD",\[\],\{"token":"(.*?)"', source).group(1),'__spin_r': re.search(r'"__spin_r":(.*?),', source).group(1),'__spin_b': 'trunk','__spin_t': re.search(r'"__spin_t":(.*?),', source).group(1),'__jssesw': '1','fb_api_caller_class': 'RelayModern','server_timestamps': 'true'}

    return data
