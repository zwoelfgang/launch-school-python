def get_grade(score1, score2, score3):
    average = (score1 + score2 + score3) / 3
    
    if average >= 90 and average <= 100:
        return 'A'
    elif average >= 80 and average < 90:
        return 'B'
    elif average >= 70 and average < 80:
        return 'C'
    elif average >= 60 and average < 70:
        return 'D'
    elif average >= 0 and average < 60:
        return 'F'

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
