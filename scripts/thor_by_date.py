# Split the large CSV by month/year
import pandas as pd

thor = pd.read_csv('../data/thor_filtered.csv')

thor.drop(thor.columns[0], inplace=True, axis=1)

thor["MSNDATE"] = pd.to_datetime(thor["MSNDATE"], errors="coerce")
thor["MONTH"], thor["YEAR"] = thor["MSNDATE"].dt.month, thor["MSNDATE"].dt.year

# iterate through, produce CSV for each year/month combination of total number of missions
for i in range(1965, 1976):
    subset = thor[thor.YEAR == i]
    for j in range(1, 13):
        month = subset[subset.MONTH == j]
        if not month.empty:
            print(str(i), ",", str(j))
            data = month[["TGTLATDD_DDD_WGS84", "TGTLONDDD_DDD_WGS84"]]
            data.to_csv("../data/dates/" + str(i) + "_" + str(j) + ".csv", index=False)