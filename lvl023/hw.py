#1) გადავხედოთ ლისტებს და საერთოდ განვლილ მასალას. gavakete
#2) ვინც არ დაასრულეთ საკლასო დავალება, აუცილებლად დაასრულეთ ბოლომდე და თავიდან უყურეთ ჩანაწერს. gavakete

#3) კომენტარების სახით ახსენით როგორ მუშაობს for ციკლი list ებთან. for cikli 
#kitxulobs listebs da ra indexsac chavwert is gamoaqvs. example; list = ['kasper', "kata"]. print(list[1]). es
#gamoitans 'katas'


#4) for ციკლის მეშვეობით გამოიტანეთ ყველა ლუწი რიცხვი 22-დან 104-მდე , და ყველა კენტი რიცხვი 204-დან 426 ამდე.

for i in range (22, 104):
    if i % 2 == 0:
        print(i)

for i in range (204, 426):
    if i % 2 == 0:
        print("")
    else:
        print(i)


#5) მომხმარებელს შემოატანინეთ თავისი ასაკი, შეინახეთ იგი ცვლადში და შეამოწმეთ მეტია თუ არა იგი 18 თუ ნაკლებია უთხარით:  "ჯერ არ ხართ 18 წლის " თუ 18 ის არის ან მეტის უთხარით: "თქვენ გადაცდით ასაკის ზღვარს"

num = int(input("enter your age: "))

if num < 18:
    print("ur young")
else:
    print("ur an adult")