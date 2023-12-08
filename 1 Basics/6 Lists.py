Anime = ["DN", "COE", "H"]
print(Anime[0])
print(Anime[-1])
print(Anime[0:3])

Anime[2]="Horimiya"
print(Anime)

TvS = ["GOT", "KK", "ST"]
print("********")
Anime.extend(TvS)
print(Anime)

#### to ad element to last of the list
Anime.append("JK")
print(Anime)

#### to add elemnt where I need it to add
Anime.insert(1 ,"CM")
print(Anime)

#### remove a elemnt if know what it is
Anime.remove("COE")
print(Anime)

#### TO remove the last elemnt in the list
Anime.pop()
print(Anime)

#### to find what we need is in the list or not
## if there is then out put will be the index of it
print(Anime.index("Horimiya"))

#### to count the value we need
print(Anime.count("Horimiya"))

#### to sort the list acoding to alphbet
Anime.sort()
print(Anime)

#### To reverse the oder of the list
## curently its in alphbetical oder
Anime.reverse()
print(Anime)

#### copy list 1 to list 2
Anime2 = Anime.copy()
print(Anime)

#### to get ridofe every elemnt in the list
Anime.clear()
print(Anime)

