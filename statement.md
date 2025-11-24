# VIT-Lost-Found

## Problem Statement & Project Scope

### 1. Problem Statement
In a bustling university campus like VIT Bhopal, students and staff frequently misplace personal belongings such as ID cards, electronics, and keys. Currently, the process of recovering these items relies on disorganized methods like WhatsApp groups, physical notice boards, or word-of-mouth. This leads to:
* **Inefficiency:** Lost items often go unnoticed by the owner.
* **Lack of Verification:** There is no standard way to verify if a claimant is the actual owner.
* **Data Redundancy:** Multiple people posting the same item in different groups.

### 2. Project Scope
**VIT Lost & Found** is a centralized Command Line Interface (CLI) based application designed to bridge the gap between the "Finder" and the "Loser" of an item. The system utilizes cloud-based storage (Firebase) to ensure data is accessible across different instances and provides a secure verification mechanism to prevent theft.

### 3. Target Users
* **Students:** To report lost items or claim found ones.
* **Faculty & Staff:** To report items found in classrooms or labs.
* **Campus Security/Proctors:** To manage the handover of valuable items (future scope).

### 4. High-Level Features
* **Centralized Cloud Database:** Uses Google Firebase Firestore to store user and item data in real-time, ensuring persistence unlike local file systems.
* **Secure Authentication:** User registration and login system to track who is reporting or claiming items.
* **Smart Verification (Innovation):** Implements a "Distinction Match" feature using fuzzy logic (SequenceMatcher). The finder sets a hidden "secret feature" (e.g., "cracked screen"), and the claimant must describe it. The system automatically verifies ownership based on text similarity.
* **Real-time Dashboard:** Displays only "Open" (unclaimed) items to keep the list relevant.
