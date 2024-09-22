from fake_useragent import UserAgent

# pip install fake-useragent
fakeuser = UserAgent(browsers=["chrome"])
print(fakeuser.random)