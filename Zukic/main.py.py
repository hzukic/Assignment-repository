# This is an assignment for Data Stewardship
# Student: Haris Zukic
# Date: 6.1.2025

# Step 1: Importing a library for visualization
import matplotlib.pyplot as plt

# Step 2: Definition of a function to calculate the average score
def calculate_average(scores):
    if not scores:  # Handle empty lists
        return 0
    return sum(scores) / len(scores)

# Step 3: Main program
def main():
    file_name = "students_scores.txt"

    # Step 4: Read the file
    with open(file_name, "r") as file:
        lines = file.readlines()
    
    # Step 5: Arrays for names and averages
    names = []
    averages = []

    # Step 6: Processing the lines in the file
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) < 2:  # Skip malformed lines
            print(f"Skipping malformed line: {line}")
            continue

        name = parts[0]  # First part is the name
        scores = list(map(int, parts[1:]))  # Convert the rest to integers

        # Step 8: Calculate average score
        avg = calculate_average(scores)

        # Step 9: Save the name and average
        names.append(name)
        averages.append(avg)

        # Step 10: Check if the average is above 70
        if avg >= 70:
            print(f"{name} passed with an average of {avg:.2f}.")
        else:
            print(f"{name} did not pass with an average of {avg:.2f}.")
    
    # Step 11: Diagram to show averages
    plt.bar(names, averages, color="skyblue")
    plt.axhline(y=70, color='red', linestyle='--', label='Passing Mark (70%)')
    plt.title("Student Average Scores")
    plt.xlabel("Students")
    plt.ylabel("Average Score")
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
    plt.tight_layout()  # Adjust layout
    plt.show()

# Step 12: Main program end
if __name__ == "__main__":
    main()

# End of the code