class Hamyon:
    def __init__(self):
        self.pul = 0

    def qo_sh(self, miqdor):
        if miqdor > 0:
            self.pul += miqdor
            print(f"+{miqdor} so'm qo‘shildi. Jami: {self.pul} so'm")
        else:
            print("Miqdor musbat bo‘lishi kerak!")

    def sarfla(self, miqdor):
        if miqdor > 0 and miqdor <= self.pul:
            self.pul -= miqdor
            print(f"-{miqdor} so'm sarflandi. Qoldi: {self.pul} so'm")
        else:
            print("Yetarli pul yo‘q yoki miqdor noto‘g‘ri!")

    def ko_rsat(self):
        print(f"Hamyonda: {self.pul} so'm")


mening_hamyonim = Hamyon()

mening_hamyonim.qo_sh(50000)    
mening_hamyonim.qo_sh(30000)   
mening_hamyonim.ko_rsat()       

mening_hamyonim.sarfla(25000)  
mening_hamyonim.sarfla(100000)  
mening_hamyonim.ko_rsat()       
