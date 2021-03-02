file = open(input("ΔΩΣΕ ΤΟ ΟΝΟΜΑ ΤΟΥ ΑΡΧΕΙΟΥ:"), 'r')       #Ανοιγμα αρχειου που δινει ο χρήστης
f=open("apotelesma.txt","w")#Ανοιγμα αρχειου ή δημιουργια του αν δεν υπαρχει για την εμφάνιση του αποτελέσματος
while 1:

    # read by character
    char = file.read(1)
    if not char:
        break
    #Υπολογισμός κατοπτρικού χαρακτήρα
    katoptrikos_arithmos=128-ord(char)
    katoptrikos_xaraktiras=chr(katoptrikos_arithmos)
    f.write(katoptrikos_xaraktiras)

file.close()
f.close()
f=open("apotelesma.txt","r")

apotelesma=f.read()
anapoda=apotelesma[::-1]#Ανάποδη γραφή του αποτελέσματος
print(anapoda)
f.close()
