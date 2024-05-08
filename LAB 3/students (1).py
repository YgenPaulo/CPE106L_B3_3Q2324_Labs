"""
File: student.py
Resources to manage a student's name and test scores.
"""
import random
class Student(object):

    def __init__(self, name, number):
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        return self.name
  
    def setScore(self, i, score):
        self.scores[i - 1] = score

    def getScore(self, i):
        return self.scores[i - 1]
   
    def getAverage(self):
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        return max(self.scores)
 
    def __str__(self):
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
    def __eq__(self, other):
        return self.name == other.name
    
    def __lt__(self, other):
        return self.name < other.name
    
    def __ge__(self, other):
        return self.name >= other.name

def main():
    listofstudents = []
    student = Student("Ethanes", 5)
    for i in range(1, 6):
        student.setScore(i, 100)
    listofstudents.append(student)

    Ygen = Student("Ygen", 4)
    for i in range(1, 5):
        Ygen.setScore(i,100)
    listofstudents.append(Ygen)
    
    Althea = Student("Althea", 4)
    for i in range(1, 5):
        Axcel2.setScore(i,100)
    listofstudents.append(Althea)
        
    Wong = Student("Wong", 3)
    for i in range(1, 4):
        Wong.setScore(i,100)
    listofstudents.append(Wong)

    random.shuffle(listofstudents)
    print("shuffled", end="->")
    for student in listofstudents:
        print (student.getName(), end =" ")

    listofstudents.sort()
    print()
    print ("Sorted" , end="->")
    for student in listofstudents:
        print (student.getName(), end = " ")
    print()
    print("Printing students")
    for persons in listofstudents:
        print(persons)


if __name__ == "__main__":
    main()


