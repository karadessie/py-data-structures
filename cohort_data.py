from unicodedata import name


def get_houses():
    
    houses = set()

    cohort_data = open("cohort_data.txt")

    for line in cohort_data:
        house = line.rstrip().split('|')[2]
        if house:
            houses.add(house)

    return houses

def get_name():

    name = input("\nWhat is the person's first and last name? ")

    return name

def students_by_cohort(cohort='All'):
    
    students = []

    cohort_data = open("cohort_data.txt", "r")

    for line in cohort_data:
        first, last, _, _, cohort_name = line.rstrip().split('|')

        if cohort_name not in ('I', 'G') and cohort in ('All', cohort_name):
            students.append(f'{first} {last}')

    return sorted(students)


def all_names_by_house():
 
    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    cohort_data = open("cohort_data.txt", "r")

    for line in cohort_data:
        first, last, house, _, cohort_name = line.rstrip().split('|')

        full_name = f'{first} {last}'

        if house:
            if house == "Dumbledore's Army":
                dumbledores_army.append(full_name)
            elif house == 'Gryffindor':
                gryffindor.append(full_name)
            elif house == 'Hufflepuff':
                hufflepuff.append(full_name)
            elif house == 'Ravenclaw':
                ravenclaw.append(full_name)
            elif house == 'Slytherin':
                slytherin.append(full_name)
        else:
            if cohort_name == 'G':
                ghosts.append(full_name)
            elif cohort_name == 'I':
                instructors.append(full_name)

    return [sorted(dumbledores_army),
            sorted(gryffindor),
            sorted(hufflepuff),
            sorted(ravenclaw),
            sorted(slytherin),
            sorted(ghosts),
            sorted(instructors), ]


def all_data():

    all_data = []

    cohort_data = open("cohort_data.txt", "r")

    for line in cohort_data:
        first, last, house, advisor, cohort_name = line.rstrip().split('|')
        all_data.append((f'{first} {last}', house, advisor, cohort_name))

    return all_data


def get_cohort_for():

    name = input("\nWhat is the person's first and last name? ")
    
    for full_name, _, _, cohort_name in all_data():
        if full_name == name:
            return cohort_name


def find_duped_last_names():
    
    dupes = set()
    seen = set()

    for full_name, _, _, _ in all_data():
        last = full_name.split(' ')[-1]

        if last in seen:
            dupes.add(last)

        seen.add(last)

    return dupes


def get_housemates_for():

    get_name()
    
    housemates = set()

    target_person = None
    for person in all_data():
        full_name, house, _, cohort_name = person

        if full_name == name:
            target_person = person
            break

    if target_person:
        _, target_house, _, target_cohort = target_person

        for full_name, house, _, cohort_name in all_data("cohort_data.txt"):
            if ((house, cohort_name) == (target_house, target_cohort) and
                    full_name != name):
                housemates.add(full_name)

    return housemates

def main():

    get_houses()

    get_name()

    students_by_cohort()

    all_names_by_house()

    all_data()

    get_cohort_for()

    find_duped_last_names()

    get_housemates_for()

main()
    
###################  DOCTEST   #########################
if __name__ == '__main__':
    import doctest

    result = doctest.testfile('cohort_data.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
