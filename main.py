#import libraries & assign csv files
import pandas as pd
import numpy as np

hot100 = pd.read_csv("HotStuff2.csv")
pfork = pd.read_csv("ps4k.csv")
goat = pd.read_csv("goats.csv").set_index("Number")
winners = pd.read_csv("gramcys.csv").drop(columns="awardType").sort_values("annualGrammy").reset_index(drop=True)

#BILLBOARD HOT 100 SECTION
#order hot100.csv file by week and chart position
hot100["WeekID"]=pd.to_datetime(hot100["WeekID"])
hot100.sort_values(["WeekID", "Week Position"], inplace=True, ascending=True)
hot100.set_index("WeekID")


#GRAMMY SECTION
winners.sort_values("annualGrammy")
while True:
    interest = input("Are you interested in artists, albums, or songs? ")
    if interest.lower() not in ("artists", "albums", "songs"):
        print("Try again sweetie.")
    else:
        break
    
if interest.lower() == "artists":
    artist = input("Pick an artist: ")
    display(winners.loc[winners["name"] == artist])
elif interest.lower() == "albums":
    album = input("Pick an album: ")
    display(winners.loc[winners["awardFor"] == album])
elif interest.lower() == "songs":
    song = input("Pick a song: ")
    display(winners.loc[winners["awardFor"] == song])
    
    
#don't pick a Best New Artist category
index = int(input("Type the index number of a category you're interested in: "))
winners.iloc[index]

if winners.iloc[index].str.contains("Album").any():
    albumQuery = winners.iloc[index]["awardFor"]
    albumGrammyInfo(albumQuery)
else:
    songQuery = winners.iloc[index]["awardFor"]
    songGrammyInfo(songQuery)

#PITCHFORK REVIEWS SECTION
pfork.loc[pfork["artist"] == "Chance the Rapper"] #can be any artist duh


#GREATEST ALBUMS SECTION
#search by album
def findGOATalbum(album):
    if goat["Album"].str.contains(album).any():
        print("Heck yeah!")
        return goat.loc[goat["Album"] == album]
    else:
        print("Sorry, it's not...yet.")

albumQuery = input("Is this album a GOAT? ")        
findGOATalbum(albumQuery)

#search by artist
def findGOATartist(artist):
    if goat["Artist"].str.contains(artist).any():
        albumCount = len(goat.loc[goat["Artist"] == artist])
        print("Heck yeah! They have " + str(albumCount) + " GOAT albums.")
        return goat.loc[goat["Artist"] == artist]
    else:
        print("Sorry, they don't...yet.")

artistQuery = input("Does this artist have GOATs? ")
findGOATartist(artistQuery)
