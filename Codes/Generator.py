import random
import string
import pandas as pd

CredentialsYT = {}
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
            TempMailId = (''.join(random.choices(string.ascii_letters, k = 7))).lower() + "@gmail.com"
            if((TempMailId not in GeneratedMailId)):
                TempPassword = TempMailId[:3] + TempMailId[4:7] + "@" + "098"
                TempUserFirst = TempMailId[:4]
                TempUserLast = TempMailId[4:7]
                GeneratedMailId.append(TempMailId)
                GeneratedPassword.append(TempPassword)
                UserFirst.append(TempUserFirst)
                UserLast.append(TempUserLast)
                CredentialsYT["MailId"] = GeneratedMailId
                CredentialsYT["Password"] = GeneratedPassword
                CredentialsYT["FirstName"] = UserFirst
                CredentialsYT["LastName"] = UserLast
            else:
                j += 1
        return CredentialsYT

GeneratorObject = Generate(5)
print(GeneratorObject.MailPassGenerator())
df = pd.DataFrame(CredentialsYT)
df.to_csv("Credentials.csv", index = False, header = True)