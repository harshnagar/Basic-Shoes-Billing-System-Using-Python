
from time import gmtime, strftime

print("-----------------------------------------------------------------------")
print("WELCOME TO SHOE BILLING SYSTEM")

def main():

    print("-----------------------------------------------------------------------")
    print("Available Offers:\n# Get 10 % off on your Second Order!"
          "\n# Get 30% off on purchase of Adidas Shoes!"
          "\n# Get 20% Off on purchase of Puma Shoes!")
    print("-----------------------------------------------------------------------")
    inp = int(input("Please Choose the Correct Options from given below Menu:\n"
                  "1 >> To list all Our Products."
                  "\n2 >> To Enter your Billing Details."
                    "\n3 >> To Check your Previous Billing Details."
                    "\n4 >> Exit."))
    if inp == 1:
        with open("Shoes List.txt",'r') as sl:
            print(sl.read())
        main()
                    
    elif inp == 2:
        total_order=0
        date_time = str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        cus_name = input("Please Enter your Name : ")
        shoe_code = int(input("Please Enter Shoe Code your Purchased : "))
        shoe_brand = input("Please Enter Shoes Brand you Purchased : ")
        cus_pn = int(input("Please Enter your Mobile Number : "))
        cus_add = input("Please Enter your Address : ")
        total_amount = int(input("Please Enter Total Amount of your Purchase : "))
        try:                
            with open(str(cus_pn)+".txt", "r") as db:
                read_file = db.read()
                total_order=read_file.count("Order")
                if total_order == 0 or total_order > 1:
                    if shoe_brand.lower() == "puma":
                        ta = total_amount - (total_amount / 100 * 20)
                        total_amount = ta
                        print("-----------------------------------------------------------------------")
                        print("Congratulation you get 20% off as per the offers now total to be paid: ₹", ta)
                    elif shoe_brand.lower() == "adidas":
                        ta = total_amount - (total_amount / 100 * 30)
                        total_amount = ta
                        print("-----------------------------------------------------------------------")
                        print("Congratulation you get 30% off as per the offers now total to be paid: ₹", ta)
                    else:
                        print("-----------------------------------------------------------------------")
                        print("Total Amount to be Paid :", total_amount)
                elif total_order == 1:
                    if shoe_brand.lower() == "puma":
                        ta = total_amount - (total_amount / 100 * 30)
                        total_amount = ta
                        print("-----------------------------------------------------------------------")
                        print("Congratulation you get 30% off as per the offers now total to be paid: ₹", ta)
                    elif shoe_brand.lower() == "adidas":
                        ta = total_amount - (total_amount / 100 * 40)
                        total_amount = ta
                        print("-----------------------------------------------------------------------")
                        print("Congratulation you get 40% off as per the offers now total to be paid: ₹", ta)

                elif shoe_brand.lower() == "puma":
                    ta = total_amount - (total_amount / 100 * 20)
                    total_amount = ta
                    print("-----------------------------------------------------------------------")
                    print("Congratulation you get 20% off as per the offers now total to be paid: ₹", ta)

                elif shoe_brand.lower() == "adidas":
                    ta = total_amount - (total_amount / 100 * 30)
                    total_amount = ta
                    print("-----------------------------------------------------------------------")
                    print("Congratulation you get 30% off as per the offers now total to be paid: ₹", ta)
        
        except FileNotFoundError:            
                if shoe_brand.lower() == "puma":
                    ta = total_amount - (total_amount / 100 * 20)
                    total_amount = ta
                    print("-----------------------------------------------------------------------")
                    print("Congratulation you get 20% off as per the offers now total to be paid: ₹", ta)

                elif shoe_brand.lower() == "adidas":
                    ta = total_amount - (total_amount / 100 * 30)
                    total_amount = ta
                    print("-----------------------------------------------------------------------")
                    print("Congratulation you get 30% off as per the offers now total to be paid: ₹", ta)
                else:
                    print("-----------------------------------------------------------------------")
                    print("Total Amount to be Paid : ₹", total_amount)
        
        with open(str(cus_pn)+".txt", "a") as db1:
            data = "Order Placed on : "+date_time+"\n"+"Phone Number : " + str(cus_pn) + "\nCustomer Name : " + cus_name + "\nShoe Code : " + str(shoe_code) + "\nShoe Brand : " + shoe_brand + "\nTotal Amount : " + str(total_amount) + "\nAddress : " + cus_add
            db1.write("\n----------------------------------------\n"
                     +str(data)+"\n----------------------------------------")

        print("Thanks! for Visiting, your Data is now Saved with Us.")
        print("-----------------------------------------------------------------------")
        main()

    elif inp == 3:
        check_pn = int(input("Enter your Phone Number to get your Order Details: "))
        try:
            with open(str(check_pn)+".txt","r") as read_db:
                print("Order placed with Mobile Number "+str(check_pn)+" are:")
                print(read_db.read())
                main()
        except FileNotFoundError:
            print("No Order Exist with Mobile Number : ", check_pn ," Please Try again with Different Mobile Number!")
            print("-----------------------------------------------------------------------")
            main()
    elif inp == 4:
        exit()
    else:
        print("Wrong Input Entered Please Try Again From Given Menus!")
        print("-----------------------------------------------------------------------")
        main()


main()
