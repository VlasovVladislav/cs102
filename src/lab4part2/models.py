class Respondent:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class AgeGroup:
    def __init__(self,min_age: int,max_age: int | None, respondents: list[Respondent]):
        self.min_age = min_age
        self.max_age = max_age
        self.respondents = respondents

    def contains(self, age: int) -> bool:
        if self.max_age is not None:
            if self.min_age <= age <= self.max_age:
                return True
        else:
            if self.min_age <= age:
                return True
        return False

    def add_respondent(self,respondent: Respondent) -> None:
        if self.contains(respondent.age):
            self.respondents.append(respondent)

    def sort_respondents(self) -> None:
        self.respondents.sort(key=lambda r: (-r.age,r.name))

class AgeGroups:
    def __init__(self,boundaries: list[int]):
        self.check_boundaries(boundaries)
        self.groups = []
        min_age = 0
        for boundary in boundaries:
            max_age = boundary
            self.groups.append(AgeGroup(min_age,max_age,[]))
            min_age = max_age + 1
        self.groups.append(AgeGroup(min_age,None,[]))

    def check_boundaries(self,boundaries: list[int]) -> None:
        if not(boundaries == sorted(boundaries) and len(boundaries) == len(set(boundaries))):
            raise ValueError

    def add_respondent(self,respondent: Respondent) -> None:
        for group in self.groups:
            if group.contains(respondent.age):
                group.add_respondent(respondent)
                break

    def get_non_empty_groups(self) -> list[AgeGroup]:
        results = []
        for i in range(len(self.groups) - 1,-1,-1):
            group = self.groups[i]
            group.sort_respondents()
            if group.respondents:
                results.append(group)
        return results
