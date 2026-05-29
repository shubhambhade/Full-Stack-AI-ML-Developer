from abc import *

class CollegeAutomationSystem(ABC):
    @abstractmethod
    def getStudentAttendance(self):
        pass
    @abstractmethod
    def updateStudentAttendance(self):
        pass
    @abstractmethod
    def getMarks(self):
        pass
    @abstractmethod
    def updateMarks(self):
        pass
    @abstractmethod
    def getFeeInfo(self):
        pass
    @abstractmethod
    def updateFeeInfo(self):
        pass

class SwastikTech(CollegeAutomationSystem):
    def getStudentAttendance(self):
        print("Get Attendance")
    def updateStudentAttendance(self):
        print("Update Attendance")
    def getMarks(self):
        print("Get Marks")
    def updateMarks(self):
        print("Update Marks")
    def getFeeInfo(self):
        print("Get Fee Info")
    def updateFeeInfo(self):
        print("Update Fee Info")
        
swastiktech = SwastikTech()
swastiktech.getStudentAttendance()
swastiktech.updateStudentAttendance()
swastiktech.getMarks()
swastiktech.updateMarks()
swastiktech.getFeeInfo()
swastiktech.updateFeeInfo()