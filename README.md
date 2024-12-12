# Facebook Graphql API
# tools
import module/library
```py
from graphql.tools import Tools

# login using cookies
tools = Tools(cookie='cookie string')
```
- Search people<br />
mencari pengguna facebook berdasarkan nama
```py
data = tools.search_people(name='fbname', cursor=None)
# name: str
# cursor: str, default set None
print(data)
```

- Search Group<br />
Mencari group berdasarkan nama
```py
data = tools.search_group(name='groupname', public=False, cursor=None)
# name: str
# public: bool, desc = filter group public only or all group
# cursor: str, default set None
print(data)
```
# action
import module/library
```py
from graphql.action import Action

# login using cookies
action = Action(cookie='cookie string')
```
- Add user<br />
Meminta pertemanan berdasarkan id
```py
data = action.add_friends(id='id user')
print(data)
