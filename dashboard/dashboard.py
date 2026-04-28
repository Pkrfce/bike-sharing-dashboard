import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

sns.set(style="whitegrid")
plt.rcParams.update({"font.size": 9})

st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

@st.cache_data
def load_data():
    BASE_DIR = Path(__file__).parent
    file_path = BASE_DIR / "main_data.csv"

    df = pd.read_csv(file_path)
    df["dteday"] = pd.to_datetime(df["dteday"])
    return df

df = load_data()

st.title("🚲 Bike Sharing Dashboard")
st.write(
    """
    Dashboard ini menampilkan pola penyewaan sepeda berdasarkan musim, cuaca,
    jenis hari, dan jam penggunaan.
    """
)

min_date = df["dteday"].min()
max_date = df["dteday"].max()

with st.sidebar:
    st.header("Filter Data")

    date_range = st.date_input(
        "Pilih Rentang Tanggal",
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    season_options = ["All Season"] + list(df["season_name"].unique())

    selected_season = st.selectbox(
        "Pilih Musim",
        options=season_options,
        index=0
    )

if len(date_range) == 2:
    start_date, end_date = date_range

    filtered_df = df[
        (df["dteday"] >= pd.to_datetime(start_date)) &
        (df["dteday"] <= pd.to_datetime(end_date))
    ]

    if selected_season != "All Season":
        filtered_df = filtered_df[
            filtered_df["season_name"] == selected_season
        ]
else:
    filtered_df = df.copy()

    if selected_season != "All Season":
        filtered_df = filtered_df[
            filtered_df["season_name"] == selected_season
        ]

filtered_df = filtered_df.copy()

st.subheader("Ringkasan Metrik")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Penyewaan", f"{filtered_df['cnt'].sum():,.0f}")

with col2:
    st.metric("Rata-rata Penyewaan per Jam", f"{filtered_df['cnt'].mean():,.2f}")

with col3:
    st.metric("Total Pengguna Terdaftar", f"{filtered_df['registered'].sum():,.0f}")


st.subheader("Visualisasi Data")

chart_size = (5.5, 3.5)

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Rata-rata Penyewaan Berdasarkan Musim")

    season_df = filtered_df.groupby("season_name")["cnt"].mean().reset_index()
    season_df = season_df.sort_values("cnt", ascending=False)

    fig, ax = plt.subplots(figsize=chart_size)
    sns.barplot(
        data=season_df,
        x="season_name",
        y="cnt",
        ax=ax
    )
    ax.set_title("Rata-rata Penyewaan Berdasarkan Musim", fontsize=10)
    ax.set_xlabel("Musim", fontsize=9)
    ax.set_ylabel("Rata-rata Penyewaan", fontsize=9)
    ax.tick_params(axis="x", labelsize=8)
    ax.tick_params(axis="y", labelsize=8)
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)

with col2:
    st.markdown("#### Rata-rata Penyewaan Berdasarkan Cuaca")

    weather_df = filtered_df.groupby("weather_name")["cnt"].mean().reset_index()
    weather_df = weather_df.sort_values("cnt", ascending=False)

    fig, ax = plt.subplots(figsize=chart_size)
    sns.barplot(
        data=weather_df,
        x="weather_name",
        y="cnt",
        ax=ax
    )
    ax.set_title("Rata-rata Penyewaan Berdasarkan Cuaca", fontsize=10)
    ax.set_xlabel("Kondisi Cuaca", fontsize=9)
    ax.set_ylabel("Rata-rata Penyewaan", fontsize=9)
    ax.tick_params(axis="x", labelsize=8, rotation=15)
    ax.tick_params(axis="y", labelsize=8)
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)


col3, col4 = st.columns(2)

with col3:
    st.markdown("#### Pola Penyewaan Sepeda per Jam")

    hourly_df = filtered_df.groupby(["workingday_name", "hr"])["cnt"].mean().reset_index()

    fig, ax = plt.subplots(figsize=chart_size)
    sns.lineplot(
        data=hourly_df,
        x="hr",
        y="cnt",
        hue="workingday_name",
        marker="o",
        ax=ax
    )
    ax.set_title("Rata-rata Penyewaan Sepeda per Jam", fontsize=10)
    ax.set_xlabel("Jam", fontsize=9)
    ax.set_ylabel("Rata-rata Penyewaan", fontsize=9)
    ax.set_xticks(range(0, 24, 2))
    ax.tick_params(axis="x", labelsize=8)
    ax.tick_params(axis="y", labelsize=8)
    ax.legend(title="Jenis Hari", fontsize=8, title_fontsize=9)
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)

with col4:
    st.markdown("#### Kategori Permintaan")

    def demand_category(cnt):
        if cnt < 100:
            return "Low Demand"
        elif cnt < 300:
            return "Medium Demand"
        else:
            return "High Demand"

    filtered_df["demand_category"] = filtered_df["cnt"].apply(demand_category)

    demand_df = filtered_df.groupby("demand_category")["cnt"].count().reset_index()
    demand_df.columns = ["demand_category", "total_records"]

    fig, ax = plt.subplots(figsize=chart_size)
    sns.barplot(
        data=demand_df,
        x="demand_category",
        y="total_records",
        order=["Low Demand", "Medium Demand", "High Demand"],
        ax=ax
    )
    ax.set_title("Jumlah Record Berdasarkan Kategori Permintaan", fontsize=10)
    ax.set_xlabel("Kategori Permintaan", fontsize=9)
    ax.set_ylabel("Jumlah Record", fontsize=9)
    ax.tick_params(axis="x", labelsize=8)
    ax.tick_params(axis="y", labelsize=8)
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)


st.subheader("Insight Utama")
st.write(
    """
    - Permintaan penyewaan cenderung lebih tinggi pada kondisi cuaca cerah.
    - Pada hari kerja, permintaan meningkat pada pagi dan sore hari.
    - Pada hari non-kerja, permintaan lebih tinggi pada siang hingga sore hari.
    - Pengelompokan permintaan dapat membantu perusahaan dalam mengatur distribusi sepeda.
    """
)