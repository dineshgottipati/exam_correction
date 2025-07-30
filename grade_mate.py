def load_lines(file_name):
    with open(file_name, 'r') as f:
        return f.readlines()

def has_enough_common_words(line1, line2, threshold=2):
    words1 = set(line1.lower().strip().split())
    words2 = set(line2.lower().strip().split())
    common = words1 & words2
    return len(common) >= threshold

def evaluate_answers(correct, student):
    total = len(correct)
    marks = 0
    remarks = []

    for index in range(total):
        if index < len(student):
            if has_enough_common_words(correct[index], student[index]):
                marks += 1
            else:
                remarks.append(f"Line {index + 1}: Needs improvement or doesn't match.")
        else:
            remarks.append(f"Line {index + 1}: Missing from student's answer.")

    return marks, total, remarks

def run_grader():
    correct_answers = load_lines('answer_key.txt')
    student_answers = load_lines('student_answer.txt')

    score, out_of, comments = evaluate_answers(correct_answers, student_answers)

    print("\n=== AutoGrader Result ===")
    print(f"Score: {score} out of {out_of}\n")

    if comments:
        print("Feedback:")
        for comment in comments:
            print("- " + comment)
    else:
        print("Great job! All lines matched perfectly.")

if __name__ == "__main__":
    run_grader()
