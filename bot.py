import praw
import random
# create the objects from the imported modules

# reddit api login
reddit = praw.Reddit(client_id='redacted',
                     client_secret='redacted',
                     username='SandEnthusiast',
                     password='redacted',
                     user_agent='thisshitdoesntmatterlel')


# the subreddits you want your bot to live on
subreddit = reddit.subreddit('SandLand')

users = ["notabear629", "JustAboutEnoughSpace", "d_140v", "wall-e200", "BIG_DICK_MYSTIQUE", "10messiFH", "Allpaintedbright", "Argus1000", "ArminIsExactlyRight", "Brittneychan", "CHRISTITOonFIRE", "Daylights_New_Hope", "Doom_Hawk", "es452002", "flashlightpoki", "Muckyduck007", "ragnaroksoon", "UnsaturatedSolution", "Verdicious", "Zekes_Coffee_Company", "Valask86", "Taitentai", "Dishout", "hitoribolemon", "WorkerAnt115", "Indigo_Clover", "-V0lD", "YourLocalTeaHoarder", "TheEscapedGoat", "arminfucker69", "NaVENOM", "GhostOfSparta27", "Cloore", "moeyberko"]

# phrase to activate the bot

ru1 = '!randomuser'
ru2 = '?randomuser'
ru3 = '+randomuser'
ru4 = '-randomuser'
ru5 = '$randomuser'


# look for phrase and reply appropriately

for comment in subreddit.stream.comments():
    if  any(x in comment.body for x in ("randomcharacter", "randomleak", "randomboy", "randomtitan", "randomalive", "ramdomgirl", "randomlivingboy", "randomlivinggirl", "randomship")):
        pass
    else:
        if  any(c in comment.body for c in (ru1, ru2, ru3, ru4, ru5)):
            reply = comment.body.replace(ru1,str(random.choice(users))).replace(ru2,str(random.choice(users))).replace(ru3,str(random.choice(users))).replace(ru4,str(random.choice(users))).replace(ru5,str(random.choice(users)))
            comment.reply(reply)
            print('posted')
