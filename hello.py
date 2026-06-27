def get_grade(score):
    if score >= 80:
        return "Grade A"
    elif score >= 70:
        return "Grade B"
    elif score >= 60:
        return "Grade C"
    elif score >= 50:
        return "Grade D"
    else:
        return "Grade F"


def main():
    try:
        score_input = input("กรุณาใส่คะแนน: ")
        score = float(score_input)
    except ValueError:
        print("กรุณาใส่ตัวเลขคะแนนที่ถูกต้อง")
        return

    grade = get_grade(score)
    print(f"ผลการประเมิน: {grade}")


if __name__ == "__main__":
    main()
