import statistics as st
import plotly.figure_factory as pff
import pandas as pd

data = pd.read_csv("data1.csv")
Weight = data["Weight"]
mean = 0
sum = 0

for x in Weight:
    sum = sum + x

mean = sum/len(Weight)
StandardDV = st.stdev(Weight)

#FirstRegion
FirstRegionSTDVstart , FirstRegionSTDVend = mean - StandardDV , mean + StandardDV
FirstRegion = [Result for Result in Weight if FirstRegionSTDVstart < Result < FirstRegionSTDVend]
FirstRegion_Per = len(FirstRegion)/len(Weight)

#SecondRegion
SecondRegionSTDVstart , SecondRegionSTDVend = mean - 2*StandardDV , mean + 2*StandardDV
SecondRegion = [Result for Result in Weight if SecondRegionSTDVstart < Result < SecondRegionSTDVend]
SecondRegion_Per = len(SecondRegion)/len(Weight)

#ThirdRegion
ThirdRegionSTDVstart , ThirdRegionSTDVend = mean - 3*StandardDV , mean + 3*StandardDV
ThirdRegion = [Result for Result in Weight if ThirdRegionSTDVstart < Result < ThirdRegionSTDVend]
ThirdRegion_Per = len(ThirdRegion)/len(Weight)

print("{}% of data is in FirstRegion\n{}% of data is in SecondRegion\n{}% of data is in ThirdRegion".format(FirstRegion_Per, SecondRegion_Per, ThirdRegion_Per))