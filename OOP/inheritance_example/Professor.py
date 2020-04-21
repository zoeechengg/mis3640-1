from BabsonPerson import *

class Professor(BabsonPerson):
    def __init__(self, name, course):
        BabsonPerson.__init__(self, name)
        self.course = course

    def __str__(self):
        return Person.__str__(self) + ' teaches ' + self.course

    def speak(self, utterance):
        newUtterance = 'In course ' + self.course + ' we say '
        return BabsonPerson.speak(self, newUtterance + utterance)

    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)

def main():
    faculty = Professor('Zhi Li', 'MIS 3640')
    print(faculty)
    print(faculty.speak('Python is cool!'))
    print(faculty.lecture('Python is easy.'))


if __name__ == "__main__":
    main()