# main.py
# main console interface for the project

import schemes_db
import validator

categories = ["General", "OBC", "SC", "ST", "EBC", "Minority"]
streams = ["Engineering", "Medical", "Science", "Commerce", "Arts"]

def show_all_schemes():
    schemes = schemes_db.get_all_schemes()
    print("\nTotal Schemes Available: " + str(len(schemes)))
    print("---------------------------------")
    count = 1
    for s in schemes:
        print(str(count) + ". " + s["name"])
        print("   Provider: " + s["provider"])
        print("   Max Income: Rs. " + str(s["max_inc"]) + " | Cutoff: " + str(s["min_pct"]) + "%")
        count = count + 1

def run_finder():
    print("\n--- Enter Candidate Profile ---")
    s_name = input("Enter Full Name: ").strip()
    if s_name == "":
        s_name = "Candidate"
        
    # get annual income
    while True:
        try:
            inc = float(input("Family annual income (Rs): "))
            if inc >= 0:
                break
            else:
                print("Income cannot be negative!")
        except:
            print("Please enter numeric characters only.")
            
    # get exam score
    while True:
        try:
            pct = float(input("Last exam score (0-100%): "))
            if pct >= 0 and pct <= 100:
                break
            else:
                print("Score must be between 0 and 100.")
        except:
            print("Invalid input, try again.")

    # category input
    print("\nAvailable Categories: " + ", ".join(categories))
    cat_inp = input("Your Category: ").strip()
    
    # stream input
    print("Available Streams: " + ", ".join(streams))
    stream_inp = input("Your Stream: ").strip()

    # process matches
    all_schemes = schemes_db.get_all_schemes()
    matched = validator.filter_scholarships(inc, pct, cat_inp, stream_inp, all_schemes)

    # display results
    print("\n=================================")
    print("Found " + str(len(matched)) + " scholarships for " + s_name + ":")
    print("=================================")
    
    if len(matched) == 0:
        print("No matching scholarships found for this profile.")
    else:
        idx = 1
        for m in matched:
            print("\n" + str(idx) + ". " + m["name"])
            print("   Provider : " + m["provider"])
            print("   Reward   : " + m["amt"])
            idx = idx + 1

def main():
    while True:
        print("\n=================================")
        print("       SCHOLARSHIP FINDER        ")
        print("=================================")
        print("1. Find Eligible Scholarships")
        print("2. View All Database Schemes")
        print("3. Exit")
        
        opt = input("Select an option (1-3): ").strip()
        
        if opt == "1":
            run_finder()
        elif opt == "2":
            show_all_schemes()
        elif opt == "3":
            print("\nExiting program. Thank you!")
            break
        else:
            print("Invalid choice, please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
