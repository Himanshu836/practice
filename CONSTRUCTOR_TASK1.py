#CREATE A STUDENT CLASS THAT TAKES NAME & MARKS OF 3 SUBJECTS AS ARGUMENTS IN CONSTRUCTOR.THEN CREATE A METHOD TO PRINT THE AVERAGE.


class student:
    @staticmethod
    def hello():
        print("I am a static method")
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        summ=0
        for val in self.marks:
            summ+=val
        avg=summ/len(self.marks)
        print("your average is : ", avg)
        # return summ/3
marks=[]
# i=3
for i in range(1,4):
    marks.append(int(input("Enter your mark")))
    # i-=1
s1=student("Himanshu",marks)
s1.average()
s1.hello()
# s4=student()
# s4.average()

