#!/usr/bin/env python3
import praw
import pdb
import time
import json
import urllib
import requests
import datetime
import random

#general settings



def invest(sID, r):
            submission = r.submission(id=sID)
            for comment in submission.comments:
                    if "INVESTMENTS GO HERE - ONLY DIRECT REPLIES TO ME WILL BE PROCESSED" in comment.body:
                        time.sleep(random.randint(0, 8))
                        elms = ['https://meme.market/api/investor/', str(r.user.me(use_cache=True))]
                        final = "".join(elms)
                        url = (requests.get(final)).json()
                        s1 = (url['balance'])
                        if s1 > 7000000000000000:
                            s2 = s1 - random.randint(3, 15)
                            elm = ["!invest ", str(s2)]
                            fin = "".join(elm)
                            comment.reply(fin)
                        else:
                            comment.reply("!invest 100%")
                        print('Invested at ', submission.score, ' Upvotes in:  "',submission.title,'" by ', submission.author, " with ", r.user.me(use_cache=True))
                        return True   
            return False


reddit = praw.Reddit(client_id="",
                            client_secret="",
                            password="",
                            username="",
                            user_agent="")

reddit2 = praw.Reddit(client_id="",
                            client_secret="",
                            password="",
                            username="",
                            user_agent="")

reddit3 = praw.Reddit(client_id="",
                            client_secret="",
                            password="",
                            username="",
                            user_agent="")

reddit4 = praw.Reddit(client_id="",
                            client_secret="",
                            password="",
                            username="",
                            user_agent="")
       
subreddit = reddit.subreddit('MemeEconomy')
sub2 = reddit2.subreddit('MemeEconomy')
sub3 = reddit3.subreddit('MemeEconomy')
sub4 = reddit4.subreddit('MemeEconomy')

name = ''#add name here

url = (requests.get('https://meme.market/api/investor/' + name).json())
s1 = (url['balance'])
print("Current balance: ", s1)
if s1 < 10000:
    urli = (requests.get('https://meme.market/api/investor/' + name +'/investments?per_page=1&page=0&from=&to=').json())
    s2 = (urli[0]['time'])
    seconds1 = time.time()
    diff1 = seconds1 - s2
    diff2 = 14400 - diff1
    print("Sleeping for ", diff2, " Seconds")
    time.sleep(diff2)
    
while True:
    for submission in subreddit.new():
        seconds = time.time()
        age = seconds - submission.created_utc
        if submission.num_comments >= 30 and age <= 180:
            if invest(submission.id, reddit) and invest(submission.id, reddit2) and invest(submission.id, reddit3) and invest(submission.id, reddit4):
                print("Sleeping started")
                time.sleep(14350)
