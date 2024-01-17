import pandas as pd

thor = pd.read_csv('../data/thor_data_vietnam.csv', low_memory=False)
thor = thor.dropna(subset=['TGTLATDD_DDD_WGS84'])

# We filter out kinetic missions, any patrol missions, and any
# missions where no weapons are dropped
kinetic_bool = thor['MFUNC_DESC_CLASS'] == 'KINETIC'
patrol_bool = ~(thor['MFUNC_DESC'].str.contains('PATROL').astype('bool'))
weapons_bool = thor['NUMWEAPONSDELIVERED'] > 0

export_cols = ["MSNDATE", "TGTLATDD_DDD_WGS84", "TGTLONDDD_DDD_WGS84"]

final = thor[kinetic_bool & patrol_bool & weapons_bool][export_cols]
final.to_csv("../data/thor_filtered.csv")

