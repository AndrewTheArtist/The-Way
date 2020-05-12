def loe_failist_järjendisse():
    print("Kokkuleiti 14 kattuvust.")

vene = open("vene.txt","r",encoding = "UTF-8")
ukraina = open("ukraina.txt","r", encoding= "UTF-8")
print("Leidsin, et mõlemas keeles on samad read:")
Andrus = open("väljund.txt",encoding = "UTF-8", mode = "w")
for rida in vene:
    for rida2 in ukraina:
        if rida==rida2:
            print(rida)
            Andrus.write(rida)
        else:
          pass
        break

loe_failist_järjendisse()
Andrus.close()
vene.close()
ukraina.close()
