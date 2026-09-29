# Python-Essentials---Evaluated-Course-Project
Scholarship Finder

A straightforward command-line tool built in Python to help students figure out which scholarships they qualify for—without having to dig through dense government circulars and foundation portals.
It takes a student's basic profile (grades, household income, category, and degree) and cross-checks it against active government and private funding schemes to surface what they're actually eligible to apply for.

What It Does

Simple Console Walkthrough: Walks you through a few quick terminal prompts to enter your academic and financial background.
Crash-Resistant Inputs: Handles typos, invalid ranges, and unexpected inputs gracefully without breaking the session.
Tailored Filtering: Evaluates multiple factors simultaneously—matching minimum cutoff marks, income ceilings, caste/category quotas, and field restrictions (like STEM or arts).
Clean, Separated Code: Organized into clear, focused files so you can tweak matching rules or update the scholarship database without touching the user interface code.

Built With

Language: Python 3 (runs entirely on native libraries like sys—no external packages or pip install required).
Standard Libraries:
sys — Clean exits and command-line flow;
time — Natural pacing between menu prompts and search results;
math — Groups income values into standardized financial brackets (math.ceil).
Version Control: Git & GitHub.

Project Structure

scholarship_finder/

├── schemes_db.py       # Scholarship catalog (criteria, limits, and awards)

├── validator.py        # Logic that tests a student's profile against scheme requirements

├── main.py             # CLI runner, menus, and user prompt handling

├── README.md           # Quickstart and overview

└── statement.md        # Background on the problem and original project goals


Installation & Setup
Clone the Repository:

```bash

git clone https://github.com/atharva-sr/Python-Essentials---Evaluated-Course-Project
```
Verify Python Installation:

Make sure Python 3.x is installed:

```bash

python --version
```
Execute the Application:
```bash
cd Python-Essentials---Evaluated-Course-Project
```
Run the driver script:
```bash
python main.py
```
Usage Instructions

Run python main.py in your terminal.
Choose Option 1 from the menu to initiate a scholarship search.

Enter your details when prompted:

Full Name

Annual Family Income (in INR)

Previous Exam Percentage (0 to 100)

Category (General, OBC, SC, ST, EBC, or Minority)

Stream of Study (Engineering, Medical, Science, Commerce, or Arts)

View your categorized income bracket and matching scholarships printed directly on the console.

Choose Option 2 anytime to view all registered schemes in the database.

Choose Option 3 to exit the program cleanly.

Instructions for Testing
To verify that the application handles inputs and filtering properly, test these cases manually:

1. Boundary & Positive Eligibility Test
Inputs: Name: Rahul, Income: 200000, Percentage: 85, Category: OBC, Stream: Engineering

Expected Output: Successfully categorizes applicant into the Up to Rs. 200000 bracket and returns matching schemes such as PM YASASVI Scholarship, AICTE Pragati Scholarship, and Central Sector Scheme Scholarship.

2. High Income Test
Inputs: Income: 1500000, Percentage: 92, Category: General, Stream: Science

Expected Output: Correctly excludes lower income schemes and only returns schemes with high or unlimited income caps (e.g., INSPIRE Scholarship (SHE)).

3. Input Validation & Error Handling Test
Negative Income: Enter -25000 at the income prompt.

Expected Output: Program displays "Income cannot be negative!" and prompts again.

Invalid Percentage: Enter 105 or -5 at the marks prompt.

Expected Output: Program displays "Score must be between 0 and 100." and prompts again.

Non-Numeric Input: Enter abc at the income prompt.

Expected Output: Intercepted by try/except block, displays "Please enter numeric characters only." without crashing.


Screenshots
<img width="1205" height="977" alt="image" src="https://github.com/user-attachments/assets/c41624ad-5263-4bf0-8b35-13b22cec30ca" />
<img width="1147" height="755" alt="image" src="https://github.com/user-attachments/assets/996c60d9-0a72-47e0-9c7f-eee6ca10acb6" />


