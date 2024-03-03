    import streamlit as st
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns


    st.title('Proyek Analisis Data: Peminjaman Sepeda🚲')
    st.subheader('About Peminjaman Sepeda: ')

    st.write('Sistem peminjaman sepeda merupakan generasi baru dari penyewaan sepeda tradisional di mana seluruh proses, mulai dari keanggotaan, penyewaan, hingga pengembalian, menjadi otomatis. Melalui sistem ini, pengguna dapat dengan mudah menyewa sepeda dari suatu posisi tertentu dan mengembalikannya di posisi lain. Saat ini, terdapat lebih dari 500 program berbagi sepeda di seluruh dunia yang terdiri dari lebih dari 500 ribu sepeda. Hari ini, terdapat minat besar dalam sistem ini karena peran pentingnya dalam masalah lalu lintas, lingkungan, dan kesehatan.')
    st.write('Proyek analisis data ini dilakukan untuk exploratory data pada sebuah sistem peminjaman sepeda dimana setelah dilakukan exploratory data dengan mendefinisikan beberapa pertanyaan bisnis dan menvisualisasikan hasil nya. ')

    # Pertanyaan 1
    st.subheader('Bagaimana tren peminjaman sepeda berubah selama musim berbeda?')
    bikeday_df = pd.read_csv("day.csv")
    bikeday_df = bikeday_df[['season', 'dteday', 'cnt']].reset_index(drop=True)
    season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    bikeday_df['season'] = bikeday_df['season'].map(season_mapping)
    trend_by_season = bikeday_df.groupby('season')['cnt'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='season', y='cnt', data=trend_by_season, marker='o', color='skyblue', label='Total Peminjaman')
    ax.set_title('Tren Peminjaman Sepeda Berdasarkan Musim', fontsize=16, fontweight='bold')
    ax.set_xlabel('Musim', fontsize=12)
    ax.set_ylabel('Total Peminjaman', fontsize=12)
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    for index, row in trend_by_season.iterrows():
        ax.text(row['season'], row['cnt'], str(row['cnt']), ha='center', va='bottom', fontsize=10)

    ax.legend(loc='upper left')
    st.pyplot(fig)

    st.write('Pada visualisasi data dapat dilihat bahwa tren peminjaman sepeda tertinggi berdasarkan musim adalah musim gugur (fall) dan disusul oleh musim panas (summer), yang mungkin disebabkan oleh cuaca yang lebih menyenangkan. Musim dimana tren peminjaman sepeda terendah ialah musim gugur (spring) yang mungkin disebabkan oleh cuaca yang belum sepenuhnya membaik setelah musim dingin.')

    # Pertanyaan 2
    st.subheader('Apakah cuaca tertentu berhubungan dengan peningkatan peminjaman?')
    bikeday_df = pd.read_csv("day.csv")
    bikeday_df = bikeday_df.reset_index()[['dteday','weathersit', 'cnt']]
    weathersit_mapping = {1: 'Clear', 2: 'Cloudy', 3: 'Light Rain', 4: 'Heavy Rain'}
    bikeday_df['weathersit'] = bikeday_df['weathersit'].map(weathersit_mapping)
    trend_by_weathersit = bikeday_df.groupby('weathersit')['cnt'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax = sns.barplot(
        x="weathersit",
        y="cnt",
        data=bikeday_df,
        palette="viridis"  
    )
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 10), textcoords='offset points', fontsize=10)

    # Menambahkan elemen desain dan integritas
    plt.title("""Number of Bike Rentals by Weather""",
              loc="center",
              fontsize=15)
    plt.xlabel("Weather")
    plt.ylabel("Number of Bike Rentals")
    st.pyplot(fig)
    st.write("""Pada visualisasi data menunjukkan bahwa peminjaman sepeda tertinggi terdapat pada cuaca cerah (clear weather) yang dimana ini mungkin terjadi disebabkan karena pada cuaca cerah dimana mood orang-orang meningkat untuk mengendarai sepeda. Berbeda dengan cuaca hujan lebat (heavy rain) dimana tidak ada terjadinya peminjaman sepeda. Tentu saja tidak ada orang yang berminat untuk mengendarai sepeda dicuaca hujan yang lebat""")
