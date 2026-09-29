# schemes_db.py
# contains list of all scholarship records

SCHOLARSHIPS = [
    {
        "name": "National Means-cum-Merit Scholarship",
        "provider": "Ministry of Education",
        "amt": "Rs. 12,000/year",
        "max_inc": 350000,
        "min_pct": 55,
        "cat": ["All"],
        "stream": ["All"]
    },
    {
        "name": "PM YASASVI Scholarship",
        "provider": "Ministry of Social Justice",
        "amt": "Rs. 75,000/year",
        "max_inc": 250000,
        "min_pct": 60,
        "cat": ["OBC", "EBC"],
        "stream": ["All"]
    },
    {
        "name": "Post Matric Scholarship for SC Students",
        "provider": "Ministry of Social Justice",
        "amt": "Tuition fee + allowance",
        "max_inc": 250000,
        "min_pct": 0,
        "cat": ["SC"],
        "stream": ["All"]
    },
    {
        "name": "Post Matric Scholarship for ST Students",
        "provider": "Ministry of Tribal Affairs",
        "amt": "Tuition fee + allowance",
        "max_inc": 250000,
        "min_pct": 0,
        "cat": ["ST"],
        "stream": ["All"]
    },
    {
        "name": "AICTE Pragati Scholarship",
        "provider": "AICTE",
        "amt": "Rs. 50,000/year",
        "max_inc": 800000,
        "min_pct": 0,
        "cat": ["All"],
        "stream": ["Engineering"]
    },
    {
        "name": "INSPIRE Scholarship (SHE)",
        "provider": "Dept. of Science & Technology",
        "amt": "Rs. 80,000/year",
        "max_inc": 10000000,
        "min_pct": 90,
        "cat": ["All"],
        "stream": ["Science"]
    },
    {
        "name": "Central Sector Scheme Scholarship",
        "provider": "Ministry of Education",
        "amt": "Rs. 10,000-20,000/year",
        "max_inc": 800000,
        "min_pct": 80,
        "cat": ["All"],
        "stream": ["All"]
    },
    {
        "name": "Sitaram Jindal Foundation Scholarship",
        "provider": "Sitaram Jindal Foundation",
        "amt": "Rs. 500-1,500/month",
        "max_inc": 300000,
        "min_pct": 50,
        "cat": ["All"],
        "stream": ["All"]
    },
    {
        "name": "Reliance Foundation UG Scholarship",
        "provider": "Reliance Foundation",
        "amt": "Up to Rs. 2,00,000",
        "max_inc": 1500000,
        "min_pct": 60,
        "cat": ["All"],
        "stream": ["All"]
    },
    {
        "name": "LIC Golden Jubilee Scholarship",
        "provider": "LIC of India",
        "amt": "Rs. 1,000-20,000/year",
        "max_inc": 250000,
        "min_pct": 0,
        "cat": ["All"],
        "stream": ["All"]
    },
    {
        "name": "AICTE Saksham Scholarship",
        "provider": "AICTE",
        "amt": "Rs. 50,000/year",
        "max_inc": 800000,
        "min_pct": 0,
        "cat": ["All"],
        "stream": ["Engineering"]
    },
    {
        "name": "Begum Hazrat Mahal National Scholarship",
        "provider": "Maulana Azad Education Foundation",
        "amt": "Rs. 5,000-12,000/year",
        "max_inc": 200000,
        "min_pct": 50,
        "cat": ["Minority"],
        "stream": ["All"]
    },
    {
        "name": "National Fellowship for OBC Students",
        "provider": "Ministry of Social Justice",
        "amt": "Rs. 31,000/month",
        "max_inc": 600000,
        "min_pct": 55,
        "cat": ["OBC"],
        "stream": ["All"]
    },
    {
        "name": "Ishan Uday Special Scholarship (NE Region)",
        "provider": "Ministry of Education",
        "amt": "Rs. 7,800/month",
        "max_inc": 450000,
        "min_pct": 0,
        "cat": ["All"],
        "stream": ["All"]
    },
    {
        "name": "HDFC Bank Parivartan ECSS",
        "provider": "HDFC Bank",
        "amt": "Up to Rs. 75,000/year",
        "max_inc": 250000,
        "min_pct": 50,
        "cat": ["All"],
        "stream": ["All"]
    },
    {
        "name": "Colgate Keep India Smiling Scholarship",
        "provider": "Colgate-Palmolive",
        "amt": "Rs. 10,000-20,000/year",
        "max_inc": 600000,
        "min_pct": 60,
        "cat": ["All"],
        "stream": ["Medical"]
    },
    {
        "name": "Vidyasaarathi Scholarship",
        "provider": "Digital India Corporation",
        "amt": "Varies by donor",
        "max_inc": 600000,
        "min_pct": 50,
        "cat": ["All"],
        "stream": ["All"]
    },
    {
        "name": "Swami Vivekananda Merit-cum-Means Scholarship",
        "provider": "State Government Scheme",
        "amt": "Rs. 1,000-5,000/month",
        "max_inc": 250000,
        "min_pct": 45,
        "cat": ["All"],
        "stream": ["All"]
    },
    {
        "name": "National Scholarship for Persons with Disabilities",
        "provider": "Ministry of Social Justice",
        "amt": "Rs. 6,000-15,000/year",
        "max_inc": 250000,
        "min_pct": 40,
        "cat": ["All"],
        "stream": ["All"]
    },
    {
        "name": "Aditya Birla Scholarship",
        "provider": "Aditya Birla Education Trust",
        "amt": "Up to Rs. 1,75,000/year",
        "max_inc": 10000000,
        "min_pct": 90,
        "cat": ["All"],
        "stream": ["Engineering"]
    }
]

def get_all_schemes():
    return SCHOLARSHIPS
