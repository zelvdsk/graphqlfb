# Facebook Graphql API

# tools
import module/library
```py
from tools import Tools
```

- Search people<br />
mencari pengguna facebook berdasarkan nama
```py
data = Tools().search_people(name='fbname', cursor=None)
# name: str
# cursor: str, default set None
# output/data: list

for user in data:
    print(user.name, user.id, user.url, user.images)
```

- Search Group<br />
Mencari group berdasarkan nama
```py
data = Tools().search_group(name='groupname', public=False, cursor=None)
# name: str
# public: bool, desc = filter group public only or all group
# cursor: str, default set None
# output/data: list
```
