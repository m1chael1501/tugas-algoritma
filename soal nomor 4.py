while True:
    kata = input("masukkan kata: ")
    
    if kata.lower() == kata [::-1].lower():
        print("palindrome")
    else :
        print ("bukan palindrome")
        
    if input("mau coba lagi (y/n)?: ").lower() != "y":
            print("terimakasih")
            break