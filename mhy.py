import pandas as pd

data = {
    "Employee ID": ["161E90", "161F91", "161F99", "171E20", "171G30"],
    "Name": ["Raman", "Himadri", "Jaya", "Tejas", "Ajay"],
    "Age": [41, 38, 51, 30, 45],
    "Salary(PM)": [56000, 67500, 82100, 55000, 44000]
}

df = pd.DataFrame(data)


class Employee:
    def _init_(self, data):
        self.data = data

    def sort_age(self):
        self.sdf = self.data.sort_values(by=["Age"], ascending=True)
        return self.sdf

    def sort_name(self):
        self.sdf = self.data.sort_values(by=["Name"], ascending=True)
        return self.sdf

    def sort_salary(self):
        self.sdf = self.data.sort_values(by=["Salary(PM)"], ascending=True)
        return self.sdf


ob = Employee(df)

choice = 1

while choice:
    print("0. Exit")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print(ob.sort_age())
    elif choice == 2:
        print(ob.sort_name())
    elif choice == 3:
        print(ob.sort_salary())
    elif choice == 0:
        print("Exiting")
    else:
        print("Invalid Option")