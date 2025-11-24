# VIT Lost & Found System

## 1. Project Overview
VIT Lost & Found is a Python-based application designed to help students at VIT Bhopal report and recover lost belongings efficiently. Unlike static lists, this project integrates **Google Firebase** for real-time cloud storage and uses **Python's Difflib** to implement an intelligent "Smart Claim" verification system.

## 2. Features
* **User Authentication:** Secure Registration and Login using unique Registration Numbers.
* **Cloud Persistence:** All data (Users and Items) is stored in Firebase Firestore, allowing the application to be run from multiple terminals while sharing the same database.
* **Report Items:** Finders can log items with details like Name, Description, Category, Location, and a hidden "Distinction" for security.
* **Smart Claim System:**
    * Users can view a dashboard of all unclaimed items.
    * To claim an item, the user must describe the unique distinction.
    * **Innovation:** The system uses `SequenceMatcher` to calculate a similarity score between the finder's hidden distinction and the claimant's description. If the match is >30% or contains key phrases, ownership is verified automatically.
* **Contact Sharing:** Once verified, the system reveals the finder's official VIT email ID to the claimant for coordination.

## 3. Technologies Used
* **Language:** Python 3.13
* **Database:** Google Firebase (Firestore NoSQL)
* **Libraries:**
    * `firebase-admin` (Cloud Database Connectivity)
    * `google-cloud-firestore` (Query filters)
    * `difflib` (For fuzzy logic string matching)
    * `os`, `datetime` (System utilities)

## 4. Folder Structure
```text
VIT-Lost-Found/
├── authentication.py      # Handles Login and Registration logic
├── data.py                # Data models (dictionaries) for Users and Items
├── file_management.py     # Firebase connection and CRUD operations
├── item_management.py     # Logic for Reporting and Claiming items (Business Logic)
├── main.py                # Entry point (Menu System)
├── serviceAccountKey.json # Firebase security credentials
├── README.md              # Project Documentation
└── statement.md           # Problem Statement and Scope
