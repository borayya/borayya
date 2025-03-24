class date:
    def __init__(self,a,b,c):
        self.d=a
        self.m=b
        self.y=c
    def day(self):
        print("day=",self.d)
    def month(self):
        print("month=",self.m)
    def year(self):
        print("year=",self.y)
    def monthname(self):
        months=['unknown','january','february','march','april','may','jun','july','august','september','october','november','december']
        print("monthname:",months[self.m])
    def is
    
    leapyear(self):
        if(self.y%400==0)and(self.y%100==0):
          print("is a leap year")
        elif(self.y%4==0)and(self.y%100!=0):
          print("is a leap year")
        else:
          print("it is not leap year")
d1=date(3,8,2000)
d1.day()
d1.month()
d1.year()
d1.monthname()
d1.isleapyear()
    