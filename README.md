# VIT Lost & Found System

## 1. Project Overview
We’ve all been there—losing an ID card or keys on campus and hoping someone finds it. VIT Lost & Found is a python app built to replace those chaotic and unorganised whatsApp groups with something that actually works for VIT Bhopal students. Instead of physical lists that never get updated, we use google firebase to keep everything updated.

## 2. Features
* **Secure Access:** You log in using your official VIT Registration Number, so we know every user is a verified student.
* **Always Up-to-Date:** We use cloud storage (Firebase), meaning the lost & found list is updated in real-time. You can access the same live data from any computer on campus.
* **Reporting Made Safe:** You can log the details (like location and category) but keep one specific detail hidden as a 'secret' to prevent theft.
* **Smart Claims:** You have to describe that hidden 'secret' detail. Our smart system compares your description with the finder's note, if it matches, the system instantly verifies you as the owner.
* **Connect & Collect:** Once the system verifies the claim, it automatically shares the finder's email with you so you can coordinate a meetup."

## 3. Technologies Used
* **Language:** Python
* **Database:** Google Firebase
* **Libraries:**
    * `firebase-admin` (For database)
    * `google-cloud-firestore` (For query filtering)
    * `difflib` (For verifying similarity)
    * `os`, `datetime`

## 4. Folder Structure
```text
VIT-Lost-Found/
├── Screenshots/
├── authentication.py
├── data.py                
├── file_management.py     
├── item_management.py     
├── main.py               
├── serviceAccountKey.json 
├── README.md              
└── statement.md         
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

![image](https://github.com/Visaging/VIT-Lost-Found/blob/main/Screenshots/login.png?raw=true)

**2. Reporting an Item**

![image](https://github.com/Visaging/VIT-Lost-Found/blob/main/Screenshots/reporting%20item%201.png?raw=true)
![image](https://github.com/Visaging/VIT-Lost-Found/blob/main/Screenshots/reporting%20item%20success.png?raw=true)

**3. Successful Claim**

![image](https://github.com/Visaging/VIT-Lost-Found/blob/main/Screenshots/claim%20sunccessful.png?raw=true)
