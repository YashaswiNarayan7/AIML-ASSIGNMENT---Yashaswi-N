# Assignment: ML Idea Generator
# Date: 02/03/2026
# Name: Yashaswi N

def main():
    print("=== ML Idea Generator ===\n")

   
    ml_ideas = {
        "College": [
            {
                "Problem": "Predict student exam performance",
                "Input": "Attendance, assignment scores, previous grades",
                "Output": "Predicted exam score"
            },
            {
                "Problem": "Classroom seat allocation optimization",
                "Input": "Student preferences, room capacity, schedule",
                "Output": "Optimized seating arrangement"
            }
        ],
        "Healthcare": [
            {
                "Problem": "Detect diseases from medical images",
                "Input": "X-ray or MRI scans",
                "Output": "Disease prediction (healthy or specific condition)"
            },
            {
                "Problem": "Predict patient readmission",
                "Input": "Patient history, medications, lab results",
                "Output": "Probability of readmission within 30 days"
            }
        ],
        "Shopping": [
            {
                "Problem": "Product recommendation system",
                "Input": "User purchase history, ratings, browsing behavior",
                "Output": "Recommended products for the user"
            },
            {
                "Problem": "Customer churn prediction",
                "Input": "Purchase frequency, returns, complaints",
                "Output": "Probability of customer leaving"
            }
        ]
    }

   
    for domain, problems in ml_ideas.items():
        print(f"\n--- {domain} ---")
        for i, idea in enumerate(problems, start=1):
            print(f"{i}. Problem: {idea['Problem']}")
            print(f"   Input: {idea['Input']}")
            print(f"   Output: {idea['Output']}\n")

    print("All ML ideas generated successfully!\n")

if __name__ == "__main__":
    main()