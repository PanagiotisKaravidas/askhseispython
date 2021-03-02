import re
with open(input("ΔΩΣΕ ΤΟ ΟΝΟΜΑ ΤΟΥ ΑΡΧΕΙΟΥ:"),'r') as file:    #Ανοιγμα αρχειου που δινει ο χρήστης
    i=0
    lexeis=[]
    for line in file:
        #Αφαιρώ περίεργους χαρακτήρες και αριθμούς
        line=re.sub(r'[^\w]',' ',line)
        line=re.sub(r'[0-9]+',' ',line)
        # Διάβασμα της κάθε λέξης
        for word in line.split():

            #Δημιουργία λιστας με τισ λέξεις του αρχείου
            if len(word)<=19:#Κρατάω μονο τις λέξεις που μπορούν να κάνουν ζευγάρι και να είναι 20
                lexeis.append(word)


apanthsh=input("Να επιτρέπεται η ίδια λέξη πολλές φορές ΝΑΙ Η΄ ΟΧΙ;")
while apanthsh!="ΝΑΙ" and apanthsh!="ΟΧΙ":
    apanthsh=input("Να επιτρέπεται η ίδια λέξη πολλές φορές ΝΑΙ Η΄ ΟΧΙ;")

lexeis=sorted(lexeis)#Ταξινομώ με βάση το μήκος την λέξης
if apanthsh=="ΟΧΙ":
    lexeis=list(dict.fromkeys(lexeis))#Καθε λέξη εμφανίζεται μονο μια φορά
file.close()#Κλεισιμο αρχείου
yparxei=False

while len(lexeis)>=2:#Ελέγχος αν η λίστα έχει τουλάχιστον 2 λ΄έξεις
    i=len(lexeis)-1
    eikosi=False
    while i>=1:

        if len(lexeis[0])+len(lexeis[i])==20:#Ελεγχει αν το μηκος των λεξεων ειναι 20
            print("Το ζευγάρι",lexeis[0],lexeis[i],"έχει μήκος 20")
            eikosi=True
            #Διαγραφή ζευγαριού απο το σύνολο
            del lexeis[0]
            del lexeis[i-1]
            yparxei=True#Υπαρχει τουλαχιστον ενα ζευγάρι με συνολικό μηκος 20
            i=i-1
            break#Ωστε να ξανα ξεκινήσει απο την αρχή
        else:
            i=i-1
    if eikosi==False:
        del lexeis[0]
if len(lexeis)==1:
    del lexeis[0]

if yparxei==False:
    print("ΔΕΝ ΥΠΑΡΧΕΙ ΚΑΝΕΝΑ ΖΕΥΓΑΡΙ ΛΕΞΕΩΝ ΜΕ ΣΥΝΟΛΙΚΟ ΜΗΚΟΣ ΧΑΡΑΚΤΗΡΩΝ 20 ")
