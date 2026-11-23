import sys
from src.lab4part2.models import AgeGroups,Respondent
arr = sys.argv
try:
    boundaries = [int(x) for x in arr[1:]]
    age_groups = AgeGroups(boundaries)
except ValueError:
    raise ValueError("Границы возрастных некорректны")
respondent = input()
while respondent != 'END':
    respondent = respondent.split(",")
    name = respondent[0].strip()
    age = int(respondent[-1].strip())
    current_respondent = Respondent(name,age)
    age_groups.add_respondent(current_respondent)
    respondent = input()

for group in age_groups.get_non_empty_groups():
    respondents_str = ", ".join(
        f"{r.name} ({r.age})" for r in group.respondents
    )
    if group.max_age is not None:
        print(f'{group.min_age}-{group.max_age}: {respondents_str}')
    else:
        print(f'{group.min_age}+: {respondents_str}')
