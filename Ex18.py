date1={}
jours_du_mois={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

date1["jour"]=int(input("Entrez le jour:"))
date1["mois"]=int(input("Entrez le mois:"))
date1["annee"]=int(input("Entrez l'année:"))

def estBissextile(date1):
  if (date1["annee"]%4==0 and date1["annee"]%100!=0) or (date1["annee"]%400==0):
    return 1
  else:
    return 0

if estBissextile(date1)==1:
  jours_du_mois[2]=29

def dateJuste(date1):
  if date1["jour"]<=jours_du_mois[date1["mois"]] and date1["jour"]>0 and date1["mois"]<=12 and date1["mois"]>0 and date1["annee"]>0:
    return 1
  else:
    return 0

def datedulendemain(date1):
  date2=date1.copy()
  date2["jour"]+=1
  if date2["jour"]>jours_du_mois[date2["mois"]]:
    date2["jour"]=1
    date2["mois"]+=1
  if date2["mois"]>12:
    date2["mois"]=1
    date2["annee"]+=1
  return date2

def comparedate(date1,date2):
  if date1["annee"]>date2["annee"]:
    return 1
  elif date1["annee"]<date2["annee"]:
    return -1
  else:
    if date1["mois"]>date2["mois"]:
      return 1
    elif date1["mois"]<date2["mois"]:
      return -1
    else:
      if date1["jour"]>date2["jour"]:
        return 1
      elif date1["jour"]<date2["jour"]:
        return -1
      else:
        return 0

def ecartjour(date1,date2):
  ecart=0
  if date1["annee"]!=date2["annee"]:
    if comparedate(date1,date2)==1:
      for i in range(date2["annee"],date1["annee"]):
        if (i%4==0 and i%100!=0) or (i%400==0):
          ecart+=366
        else:
          ecart+=365
    else:
      for i in range(date1["annee"],date2["annee"]):
        if (i%4==0 and i%100!=0) or (i%400==0):
          ecart-=366
        else:
          ecart-=365
  if date1["mois"]!=date2["mois"]:
    if date1["mois"]>date2["mois"]:
      for i in range(date2["mois"],date1["mois"]):
        ecart+=jours_du_mois[i]
    if date1["mois"]<date2["mois"]:
      for i in range(date1["mois"],date2["mois"]):
        ecart-=jours_du_mois[i]
    ecart+=date1["jour"]-date2["jour"]
  return ecart