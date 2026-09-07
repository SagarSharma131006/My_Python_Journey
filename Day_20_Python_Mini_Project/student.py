class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return self.total_marks() / len(self.marks)

    def grade(self):

        average = self.average_marks()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def display(self):

        print("\n------------------------------")
        print(f"Name       : {self.name}")
        print(f"Roll No    : {self.roll_no}")
        print(f"Marks      : {self.marks}")
        print(f"Total      : {self.total_marks()}")
        print(f"Average    : {self.average_marks():.2f}")
        print(f"Grade      : {self.grade()}")
        print("------------------------------")

    def to_dict(self):

        return {
            "name": self.name,
            "roll_no": self.roll_no,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data):

        return cls(
            data["name"],
            data["roll_no"],
            data["marks"]
        )