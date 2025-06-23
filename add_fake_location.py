import pandas as pd
import numpy as np
df = pd.read_csv("data/predicted_frauds.csv")
df['latitude'] = np.random.uniform(10.0, 30.0, size=len(df))
df['longitude'] = np.random.uniform(70.0, 90.0, size=len(df))
df.to_csv("data/predicted_frauds_with_location.csv", index=False)

print("Saved file with location data to data/predicted_frauds_with_location.csv")


