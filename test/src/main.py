import instaloader

from contexts.user_context import L
from controller.rate_controller import MyRateController

rate_controller = MyRateController(L.context)

L.context._rate_controller = rate_controller

profile = instaloader.Profile.from_username(L.context,'luciano.alcantara.dev')

followers = profile.get_followers()
 
for follower in followers:
   print(follower.followers)