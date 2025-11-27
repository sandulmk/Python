class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        
        sec = self.__second + other.__second
        min_carry = sec // 60
        sec = sec % 60

        
        minute = self.__minute + other.__minute + min_carry
        hour_carry = minute // 60
        minute = minute % 60

        
        hour = self.__hour + other.__hour + hour_carry
        hour = hour % 24   

        return Time(hour, minute, sec)

    def display(self):
        print(f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}")



t1 = Time(2, 45, 50)
t2 = Time(3, 20, 30)

t3 = t1 + t2
t3.display()
