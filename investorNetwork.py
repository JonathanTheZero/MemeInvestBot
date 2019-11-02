import praw
import time
import requests
import random
import threading
import pdb
import re
import os
import datetime

class account:

    def __init__(self, reddit, maxInvestments, name, gamble, sleep):
        self.reddit = reddit
        self.maxInvestments = maxInvestments
        self.name = name
        self.gamble = gamble - 1
        self.sleep = sleep

    def invest(self, sID):
        #print("Start")
        submission = self.reddit.submission(id=sID)
        elm = ["https://meme.market/api/investor/", str(self.name), "/investments?page=0&per_page=12"]
        investmentsData = (requests.get(''.join(elm)).json())
        investmentsThisDay = 0
        for investments in investmentsData:
            #print("Inv check with", self.name)
            investmentDate = time.time() - investments["time"]
            if investmentDate <= 86400:
                investmentsThisDay += 1
                #print(investmentDate, "hmmm", investmentsThisDay)

        #print("hmmm", investmentsThisDay)
        elm2 = ['https://meme.market/api/investor/', str(self.name)]
        url = (requests.get(''.join(elm2)).json())
        s1 = (url['balance'])
        nw = (url['networth'])
        #print("bal check")
        dt = datetime.datetime.now()
        timeNow = dt.hour * 60 * 60 + dt.minute * 60 + dt.second + 7200
        if self.sleep and (timeNow >= 84600 or timeNow <= 24000):
            if datetime.datetime.today().weekday() >= 5:
                print("No investment with ", self.reddit.user.me(use_cache=True), " because of sleep schedule")
                return
            if timeNow < 18000:
                print("No investment with ", self.reddit.user.me(use_cache=True), " because of sleep schedule")
                return
        if investmentsThisDay <= self.maxInvestments:
            sback = s1
            #print("Layer 1")
            if nw == sback:
                for comment in submission.comments:
                    #print("Layer 2")
                    if "INVESTMENTS GO HERE - ONLY DIRECT REPLIES TO ME WILL BE PROCESSED" in comment.body:
                        #print("layer 3")
                        if random.randint(0, 99) > self.gamble:
                            time.sleep(random.randint(0, 7))
                            #print("Layer 4")
                            s3 = (url["networth"])
                            if s3 > 7000000000000000:
                                s2 = s3 - random.randint(2, 17)
                                elm = ["!invest ", str(s2)]
                                fin = "".join(elm)
                                comment.reply(fin)
                            else:
                                comment.reply("!invest 100%")
                            print('Invested at ', submission.score, " Upvotes with ", self.reddit.user.me(use_cache=True))
                            return
                        print("No investment with ", self.reddit.user.me(use_cache=True), " because of coincidence")
                        return
            print("No investment with ", self.reddit.user.me(use_cache=True), " because of balance")
            return
        print("No investment with ", self.reddit.user.me(use_cache=True), "because of max investments")
        return
        #print("finished")

zero = praw.Reddit(client_id="",
                   client_secret="",
                   password="",
                   username="JonathanTheZero",
                   user_agent="MemeInvestor Bot 2.0")
ZeroAcc = account(zero, 5, "JonathanTheZero", 10, True)
#.... for as many accounts as needed


subreddit = zero.subreddit("MemeEconomy")

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

while True:
    #print("Loop")
    for submission in subreddit.new():
        #print("Searching")
        seconds = time.time()
        age = seconds - submission.created_utc
        if submission.num_comments >= random.randint(28, 36) and age <= 180 and submission.id not in posts_replied_to:
            time.sleep(random.randint(0, 30))
            print()
            print("-----------------------------------")
            print("Post:", submission.title)
            print("Author:", submission.author)
            print("Comment amount:", submission.num_comments)
            print("-----------------------------------")

            tList = [
                threading.Thread(target=ZeroAcc.invest(submission.id)),
                threading.Thread(target=a2.invest(submission.id)),
                threading.Thread(target=a3.invest(submission.id)),
                threading.Thread(target=a4.invest(submission.id))
                #etc...
                ]
            posts_replied_to.append(submission.id)
            with open("posts_replied_to.txt", "w") as f:
                for post_id in posts_replied_to:
                    f.write(post_id + "\n")
            for tElm in tList:
                tElm.start()