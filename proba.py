import pandas as pd
import matplotlib.pyplot as plt


def diagram():
    df = pd.read_json("Station_1.json")
    df2 = df.transpose()
    df2.plot(figsize=(10, 8))
    plt.show()
