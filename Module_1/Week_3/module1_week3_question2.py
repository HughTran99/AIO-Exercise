"""Question 2 of homework."""


class Student():
    """Display students' information."""

    def __init__(self, name, yob, grade):
        """Initialize student's name, year of birth, and grade."""
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(f"Name: {self.name}, Yob: {self.yob}, Grade: {self.grade}")


class Doctor():
    """Display doctors' information."""

    def __init__(self, name, yob, specialist):
        """Initialize doctor's name, year of birth, and specialist."""
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(
            f"Name: {self.name}, Yob: {self.yob}, Specialist: {self.specialist}")


class Teacher():
    """Display teachers' information."""

    def __init__(self, name, yob, subject):
        """Initialize teacher's name, year of birth, and subject."""
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(f"Name: {self.name}, Yob: {self.yob}, Subject: {self.subject}")


class Ward():
    """Display wards' information."""

    def __init__(self, name):
        """Initialize ward's name and list of civilians."""
        self.name = name
        self.civilians = []

    def add_person(self, person):
        self.civilians.append(person)

    def describe(self):
        print(f"Ward: {self.name}")
        for person in self.civilians:
            person.describe()

    def count_doctors(self):
        count = 0
        for person in self.civilians:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.civilians.sort(reverse=True, key=lambda x: x.yob)

    def compute_average(self):
        total_age = 0
        for person in self.civilians:
            total_age += person.yob
        return total_age / len(self.civilians)


# Question 1
student1 = Student("Chris", 2007, "12")
student1.describe()

teacher1 = Teacher("Chloe", 1989, "Math")
teacher1.describe()

doctor1 = Doctor("Emmanuel", 1975, "Psychiatry")
doctor1.describe()

teacher2 = Teacher("Michael", 1990, "Science")
doctor2 = Doctor("Isaac", 1981, "Dental")

# Question 2
ward1 = Ward("Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(doctor1)
ward1.add_person(teacher2)
ward1.add_person(doctor2)
ward1.describe()

# Question 3
print(f"Number of doctors: {ward1.count_doctors()}")

# Question 4
ward1.describe()
ward1.sort_age()

# Question 5
print(f"Average year of birth: {ward1.compute_average()}")
