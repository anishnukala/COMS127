# dictAndFuncts.py
# Anish Reddy Nukala
# Date: 02-04-2024
# Lab Week 12 

def inputValidInteger(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")
            
def calcAAS(a, b, c, d):
    return a + b + c - d

def calcASA(a, b, c, d):
    return a + b - c * d

def calcASM(a, b, c, d):
    return a + b - c * d            

def calcAAA(a, b, c, d):
    return a + b + c + d

def calcAAS(a, b, c, d):
    return a + b + c - d

def calcASA(a, b, c, d):
    return a + b - c + d

def calcSAA(a, b, c, d):
    return a - b + c + d

def calcAAM(a, b, c, d):
    return a + b - c * d

def calcAMM(a, b, c, d):
    return a + b * c * d

def calcASA(a, b, c, d):
    return a + b - c - d

def calcASS(a, b, c, d):
    return a + b - c + d

def calcMMA(a, b, c, d):
    return a - b - c * d

def calcMMM(a, b, c, d):
    return a - b * c * d

def calcMSA(a, b, c, d):
    return a - b - c - d

def calcMSS(a, b, c, d):
    return a - b - c + d

def calcSAA(a, b, c, d):
    return a - b - c - d

def calcSAM(a, b, c, d):
    return a - b - c * d

def calcSMA(a, b, c, d):
    return a - b + c * d

def calcSMS(a, b, c, d):
    return a - b + c - d

def calcSMM(a, b, c, d):
    return a - b + c * d

def calcASS(a, b, c, d):
    return a + b - c - d

def calcASA(a, b, c, d):
    return a + b - c * d

def calcAAM(a, b, c, d):
    return a + b - c * d

def calcMMA(a, b, c, d):
    return a - b - c * d

def calcSAA(a, b, c, d):
    return a - b - c - d

def calcAMA(a, b, c, d):
    return a + b * c + d

def calcSMA(a, b, c, d):
    return a - b + c * d

def calcSMS(a, b, c, d):
    return a - b + c - d

def calcMMS(a, b, c, d):
    return a - b * c - d

def calcSSS(a, b, c, d):
    return a - b - c - d            

def calcMAS(a, b, c, d):
    return a * b + c - d  

def calcAMS(a, b, c, d):
    return a + b * c - d  

def calcMAA(a, b, c, d):
    return a + b * c - d  

def calcMSM(a, b, c, d):
    return a * b + c * d  

def calcSAS(a, b, c, d):
    return a - b + c - d  

def calcSMA(a, b, c, d):
    return a - b * c + d  


def main():

    a = inputValidInteger("input 'a': ")
    b = inputValidInteger("input 'b': ")
    c = inputValidInteger("input 'c': ")
    d = inputValidInteger("input 'd': ")

    calculations = {
        "AAS": calcAAS(a, b, c, d),
        "ASA": calcASA(a, b, c, d),
        "ASM": calcASM(a, b, c, d),
        "AAA": calcAAA(a, b, c, d),
        "AAS": calcAAS(a, b, c, d),
        "ASA": calcASA(a, b, c, d),
        "SAA": calcSAA(a, b, c, d),
        "AAM": calcAAM(a, b, c, d),
        "AMM": calcAMM(a, b, c, d),
        "ASA": calcASA(a, b, c, d),
        "ASS": calcASS(a, b, c, d),
        "MMA": calcMMA(a, b, c, d),
        "MMM": calcMMM(a, b, c, d),
        "MSA": calcMSA(a, b, c, d),
        "MSS": calcMSS(a, b, c, d),
        "SAA": calcSAA(a, b, c, d),
        "SAM": calcSAM(a, b, c, d),
        "SMA": calcSMA(a, b, c, d),
        "SMS": calcSMS(a, b, c, d),
        "SMM": calcSMM(a, b, c, d),
        "ASS": calcASS(a, b, c, d),
        "ASA": calcASA(a, b, c, d),
        "AAM": calcAAM(a, b, c, d),
        "MMA": calcMMA(a, b, c, d),
        "SAA": calcSAA(a, b, c, d),
        "AMA": calcAMA(a, b, c, d),
        "SMA": calcSMA(a, b, c, d),
        "SMS": calcSMS(a, b, c, d),
        "MMS": calcMMS(a, b, c, d),
        "SSS": calcSSS(a, b, c, d),
        "MAS": calcMAS(a, b, c, d),
        "AMS": calcAMS(a, b, c, d),
        "MAA": calcMAA(a, b, c, d),
        "MSM": calcMSM(a, b, c, d),
        "SAS": calcSAS(a, b, c, d),
        "SMA": calcMSA(a, b, c, d),
      
      
    }

    for key, value in calculations.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
