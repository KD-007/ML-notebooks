class Accident(Exception):
    def __init__(self, msg:str) -> None:
        self.msg=msg
try:
    raise Accident("apple")
    a+b
except Exception as e:
    print(e.msg)    
       