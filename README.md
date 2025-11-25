# VIT Lost & Found System

## 1. Project Overview
We've all been there: losing our keys or ID card on campus and hoping someone finds them.  VIT Lost & Found is a Python app that was made to get rid of the messy and disorganised WhatsApp groups that VIT Bhopal students use.  We use Google Firebase to keep everything up to date instead of physical lists that never change.

## 2. Features
* **Secure Access:** We are able to verify that each user is a verified student because you log in using your official VIT Registration Number.
* **Always Up-to-Date:** Because we use cloud storage (Firebase), the lost and found list is updated instantly.  Any computer on campus has access to the same real-time data.
* **Reporting Made Safe:**  You need to explain that "secret" detail.  If your description and the finder's note match, our intelligent system instantly confirms that you are the owner.
* **Smart Claims:** You must explain that "secret" detail. If the finder's note and your description match, our intelligent system instantly confirms that you are the owner.
* **Connect & Collect:** The system will automatically send you the finder's email so you can arrange a meeting once the claim has been validated.

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
    ├── claim fail.png
    ├── aclaim sunccessful.png
    ├── dashboard.png
    ├── login.png
    ├── reporting item 1.png
    ├── reporting item success.png
├── Source_Code/
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
git clone [https://github.com/Visaging/VIT-Lost-Found.git](https://github.com/Visaging/VIT-Lost-Found.git)
```
```bash
cd VIT-Lost-Found\Source_Code
```
**Step 2: Install Dependencies**
Install the firebase library:
```bash
pip install firebase-admin
```
**Step 3: Run the application**
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
