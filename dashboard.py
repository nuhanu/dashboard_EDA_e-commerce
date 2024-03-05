import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar
import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)


day_df = pd.read_csv("https://raw.githubusercontent.com/nuhanu/dashboard_EDA_e-commerce/main/day.csv")
# Mengubah nama kolom menjadi nama yang lebih jelas
     # Misalkan yr dirubah menjadi year

day_df.rename(columns={
    'dteday': 'dateday',
    'yr': 'year',
    'mnth': 'month',
    'weathersit': 'weather_cond',
    'cnt': 'count'
}, inplace=True)

day_df['month'] = day_df['month'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})
day_df['season'] = day_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
day_df['weekday'] = day_df['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})
day_df['weather_cond'] = day_df['weather_cond'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})

st.title("Bike Sharing Dashboard")

# Grafik 1: Distribusi Jumlah Penyewa Sepeda berdasarkan Cuaca
# Buat subplot dengan 1 baris dan 2 kolom
fig, ax = plt.subplots(figsize=(12, 6))

# Plot - Distribusi Jumlah Penyewa Sepeda berdasarkan Cuaca
subset_df = day_df[['weather_cond', 'count']]
sns.histplot(data=subset_df,
             x='count', 
             hue='weather_cond',
             multiple="stack", 
             bins=30,
             kde=True,
             hue_order=['Clear/Partly Cloudy', 'Light Snow/Rain', 'Misty/Cloudy'],  # Urutan yang diinginkan
             ax=ax)

# Atur label dan judul plot
ax.set_xlabel('Jumlah Penyewa Sepeda')
ax.set_ylabel('Frekuensi')
ax.set_title('Distribusi Jumlah Penyewa Sepeda berdasarkan Cuaca')

# Tampilkan plot di Streamlit
st.pyplot(fig)


# Mengurutkan data untuk urutan yang diinginkan
season_order = ['Fall', 'Spring', 'Summer', 'Winter']
day_df['season'] = pd.Categorical(day_df['season'], categories=season_order, ordered=True)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot - Histogram Jumlah Total Penyewa Sepeda berdasarkan Musim
sns.histplot(data=day_df, 
             x='season', 
             y='count', 
             hue='season', 
             bins=30, 
             kde=True, 
             ax=ax)

ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Penyewa Sepeda")
ax.set_title("Histogram Jumlah Total Penyewa Sepeda berdasarkan Musim")

# Tampilkan plot di Streamlit
st.pyplot(fig)


# Grafik 3: Jumlah total sepeda yang disewakan berdasarkan Bulan dan tahun
day_df['year'] = day_df['year'].map({0:2011, 1:2012})
day_df['month'] = pd.Categorical(day_df['month'], categories=
    ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    ordered=True)

monthly_counts = day_df.groupby(by=["month","year"]).agg({
    "count": "sum"
}).reset_index()

fig, ax = plt.subplots(figsize=(10, 6))


sns.lineplot(
    data=monthly_counts,
    x="month",
    y="count",
    hue="year",
    palette="pastel",
    ax=ax
)

ax.set_title("Jumlah total sepeda yang disewakan berdasarkan Bulan dan tahun")
ax.set_xlabel(None)
ax.set_ylabel("Jumlah Penyewa Sepeda")
ax.legend(title="Tahun", loc="upper right")

plt.tight_layout()

st.pyplot(fig)

