# simple login and getting user_id
import notalone
NEclient = notalone.NotAloneClient()
NEClient.login(login="login", password="password")
print(f"-- Account user_id is::: {client.user_id}")
