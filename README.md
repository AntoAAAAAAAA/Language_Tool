# Volunteer Language Access Tool

A bilingual, plug-and-play phrase finder built with **Streamlit**. It lets clinic/community volunteers quickly search, filter, and copy common clinical phrases in **English ↔ Spanish** so basic communication isn’t a scramble.

## Live App
**Try it here:** https://volunteerlanguageaccesstool.streamlit.app/

## Purpose
This app was built to mirror a simple, real-world tool you might keep at a triage desk or outreach event. It focuses on:
- Fast access to common phrases
- Clear, culturally respectful wording
- Bilingual support (English/Spanish)
- Low barrier to use (no logins, no training needed)

## Features
- **Searchable phrase list** (accent- & case-insensitive)
- **Category filters** (introductions, vitals, social history, etc.)
- **Favorites** to pin your go-to lines
- **One-click copy** for both languages
- **Template blanks** (e.g., “Do you have a history of ___?”)
- **Optional notes & phonetic helpers** in the CSV
- **Quick edit/reset** (dev page): tweak phrases during a session and export the updated CSV

## Why This Matters
Tools like this help:
- Bridge language gaps when an interpreter isn’t immediately available
- Support volunteers and students in community clinics
- Encourage consistent, respectful phrasing instead of ad‑hoc translations

## Built With
- **Streamlit** (UI)
- **Python / Pandas** (data handling)
- **unicodedata & custom helpers** for normalized search
- CSV backend for simplicity (no database required)
