# Assignment: Spam Classifier Thinking
# Date: 10/03/2026
# Name: Yashaswi N

def main():
    print("=== Spam Classifier Thinking ===\n")

    # Step 1: Define sample messages
    messages = [
        {"Text": "Congratulations! You've won a free iPhone!", "Label": "Spam"},
        {"Text": "Hi, can we meet tomorrow for the project discussion?", "Label": "Ham"},
        {"Text": "Limited time offer, claim your prize now!", "Label": "Spam"},
        {"Text": "Please find attached the assignment file.", "Label": "Ham"}
    ]

    # Step 2: Define features we would use
    features = [
        "Number of links in the message",
        "Presence of certain keywords like 'Congratulations', 'Offer', 'Free'",
        "Number of capital letters",
        "Message length",
        "Frequency of exclamation marks"
    ]

    # Step 3: Print messages and features
    print("Sample Messages:")
    for i, msg in enumerate(messages, start=1):
        print(f"{i}. {msg['Text']} --> {msg['Label']}")

    print("\nFeatures considered for classification:")
    for feat in features:
        print("-", feat)

    # Step 4: Possible mistakes in spam detection
    mistakes = [
        "False positives: marking a normal message as spam",
        "False negatives: missing an actual spam message",
        "Overfitting on certain keywords may ignore context",
        "Short messages may be misclassified"
    ]

    print("\nPossible Mistakes / Challenges:")
    for m in mistakes:
        print("-", m)

    input("\nPress Enter to exit...") 

if __name__ == "__main__":
    main()