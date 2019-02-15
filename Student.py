class Student:
    total=0
    def __init__(self):
        Student.total = Student.total + 1
        self.result={'java':0,'DAA':0,'TOC':0,'ICT':0,'AOS':0,'CN':0,'avg':0}
        self.info={'name':'new student','roll':None,'branch':None,'year':None}
        self.fee={'payed':None,'panding':None,'fine':None}
        self.info['name']=f'{self.info["name"]} ({Student.total})'
    def setInfo(self):
        for var in self.info:
            self.info[var]=input(f'enter {var} of student ')

    def getInfo(self):
        # print(f'Name:\t{self.info["name"]}\nRoll:\t{self.info["roll"]}\nBranch:\t{self.info["branch"]}\nYear:\t{self.info["year"]}')
        for var in self.info:
            print(f'{var} {self.info[var]}')
    def setResult(self):
        for var in self.result:
            if var=='avg':
                break
            self.result[var]=int(input(f'enter matks of {var} '))
            self.result['avg']=self.result['avg']+self.result[var]
        self.result['avg']=self.result['avg']//6
    def __str__(self):
        return str(self.info['name'])