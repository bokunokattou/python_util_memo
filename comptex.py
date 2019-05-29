class Ccomptex:
    def __init__(self,AtexPath,BtexPath):
        self.Af = open(AtexPath)
        self.Bf = open(BtexPath)
        self.splitfor = "\n"
        self.AtexArr = []
        self.BtexArr = []
        self.flag = False
    def __del__(self):
        self.Af.close()
        self.Bf.close()
    def take(self):
        self.AtexArr = self.Af.read().split(self.splitfor)
        self.BtexArr = self.Bf.read().split(self.splitfor)
    def forTest(self,text):
        return text.split(self.splitfor)
    def check(self):        
        for (a, b) in zip(self.AtexArr, self.BtexArr):
            if str(a) == str(b):
                pass
            else:
                self.flag = True
                print("A:",str(a))
                print("B:",str(b))
        if ~self.flag:
            print("no matter")



Apath = "type_A.txt"
Bpath = "type_B.txt"

texs = Ccomptex(Apath,Bpath)
texs.check()
del texs
