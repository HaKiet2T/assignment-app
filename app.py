def grade_submission(assignment_id, student_name, score):
    for assignment in assignments:
        if assignment["id"] == assignment_id:
            assignment["submissions"].append({
                "student": student_name,
                "score": score
            })
            return assignment
    return None

# Test thử chấm điểm
if __name__ == "__main__":
    a = create_assignment("Bài tập 2", "In ra bảng cửu chương", "2025-07-01")
    grade_submission(a["id"], "Nguyễn Văn A", 9.5)
    print("Bài tập đã chấm:", a)
