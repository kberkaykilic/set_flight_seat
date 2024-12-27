import random

def print_menu():
    print("Menu:\n"
          "1-THY\n"
          "2-Pegasus\n"
          "3-Çıkış\n")
pegasus_seats = [False, False, False, False, False, False, False, False, False, False]
thy_seats = [False, False, False, False, False, False, False, False, False, False]

def is_thy_business_full():
    for i in range(5):
        if thy_seats[i] == False:
            return False
    return True

def is_thy_ekonomi_full():
    for i in range(5, 10):
        if thy_seats[i] == False:
            return False
    return True

def is_thy_full():
    for i in range(10):
        if thy_seats[i] == False:
            return False
    return True


def thy():
    if is_thy_full():
        print("All seats are full")
        return
    print("1-Business\n"
          "2-Ekonomi\n")
    secim_2 = int(input("Seçiminiz: "))

    if secim_2 == 1:
        if is_thy_business_full():
            print("Business full")
            return
        print(f"THY business seats= ")
        for i in range(5):
            if thy_seats[i] == False:
                print(f"{i+1}", end=" ")
        print()
        koltuk = int(input("Koltuk(1-5 arası giriniz.): "))
        if 1 <= koltuk <= 5:
            thy_seats[koltuk-1] = True
            print(f"{koltuk} numaralı koltuk size rezerveedildi, iyi uçuşlar!")
        else:
            print("Gecersiz koltuk secimi yaptiniz.")
    elif secim_2 == 2:
        if is_thy_ekonomi_full():
            print("ekonomi full")
            return
        print(f"THY ekonomi seats= ")
        for i in range(5, 10):
            if thy_seats[i] == False:
                print(f"{i + 1}", end=" ")
        print()
        r_koltuk = random.randrange(6, 11)
        while True:
            if thy_seats[r_koltuk-1] == True:
                r_koltuk = random.randrange(6, 11)
            else:
                thy_seats[r_koltuk - 1] = True
                print(f"{r_koltuk} numaralı koltuk size rezerveedildi, iyi uçuşlar!")
                return

def pegasus():
    pass

while True:
    print_menu()
    secim = int(input("Seçiminiz: "))

    if secim==1:
        print("THY Sistemine hoşgeldiniz")
        thy()
    elif secim==2:
        print("Pegasus sistemine hoşgeldiniz")
        pegasus()
    elif secim==3:
        break
    else:
        print("Gecersiz secim.")
