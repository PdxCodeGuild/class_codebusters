#----------------------------------------------------#
# *'-.-'*'-.-'(👍≖‿‿≖)👍 👍(≖‿‿≖👍)*'-.-'*'--'*#
# 
#          Project: Python request system
#          Version: 0.1
#          Author: Calen Ray
#          Email: Calen.w.ray@gmail.com
#          Date: 05/7/21
#----------------------------------------------------#

# Target url      https://cod.tracker.gg/cold-war/profile/battlenet/crayfish%2311592/mp

# e128ce15-cb17-413f-ab3f-cf4c39ef5048

from requests.auth import HTTPBasicAuth
import requests

# api_key = 'e128ce15-cb17-413f-ab3f-cf4c39ef5048'
# auth = HTTPBasicAuth('TRN-Api-Key', 'e128ce15-cb17-413f-ab3f-cf4c39ef5048')

# # x = requests.get('https://public-api.tracker.gg/v2/overwatch/standard/profile/battlenet/BeeZee#11551', auth=auth)
# print(auth)
# # print(x)




s = requests.Session()
s.headers.update({'TRN-Api-Key': 'e128ce15-cb17-413f-ab3f-cf4c39ef5048'})
r = s.get('https://public-api.tracker.gg/v2/overwatch/standard/profile/battlenet/Crayfish#11592')
print(r)


