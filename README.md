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

Language: Python 3 (runs entirely on native libraries like sys—no external packages or pip install required)
Version Control: Git & GitHub

Project Structure

scholarship_finder/
│
├── schemes_db.py       # Scholarship catalog (criteria, limits, and awards)
├── validator.py        # Logic that tests a student's profile against scheme requirements
├── main.py             # CLI runner, menus, and user prompt handling
├── README.md           # Quickstart and overview
└── statement.md        # Background on the problem and original project goals
