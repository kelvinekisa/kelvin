from collections import defaultdict

salaries_and_tenures = [
    (83000, 8.7), (88000, 8.1),
    (48000, 0.7), (76000, 6),
    (69000, 6.5), (76000, 7.5),
    (60000, 2.5), (83000, 10),
    (48000, 1.9), (63000, 4.2)
]
print(salaries_and_tenures)
# Average salary for each tenure
salary_by_tenure = defaultdict(list)

for salary, tenure in salary_by_tenure:
    salary_by_tenure[tenure].append(salary)

# keys are years, each value is avarage salary for that tenure.
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()

}

# it might be useful to bucket the tenures
def tenure_bucket(tenure):
    if tenure <2:
        return "less than two"
    elif tenure <5:
        return "between two and five"
    else:
        return "more than five"

# we can group together the salaries corresponding to each bucket

salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# compute te average salary for each group

average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}
print(average_salary_by_bucket)
print(average_salary_by_tenure)


def predict_paid_or_unpaid(years_of_experience):
    if years_of_experience < 3.0:
        return "paid"
    elif years_of_experience < 8.5:
        return "unpaid"
    else:
        return "paid"
