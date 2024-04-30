running = True
while running:
   age = int(input("რამდენის ხარ ?"))
   if age < 18:
    print("შენ ხარ  ბავშვი")
   elif age > 18 and age < 60:
    print("შენ ხარ სლურწლოვანი")
   else :
    print("შენ ხარ მოხუცი")