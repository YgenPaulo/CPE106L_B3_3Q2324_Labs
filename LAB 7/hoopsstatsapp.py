
from hoopstatsview import HoopStatsView
import pandas as pd

def main():
    frame = pd.read_csv("cleanbrogdonstats.csv")
    HoopStatsView(frame)

if __name__ == "__main__":
    main()
