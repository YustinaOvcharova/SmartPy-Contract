import smartpy as sp

class Registry(sp.Contract):
    def __init__(self, _admin):
        self.init(admin = _admin, registry = sp.map(tkey = sp.TAddress, tvalue = sp.TInt))
        
    @sp.entryPoint
    def addRecord(self, params):
        self.data.registry[sp.sender] = params.amount
        
    @sp.entryPoint
    def addRecordAdmin(self, params):
        sp.verify(sp.sender == self.data.admin)
        self.data.registry[params.account] = params.amount
        
        
@addTest(name = "RegistryTest")
def RegistryTest():
    scenario = sp.testScenario()
    scenario.h1("Resgistry")
    c1 = Registry(sp.address("KT1UjFQxXPbjptnDbMd5MkDZrdTN7DsDU9Lk"))
    scenario += c1
    
    scenario += c1.addRecord(amount = 1000).run(sender = "tz1-address-1111")
    scenario += c1.addRecord(amount = 2222).run(sender = "tz1-address-2222")
    scenario += c1.addRecord(amount = 31313131).run(sender = "tz1-address-3333")
    scenario += c1.addRecordAdmin(account = sp.address("tz1-address-1111"), amount = 99999).run(sender = "KT1UjFQxXPbjptnDbMd5MkDZrdTN7DsDU9Lk")
    scenario += c1.addRecordAdmin(account = sp.address("tz1-address-4444"), amount = 2134).run(sender = "KT1UjFQxXPbjptnDbMd5MkDZrdTN7DsDU9Lk")
    
    