#import libraries & assign csv files
import pandas as pd
import numpy as np

hot100 = pd.read_csv("HotStuff2.csv")
pfork = pd.read_csv("ps4k.csv")
goat = pd.read_csv("goats.csv").set_index("Number")
winners = pd.read_csv("gramcys.csv").drop(columns="awardType").sort_values("annualGrammy").reset_index(drop=True)


#FUNCTIONS
def albumGrammyInfo(album):
    artist = winners.iloc[index]["name"]
    year = winners.iloc[index]["year"]
    cat = winners.iloc[index]["category"]
    print("In %d, %s won %s for %s." % (year, artist, cat, album))
    
def songGrammyInfo(song):
    artist = winners.iloc[index]["name"]
    year = winners.iloc[index]["year"]
    cat = winners.iloc[index]["category"]
    print("In %d, %s won %s for %s." % (year, artist, cat, song))
    
def findGOATalbum(album):
    if goat["Album"].str.contains(album).any():
        print("The Rolling Stones considers this album one of the GOATs.")
        display(goat.loc[goat["Album"] == album])
    else:
        pass
    
def findOthers(year):
    if goat["Year"].isin([year]).any():
        goatNum = len(goat.loc[goat["Year"] == year])
        if goatNum > 1:
            print("Actually, " + str(goatNum) + " GOAT albums came out that year.")
            display(goat.loc[goat["Year"] == year])
    else:
        pass

def findGOATartist(artist):
    if goat["Artist"].str.contains(artist).any():
        albumCount = len(goat.loc[goat["Artist"] == artist])
        print("They do have " + str(albumCount) + " GOAT album(s) though.")
        display(goat.loc[goat["Artist"] == artist])
        
def findP4Krating(album):
    if pfork["album"].str.contains(album).any():
        rating = pfork.loc[pfork["album"] == album]
        score = rating.iloc[0]["score"]
        artistName = rating.iloc[0]["artist"]
        print("Pitchfork rated %s by %s: %g out of 10." % (album, artistName, score))
        
#BILLBOARD HOT 100 SECTION
#order hot100.csv file by week and chart position
hot100["WeekID"]=pd.to_datetime(hot100["WeekID"])
hot100.sort_values(["WeekID", "Week Position"], inplace=True, ascending=True)
hot100.set_index("WeekID")


#GRAMMY SECTION
while True:
    interest = input("Are you interested in artists, albums, or songs? ")
    if interest.lower() not in ("artists", "albums", "songs"):
        print("try again sweetie.")
    else:
        break
    
if interest.lower() == "artists":
    artistQuery = input("Pick an artist: ")
    if winners["name"].str.contains(artistQuery).any():
        gramCount = len(winners.loc[winners["name"] == artistQuery])
        print("Total number of Grammy awards: " + str(gramCount))
        display(winners.loc[winners["name"] == artistQuery])
    else:
        print("They don't have any Grammy Awards.")
        findGOATartist(artistQuery)
           
elif interest.lower() == "albums":
    albumQuery = input("Pick an album: ")
    findP4Krating(albumQuery) #DANGER WILL ROBINSON
    if winners["awardFor"].str.contains(albumQuery).any():
        gramCount = len(winners.loc[winners["awardFor"] == albumQuery])
        print("Total number of Grammy awards: " + str(gramCount))
        display(winners.loc[winners["awardFor"] == albumQuery])
    else:
        print("This album has no Grammy Awards.")
        findGOATalbum(albumQuery)    
    
elif interest.lower() == "songs":
    songQuery = input("Pick a song: ")
    if winners["awardFor"].str.contains(songQuery).any():
        gramCount = len(winners.loc[winners["awardFor"] == songQuery])
        print("Total number of Grammy awards: " + str(gramCount))
        display(winners.loc[winners["awardFor"] == songQuery])
    else:
        print("This song has no Grammy Awards.")
        
        
#don't pick a Best New Artist category
index = int(input("Type the index number of a category you're interested in: "))
winners.iloc[index]

if winners.iloc[index].str.contains("Album").any():
    albumQuery = winners.iloc[index]["awardFor"]
    albumYear = winners.iloc[index]["year"] - 1
    albumGrammyInfo(albumQuery)
    findP4Krating(albumQuery)
    findGOATalbum(albumQuery)
    findOthers(albumYear)
    
else:
    songQuery = winners.iloc[index]["awardFor"]
    songGrammyInfo(songQuery)

#PITCHFORK REVIEWS SECTION
pfork["date"] = pd.to_datetime(pfork["date"])
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

#search by year
def findGOATyear(year):
    if goat["Year"].isin([year]).any():
        goatNum = len(goat.loc[goat["Year"] == year])
        print(str(goatNum) + " GOAT albums came out that year.")
        return goat.loc[goat["Year"] == year]
    else:
        print("That is all.")
        print(type(goat["Year"]))

yearQuery = int(input("Any GOATs this year? "))
findGOATyear(yearQuery)
