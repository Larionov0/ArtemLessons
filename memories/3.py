workers = [
    {
        'name': 'Bob',
        'surname': 'Bobenko',
        'job': 'programmer',
        'salary': 2000
    },
    {
        'name': 'Alex',
        'surname': 'Bobenko',
        'job': 'designer',
        'salary': 4000
    },
    {
        'name': 'Nina',
        'surname': 'Bobenko',
        'job': 'programmer',
        'salary': 3000
    },
    {
        'name': 'Ivan',
        'surname': 'Bobenko',
        'job': 'cleaner',
        'salary': 6000
    },
    {
        'name': 'Anna',
        'surname': 'Bobenko',
        'job': 'programmer',
        'salary': 4000
    },
]


def find_average_salary(workers):
    """
    написать функцию, которая принимает структуру, и
    посчитать среднюю зарплату по всем работникам
    """
    sum_salary = 0
    count = 0
    for worker in workers:
        sum_salary += worker['salary']
        count += 1
    return sum_salary / count


def find_richest_worker(workers):
    """
    Принимает структуру и возвращает словарь работника с макс зарплатой
    """
    max_worker = None
    max_salary = 0
    for worker in workers:
        if max_salary < worker['salary']:
            max_salary = worker['salary']
            max_worker = worker

    return max_worker


print(find_richest_worker(workers))
