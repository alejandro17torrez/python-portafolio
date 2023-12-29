import logging
from enum import Enum

import pandas as pd
import plotly.express as px
from plotly.graph_objs import Figure

logging.basicConfig(level=logging.DEBUG)


class Columns(Enum):
    ERD = "Expected_Ride_Duration"
    HCR = "Historical_Cost_of_Ride"
    AR = "Average_Ratings"
    NPR = "Number_of_Past_Rides"
    NOD = "Number_of_Drivers"
    NOR = "Number_of_Riders"
    VT = "Vehicle_Type"


data: pd.DataFrame = pd.read_csv("./datasets/dynamic_pricing.csv")

scatter: Figure = px.scatter(
    data,
    x=Columns.ERD.value,
    y=Columns.HCR.value,
    title="Expected Ride Duration vs. Historical Cost of Ride",
    trendline="ols",
)

box: Figure = px.box(
    data,
    x=Columns.VT.value,
    y=Columns.HCR.value,
    title="Historical Cost of Ride Distribution by Vehicle Type",
)

graphs: list[Figure] = [box, scatter]

for graph in graphs:
    graph.show()
