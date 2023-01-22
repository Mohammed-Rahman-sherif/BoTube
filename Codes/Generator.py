import random
import string
import pandas as pd
import os

CredentialsYT = {}
OldMailId = []
OldPassword = []
OldUserFirst = []
OldUserLast = []
GeneratedMailId = []
GeneratedPassword = []
UserFirst = []
UserLast = []

class Generate:
    def __init__(self, GenerateCount = 100):
        self.GenerateCount = GenerateCount

    def MailPassGenerator(self):
        j = 0
        for i in range(self.GenerateCount + j):
            TempMailId = (''.join(random.choices(string.ascii_letters, k = 14))).lower() + "@gmail.com"
            if(TempMailId not in GeneratedMailId and TempMailId not in OldMailId):
                TempPassword = TempMailId[:4] + TempMailId[10:14] + "@098"
                TempUserFirst = TempMailId[:4]
                TempUserLast = TempMailId[6:10]
                GeneratedMailId.append(TempMailId)
                GeneratedPassword.append(TempPassword)
                UserFirst.append(TempUserFirst)
                UserLast.append(TempUserLast)
            else:
                j += 1
        CredentialsYT["MailId"] = OldMailId + GeneratedMailId
        CredentialsYT["Password"] = OldPassword + GeneratedPassword
        CredentialsYT["FirstName"] = OldUserFirst + UserFirst
        CredentialsYT["LastName"] = OldUserLast + UserLast
        return CredentialsYT

if(os.path.exists("../Credentials.csv")):
    CredentialsDetails = pd.read_csv("../Credentials.csv")
    for Mail in CredentialsDetails.MailId:
        OldMailId.append(Mail)
    for Pass in CredentialsDetails.Password:
        OldPassword.append(Pass)
    for FName in CredentialsDetails.FirstName:
        OldUserFirst.append(FName)
    for LName in CredentialsDetails.LastName:
        OldUserLast.append(LName)

GeneratorObject = Generate(5)
print(GeneratorObject.MailPassGenerator())
df = pd.DataFrame(CredentialsYT)
df.to_csv("../Credentials.csv", index = False, header = True)
