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
```
## 5. Installation and Setup Steps
Follow these instructions to run the project.

**Prerequisites**
* Python installed
* An active internet connection (for firebsae)

**Step 1: Clone the repository**
Open terminal and run:
```bash
git clone [https://github.com/YourUsername/VIT-Lost-Found.git](https://github.com/YourUsername/VIT-Lost-Found.git)
```
```bash
cd VIT-Lost-Found
```
**Step 2: Install Dependencies**
Install the firebase library:
```bash
pip install firebase-admin
```
**Step 3: Configure Firebase**
* This project uses a `serviceKey.json` file to access the database.
* This has been excluded from the project repository to avoid leaking database information.

**Step 4: Run the application**
```bash
python main.py
```
## 6. Instructions for Testing
To verify the functionality of the system, follow these steps:

**Test 1: Registering a New Student**
* Launch the app
* Select option `2`.
* Enter registration number, name and password.
* _The system saves your profile, now you can login._

**Test 2: Reporting an item**
* Login
* Select option `1` from dashboard.
* Enter the details:
  * Item Name: `Water bottle`
  * Location: `AB-1 418`
  * Distinction: `has a car sticker`
* _The item is uploaded with a status `Open`._

**Test 3: Claiming an item**
* Login with a different user.
* Select option `2` from dashboard to see the list of all lost items.
* Enter the item ID from the list.
* Enter description:
The system checks the similarity of the description enter with the disctinction entered by the finder.
   * **Case 1:** Type `blue bottle`.
     * _System denies the claim._
   * **Case 2:** Type `blue bottle with a sticker`.
     * _System approves the claim._
* _The item status is changed to `Claimed` and the system shares the finder's details._
## 7. Future Enhancements
* Image Support: Integrating firebase allows user to upload photos of the fount items.
* Notifications: Automatically notify the finder when a claim is initiated.
* UI/UX: Inclusion of HTML or web apps for easier access across different platform.
## 8. Screenshots
**1. Login Screen**

![image]()

**2. Reporting an Item**

![image]()

**3. Successful Claim**

![image]()
