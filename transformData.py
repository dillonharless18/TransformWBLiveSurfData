import pandas as pd 

# read in the data and store in dataframe
df = pd.read_csv('reports.csv',skiprows=None)

# Set up a dict to be used for addition in the loop
addition_dict = {
    "zero": 0,
    "ratingCell half": .5,
    "ratingCell": 1 
}

# Replace all nulls with zero to make it work with the addition_dict
#     Null represents the current logo in the rating is unfilled, hence it should contribute a 0 to the overall rating
#     If left as null, pandas will throw a nan error
for i in range(5):
    df['fun-factor' + str(i)] = df['fun-factor' + str(i)].fillna("zero")
    # Also replace all nulls in swell-size and water-surface
    if i == 0:
            df['swell-size'] = df['swell-size'].fillna("Missing")
            df['water-surface'] = df['water-surface'].fillna("Missing")


# Iterate through each row in the dataframe
for index, row in df.iterrows():
    total_rating = 0
    for i in range(5):
        total_rating += addition_dict[row['fun-factor' + str(i)]]
    df.at[index, 'total_rating'] = total_rating
    # print("The total_rating for {} on {} is {}".format( row["report-link"],  row["date"], total_rating))
    print("The total_rating for {} on {} is {}".format( row["report-link"],  row["date"], df.at[index, 'total_rating']))

    # Strip the HTML from these two elements
    print("df.at[index, 'swell-size']: " + str(df.at[index, 'swell-size']))
    print("TYPE OF df.at[index, 'swell-size']: " + str(type(df.at[index, 'swell-size'])))
    df.at[index, 'swell-size'] = df.at[index, 'swell-size'][28:]
    df.at[index, 'water-surface'] = df.at[index, 'water-surface'][31:]

# Delete the unnecessary columns
for i in range(5):
    del df['fun-factor' + str(i)] 


# TODO Come up with a conversion factor for the swell size
# For example:
    # {   
    #     "Ankle": 0.5,
    #     "Shin": 1,
    #     "Knee": 1.5,
    #     "Thigh": 2.5,
    #     "Waist": 3,
    #     "Stomach": 3.5,
    #     "Chest": 4,
    #     "Shoulder": 5,
    #     "Head": 6,
    #     "Overhead": 8,
    #     "Double Overhead": 12
    # }

# Come up with a dictionary for Water Surface Condtions
# For example:
    # { 
    #     "Glass": 0,
    #     "Clean": 1,
    #     "Bumpy": 2,
    #     "Choppy": 3,
    #     "Drifty": .5 # This could be added to one of the others, so if a number ends in .5 we know it's a combination of something and Drifty
    # }

df.to_csv('transformed_reports.csv')




