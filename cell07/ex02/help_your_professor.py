def average(scores):
    if not scores:
        return 0
    total = sum(scores.values())
    count = len(scores)
    return total / count

if __name__ == "__main__":
    # Example dictionary
    student_scores = {
        "Alice": 85,
        "Bob": 90,
        "Charlie": 78,
        "Daisy": 92,
        "Eve": 88
    }

    class_average = average(student_scores)
    print(f"Class average: {class_average:.2f}")