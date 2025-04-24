# 80 * 0.2 + 90 * 0.5 + 70 * 0.3 = 16   + 45    + 21     = 82
def calculate_grade(student_name, exam_scores, exam_weights):
    weighted_average = (exam_scores[0] * exam_weights[0] + exam_scores[1] * exam_weights[1] +
                        exam_scores[2] * exam_weights[2])

    print(f"{student_name}'s final grade is: {weighted_average}")

calculate_grade("Fernando", [80,90,70], [0.2,0.5,0.3] )
calculate_grade(exam_scores=[80,90,70], exam_weights=[0.2,0.5,0.3], student_name="Fernando")


def merge_strings(str1, str2, str3, separator=","):
    single_string = str1 + separator + str2 + separator + str3
    return single_string

print(merge_strings("fernando", "vc é", "forte!"))
print(merge_strings("fernando", "vc é", "forte!", ":"))

def calculate_discount(price, discount=10):
    total = price - ((discount/100) * price)
    return total

print(calculate_discount(200, 25))
print(calculate_discount(200))