class student:
  def getstudentdata(self,name,age,city):
    self.name=name
    self.age=age
    self.city=city
  def displaystudentdata(self):
    print("name:",self.name)
    print("age:",self.age)
    print("city:",self.city)
class teacher(student):
  def getteacherdata(self,salary,designation):
    self.salary=salary
    self.designation=designation
  def displayteacherdata(self):
    print("Salary:",self.salary)
    print("desingnation:",self.designation)

obj=teacher()
obj.getteacherdata(20000,"Assistant professor")
obj.displayteacherdata()
obj1=student()
obj.getstudentdata("Akshaya",18,"Chennai")
obj.displaystudentdata()