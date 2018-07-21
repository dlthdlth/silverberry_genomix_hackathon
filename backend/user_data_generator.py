import csv

def user_assessment(trait_str):
    with open('csvreports.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == trait_str:
                return row[2]
    return "not found"

def isHarmful(assessment_str):
    try:
        if assessment_str in ['ELIVATED', 'SLIGHTLY ELEVATED']:
            return True
        elif assessment_str in ['NORMAL', 'ADVANTAGE', 'TYPICAL', 'SLIGHTLY ADVANTAGED']:
            return False
    except:
        return None

def main():
    # example usage
    # user_str = user_assessment("Lactose Intolerance")
    # isHarmful(user_str)

if __name__ == '__main__':
    main()
