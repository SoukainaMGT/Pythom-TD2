def supp_espace(ch):
  ind=0
  for i in ch:
    if i==" ":
      ind+=1
    else:
      break
  chn=""
  for i in range(ind,len(ch)):
    chn+=ch[i]
  return chn