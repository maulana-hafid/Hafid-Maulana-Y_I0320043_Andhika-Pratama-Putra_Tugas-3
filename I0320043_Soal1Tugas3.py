list_teman = ["Alam", "Ojat", "Issa", "Ilham", "Fadhila", "Ivan", "Hilmy", "Ara", "Gea", "Rian"]
print("====================================")
#Index nomor 4,6,7
print("List teman index nomor 4,6,7: ", list_teman[4], list_teman[6], list_teman[7])
print("====================================")

#Ganti nama teman index nomor 3,5,9
print("List teman awal: ", list_teman)
list_teman[3] = "Washul"
list_teman[5] = "Pasya"
list_teman[9] = "Athan"
print("List teman diganti: ", list_teman)
print("====================================")

#Menambah 2 teman
list_teman.append("Memed")
list_teman.append("Bagus")
print("Total nama teman: ", list_teman)
print("====================================")

for teman in list_teman:
    print("Teman saya",teman)