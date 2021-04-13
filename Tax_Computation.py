#Editor: Jacky & Kalvin


#Self's MPF
PSincome = float(input("Enter self annual income: "))                  #PSinocme = Personal Income
PPincome = float(input("Enter Spouse's annual income: "))
 
Smpf = 0.0
if PSincome >= 7100:                           
    Smpf = PSincome * 0.05 
    if Smpf > 18000: Smpf = 18000
else:
    PSincome = 0
    
Smpf = round(Smpf,0)
print("The self's MPF:", Smpf)

#Spouse's MPF
Pmpf = 0.0
if PPincome >= 7100:                           
    Pmpf = PPincome * 0.05 
    if Pmpf > 18000: Pmpf = 18000
else:
    PPincome = 0
    
Pmpf = round(Pmpf,0)
print("The spouse's MPF is:", Pmpf)

#Tax calculator
PSincome = float(input("Enter self annual income: ")) - 132000 - Smpf
PPincome = float(input("Enter Spouse's annual income: ")) - 132000 - Pmpf
PJincome = PSincome + PPincome-Smpf-Pmpf
 
SSincome = PSincome + 132000
SPincome = PPincome + 132000
SJincome = PSincome + PPincome + 264000
 
PStax = 0.0
PPtax = 0.0
PJtax = 0.0
 
SStax = 0.0
SPtax = 0.0
SJtax = 0.0
 
#PR
#Self Tax
if PSincome <= 0:
   print("The self tax by PR is: 0")
elif PSincome <= 50000:
   PStax = PSincome * 0.02
   if PStax<0: PStax=0
elif PSincome<=100000:
   PStax=(PSincome-50000) * 0.06 + 1000
   if PStax<0: PStax=0
elif PSincome<=150000:
   PStax=(PSincome-100000) * 0.1 + 4000
   if PStax<0: PStax=0
elif PSincome<=200000:
   PStax=(PSincome-150000) * 0.14 + 9000
   if PStax<0: PStax=0
else:
   PStax=(PSincome-200000) * 0.17 + 16000
   if PStax<0: PStax=0
PStax = round(PStax,0)
print("The self tax by PR is:", PStax)


#Spouse Tax
if PPincome <= 0:
   print("The spouse tax by PR is: 0")
elif PPincome <= 50000:
   PPtax = PPincome * 0.02
   if PPtax<0: PPtax=0
elif PPincome<=100000:
   PPtax=(PPincome-50000) * 0.06 + 1000
   if PPtax<0: PPtax=0
elif PPincome<=150000:
   PPtax=(PPincome-100000) * 0.1 + 4000
   if PPtax<0: PPtax=0
elif PPincome<=200000:
   PPtax=(PPincome-150000) * 0.14 + 9000
   if PPtax<0: PPtax=0
else:
   PPtax=(PPincome-200000) * 0.17 + 16000
   if PPtax<0: PPtax=0
PPtax = round(PPtax,0)
print("The spouse tax by PR is:", PPtax)
print('Total tax payable by separation is:', PStax + PPtax)


#Joint assessment
if PJincome <= 0:
   print("The joint tax by PR is: 0")
elif PJincome <= 50000:
   PJtax = PJincome * 0.02
   if PJtax<0: PJtax=0
elif PJincome<=100000:
   PJtax=(PJincome-50000) * 0.06 + 1000
   if PJtax<0: PJtax=0
elif PJincome<=150000:
   PJtax=(PJincome-100000) * 0.1 + 4000
   if PJtax<0: PJtax=0
elif PJincome<=200000:
   PJtax=(PJincome-150000) * 0.14 + 9000
   if PJtax<0: PJtax=0
else:
   PJtax=(PJincome-200000) * 0.17 + 16000
   if PJtax<0: PJtax=0
PJtax = round(PJtax,0)
print("The join assessment tax by PR is:", PJtax)


#SR
SStax = SSincome * 0.15 
print("The self tax by SR is:", SStax)
SPtax = SPincome * 0.15
print("The spouse tax by SR is:", SPtax)	
print('Total tax payable by separation is:', SStax + SPtax)
SJtax = SJincome * 0.15
print("The join assessment tax by SR is:", SJtax)


#Recommendation
if PSincome + 132000 < 132000:                                                              # 132000 have been minus in Tax calculator
   print(" ( Recommendation: You should apply the joint assessment )")
elif  PPincome + 132000 < 132000: 
    print("( Recommendation: You should apply the joint assessment )")
else:
    print("( Recommendation: You should apply the separate assessment )")
   
