import pandas as pd
import os.path, os, datetime
from os import path
from sodapy import Socrata

if __name__ == "__main__":
    latest = input("(y/n) Do you wish to download latest: ")
    if(latest.lower() == "y" or latest.lower() == "yes"):
        #Create the excel workbook and worksheet
        if(path.exists("PowerballResults.csv")):
            if not os.path.exists("OldFiles"):
                os.makedirs("OldFiles")
            now = datetime.datetime.now()
            os.rename("PowerballResults.csv","OldFiles/PowerballResults" + str(now.strftime("%I-%M-%S")) + ".csv")
        if(path.exists("MegaMillionsResults.csv")):
            if not os.path.exists("OldFiles"):
                os.makedirs("OldFiles")
            now = datetime.datetime.now()
            os.rename("MegaMillionsResults.csv","OldFiles/MegaMillionsResults" + str(now.strftime("%I-%M-%S")) + ".csv")

        # Making api call with app token
        client = Socrata("data.ny.gov", "cP3KsYaY1gMu7w22uPA97fiCr")

        # Results, returned as JSON from API / converted to Python list of
        # dictionaries by sodapy.
        #This is for Powerball
        pbresults = client.get("d6yy-54nr", where="draw_date > '2015-10-07'")
        #This is for MegaMillions
        mmresults = client.get("5xaw-6ayf", where="draw_date > '2017-10-31'")

        # Convert to pandas DataFrame
        pbdf = pd.DataFrame.from_records(pbresults)
        print(pbdf)
        for i, row in pbdf.iterrows():
            new_date = pbdf.at[i,"draw_date"][:10]
            pbdf.at[i,"draw_date"] = new_date
        pbdf.to_csv("PowerballResults.csv", index=False)

        mmdf = pd.DataFrame.from_records(mmresults)
        print(mmdf)
        for i, row in mmdf.iterrows():
            new_date = mmdf.at[i,"draw_date"][:10]
            mmdf.at[i,"draw_date"] = new_date
        mmdf.to_csv("MegaMillionsResults.csv", index=False)
    else:
        pbdf = pd.read_csv("PowerballResults.csv")
        mmdf = pd.read_csv("MegaMillionsResults.csv")
        
        #Powerball
        pbdf["data_i_want"] = pbdf["draw_date"].astype(str) + " " + pbdf["winning_numbers"]
        split_data = pbdf["data_i_want"].str.split(" ")
        data = split_data.to_list()
        names = ["draw_date","First","Second","Third","Fourth","Fifth","Power"]
        new_pbdf = pd.DataFrame(data,columns=names)
        new_pbdf.to_csv("ModifiedPBResults.csv", index=False)

        #MegaMillions
        mmdf["new_nums"] = mmdf["draw_date"].astype(str) + " " + mmdf["winning_numbers"] + " " + mmdf["mega_ball"].astype(str)
        split_data = mmdf["new_nums"].str.split(" ")
        data = split_data.to_list()
        names = ["draw_date","First","Second","Third","Fourth","Fifth","Mega"]
        new_mmdf = pd.DataFrame(data,columns=names)
        new_mmdf.to_csv("ModifiedMMResults.csv", index=False)

        #Powerball
        first = new_pbdf.First.mode()[0]
        second = new_pbdf.Second.mode()[0]
        third = new_pbdf.Third.mode()[0]
        fourth = new_pbdf.Fourth.mode()[0]
        fifth = new_pbdf.Fifth.mode()[0]
        power = new_pbdf.Power.mode()[0]
        #MegaMillions
        firstm = new_mmdf.First.mode()[0]
        secondm = new_mmdf.Second.mode()[0]
        thirdm = new_mmdf.Third.mode()[0]
        fourthm = new_mmdf.Fourth.mode()[0]
        fifthm = new_mmdf.Fifth.mode()[0]
        mega = new_mmdf.Mega.mode()[0]
        
        print(f"Most common powerball numbers are {first} {second} {third} {fourth} {fifth} {power}")
        print(f"Most common megamillion numbers are {firstm} {secondm} {thirdm} {fourthm} {fifthm} {mega}")
        print(new_pbdf.First.value_counts()[:1])
        print(new_pbdf.Second.value_counts()[:1])
        print(new_pbdf.Third.value_counts()[:1])
        print(new_pbdf.Fourth.value_counts()[:1])
        print(new_pbdf.Fifth.value_counts()[:1])
        print(new_pbdf.Power.value_counts()[:1])
        print(new_mmdf.First.value_counts()[:1])
        print(new_mmdf.Second.value_counts()[:1])
        print(new_mmdf.Third.value_counts()[:1])
        print(new_mmdf.Fourth.value_counts()[:1])
        print(new_mmdf.Fifth.value_counts()[:1])
        print(new_mmdf.Mega.value_counts()[:1])

    leave = input("Press any key to leave...")
