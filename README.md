# NotAlone.py
Web-API for [notalone.tv](https://notalone.tv) website with joint viewing of anime, movies

## Example
```python3
# simple login and getting user_id
import notalone
NEclient = notalone.NotAloneClient()
NEClient.login(login="login", password="password")
print(f"-- Account user_id is::: {client.user_id}")
```
