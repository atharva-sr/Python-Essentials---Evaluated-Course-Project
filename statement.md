The Problem & Project Scope

Why This Matters

Every academic year, millions in financial aid go unclaimed simply because students don't know they qualify. Scholarship details are scattered across dozens of clunky state websites, central portals, and private foundation PDFs—each with its own confusing mix of income caps, minimum percentages, category reservations, and eligible degrees.
Trying to check these manually is exhausting, easy to get wrong, and often causes deserving students to miss out before they even apply.

What This Project Does

The Scholarship Finder is a lightweight terminal utility built to simplify that discovery process. It focuses on four core jobs:
Gathering a student's basic academic and socioeconomic background through an intuitive CLI flow.
Sanitizing and validating user entries so unexpected inputs don't crash the session.
Comparing applicant data against a curated catalog of central, state, and private schemes using clean, deterministic eligibility checks.
Generating a clear, actionable list of matching opportunities complete with key requirements and award details.

Who It's For

Students: Anyone looking for funding who wants a 30-second answer on where they actually qualify.
School & College Counsellors: Advisors who want a dependable, offline-friendly tool to quickly screen opportunities for students.
Campus Helpdesks: Support staff looking for a consistent, repeatable way to point applicants toward relevant grants.

Key Capabilities

Forgiving Input Handling: Keeps users on track with helpful prompts and boundary checks rather than dumping stack traces.
Multi-Factor Matching Engine: Automatically balances overlapping criteria—like income thresholds, minimum marks, caste/category quotas, and specific disciplines (STEM, humanities, vocational).
Standalone Scheme Directory: Lets users browse the full scholarship catalog directly if they just want to explore requirements.
Decoupled Architecture: Built with separate data, validation, and presentation layers so anyone can add new schemes or adjust criteria without breaking the UI.
