
import csv
with open('listaTweets.csv', 'rb') as f:
content = f.readlines()
for l in content:
    x = ""+str(l.decode("utf-8"))
    l = x.replace("\n", "")
    try:
        client.update_status(l)
        print("+",l)
        time.sleep(10)
    except tweepy.error.TweepError:
        print("-",l)
        time.sleep(1)
