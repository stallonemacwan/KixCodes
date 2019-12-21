def kix_code(addr):
  new = addr.split(",")
  ans = new[2][:8]
  second = new[1].split(" ")
  check = second[2]
  final = check.replace("-","X")
  #print(final)
  ans = ans+final
  print(ans.replace(" ",""))




kix_code("PostNL, Postbus 30250, 2500 GG 's Gravenhage")
kix_code("Liesanne B Wilkens, Kogge 11-1, 1657 KA Abbekerk")
kix_code("Dijk, Antwoordnummer 80430, 2130 VA Hoofddorp")
kix_code("Mahir F Schipperen, IJsselmeerlaan 31, 8304 DE Emmeloord")
