
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title("Analyse des facteurs influençant le prix des logements - Californie")


df = pd.read_csv("housing.csv")
st.subheader("Aperçu des données")
st.dataframe(df.head())


st.subheader("Statistiques descriptives")
st.write(df.describe())


st.subheader("Distribution des prix des logements")
fig, ax = plt.subplots()
sns.histplot(df['median_house_value'], bins=20, kde=True, ax=ax)
st.pyplot(fig)


st.subheader("Matrice de corrélation")
fig, ax = plt.subplots()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)


st.subheader("Prix des logements par âge médian")
fig, ax = plt.subplots()
sns.boxplot(x=pd.cut(df['housing_median_age'], bins=5), y=df['median_house_value'], ax=ax)
st.pyplot(fig)


st.subheader("Filtrage interactif")
min_price, max_price = st.slider("Plage de prix", int(df['median_house_value'].min()), int(df['median_house_value'].max()), (50000, 300000))
filtered_df = df[(df['median_house_value'] >= min_price) & (df['median_house_value'] <= max_price)]
st.write(f"Nombre de logements trouvés : {len(filtered_df)}")
st.dataframe(filtered_df)
