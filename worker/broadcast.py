from zzcore import StdAns

class Ans(StdAns):
    AllowUser = [1318000868]

    def GETMSG(self):
        groups = self.getgroups()
        
        msg = ""
        for g in groups:
            msg += g["group_name"] + "\n"

        return msg
