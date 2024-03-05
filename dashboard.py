import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Membaca data dari file CSV ke dalam DataFrame
day_df = pd.read_csv("/content/day.csv")
day_df.head()

# Grafik 1: Distribusi Jumlah Penyewa Sepeda berdasarkan Cuaca
subset_df = day_df[['weather_cond', 'count']]
plt.figure(figsize=(10, 6))
sns.histplot(data=subset_df,
             x='count', 
             hue='weather_cond',
             multiple="stack", 
             bins=30,
             kde=True)
plt.xlabel('Jumlah Penyewa Sepeda')
plt.ylabel('Frekuensi')
plt.title('Distribusi Jumlah Penyewa Sepeda berdasarkan Cuaca')
st.pyplot()

# Grafik 2: Histogram Jumlah Total Penyewa Sepeda berdasarkan Musim
plt.figure(figsize=(10, 6))
sns.histplot(data=day_df, x='season', y ='count', hue='season', bins=30, kde=True)
plt.xlabel("Musim")
plt.ylabel("Jumlah Penyewa Sepeda")
plt.title("Histogram Jumlah Total Penyewa Sepeda berdasarkan Musim")
st.pyplot()

# Grafik 3: Jumlah total sepeda yang disewakan berdasarkan Bulan dan tahun
day_df['month'] = pd.Categorical(day_df['month'], categories=
    ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    ordered=True)
monthly_counts = day_df.groupby(by=["month","year"]).agg({
    "count": "sum"
}).reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(
    data=monthly_counts,
    x="month",
    y="count",
    hue="year",
    palette="rocket")
plt.title("Jumlah total sepeda yang disewakan berdasarkan Bulan dan tahun")
plt.xlabel("Bulan")
plt.ylabel("Jumlah Penyewa Sepeda")
plt.legend(title="Tahun", loc="upper right")
st.pyplot()


