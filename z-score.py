import csv
import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

mean = statistics.mean(data)
SD = statistics.stdev(data)

print("Mean is ", mean)
print("SD is ", SD)

def random_set_of_means(counter):
    dataset = []

    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]

        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean
    
meanlist = []

for i in range(0, 100):
    set_of_means = random_set_of_means(30)
    meanlist.append(set_of_means)

sampling_mean = statistics.mean(meanlist)
samplingSD = statistics.stdev(meanlist)

first_std_deviation_start, first_std_deviation_end = sampling_mean - samplingSD, sampling_mean + samplingSD
second_std_deviation_start, second_std_deviation_end = sampling_mean - (2*samplingSD), sampling_mean + (2*samplingSD)
third_std_deviation_start, third_std_deviation_end = sampling_mean - (3*samplingSD), sampling_mean + (3*samplingSD)

print("First Std Deviation is ", first_std_deviation_start,", ", first_std_deviation_end)
print("Second Std Deviation is ", second_std_deviation_start,", ", second_std_deviation_end)
print("Third Std Deviation is ", third_std_deviation_start,", ", third_std_deviation_end)

fig = ff.create_distplot([meanlist], ["Reading Time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="Mean"))

fig.add_trace(go.Scatter(x=[sampling_mean, sampling_mean], y=[0, 1], mode="lines", name="Sampling Mean"))

fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 1], mode="lines", name="Sd 1 Start"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 1], mode="lines", name="Sd 1 end"))

fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 1], mode="lines", name="Sd 2 Start"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 1], mode="lines", name="Sd 3 end"))

fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 1], mode="lines", name="Sd 3 Start"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 1], mode="lines", name="Sd 3 end"))

fig.show()

z_score = (sampling_mean - mean)/samplingSD
print(f"The Z-Score is  {z_score}")