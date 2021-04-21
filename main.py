import statsapi
import pprint

# games = statsapi.schedule(start_date='01/01/2021',end_date='04/19/2021')
# for x in games:
#     print(x)

box = statsapi.boxscore(642138, timecode=None,fieldingInfo=False,pitchingBox=False,gameInfo=False, battingInfo=False)
box = statsapi.boxscore_data(642138, timecode=None)
pp = pprint.PrettyPrinter(indent=4)
d = box.get('homeBatters')
temp = list()
for x in d:
    temp.append([])
print(pp.pprint(d))