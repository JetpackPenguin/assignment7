import streamlit as st
import requests
import logging

API_URL = "https://your-render-url.onrender.com"
API_KEY = "your_admin_key_here"

headers = {
    "X-Admin-Key": API_KEY
}

logging.basicConfig(level=logging.INFO)

st.title("🎵 Musicians App")

# ---------------- CREATE ----------------
st.header("Create Musician")

name = st.text_input("Name")
genre = st.text_input("Genre")
country = st.text_input("Country")
bio = st.text_area("Bio")
avatar_url = st.text_input("Avatar URL")

if st.button("Create"):
    payload = {
        "name": name,
        "genre": genre,
        "country": country,
        "bio": bio,
        "avatar_url": avatar_url
    }

    res = requests.post(f"{API_URL}/musicians", json=payload, headers=headers)
    st.write(res.json())


# ---------------- SEARCH ----------------
st.header("Search Musicians")

search = st.text_input("Search keyword")

if st.button("Search"):
    res = requests.get(f"{API_URL}/musicians", params={"search": search})
    st.write(res.json())


# ---------------- GET ONE ----------------
st.header("Get One Musician")

mid = st.text_input("Musician ID")

if st.button("Retrieve"):
    res = requests.get(f"{API_URL}/musicians/{mid}")
    st.write(res.json())


# ---------------- UPDATE (PATCH is safer) ----------------
st.header("Update Musician")

uid = st.text_input("Update ID")
new_name = st.text_input("New Name")
new_genre = st.text_input("New Genre")

if st.button("Update"):
    payload = {}

    if new_name:
        payload["name"] = new_name
    if new_genre:
        payload["genre"] = new_genre

    res = requests.patch(
        f"{API_URL}/musicians/{uid}",
        json=payload,
        headers=headers
    )

    st.write(res.json())


# ---------------- DELETE ----------------
st.header("Delete Musician")

did = st.text_input("Delete ID")

if st.button("Delete"):
    res = requests.delete(
        f"{API_URL}/musicians/{did}",
        headers=headers
    )
    st.write(res.json())
