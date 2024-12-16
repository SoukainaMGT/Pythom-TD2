def inverser_chaine(mot):
  inv=""
  for i in range(-1,-len(mot)-1,-1):
    inv+=mot[i]
  return inv