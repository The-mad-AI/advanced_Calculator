from mylibrary import Library


def run_library_system():
    lib = Library()
    
    while True :
        print("system modirite ketabkhane \n")
        print("1. ezafe kardan ketab")
        print("2. hazf ketab")
        print("3. jostojoy ketab")
        print("4. namayesh ketab ha")
        print("5. khoroj")
        
        choice = input("ebtekhab shoma: ")
        
        if choice == '1' :
            title = input("onvane ketab: ")
            author = input("name nevisande: ")
            lib.add_book(title, author)
            
        elif choice == '2':
            title = input("onvane ketab baray hazf: ")
            lib.remove_book(title)
            
        elif choice == '3':
            title = input("onvane ketab braye jostejo: ")
            lib.search_book(title)
            
        elif choice == '4':
            lib.show_book()
            
        elif choice == '5':
            print("khodahafez")
            break
            
        else:
            print("gozine na motabar ast lotfn dobre talash konid !")
            
if __name__ == "__main__":
    run_library_system()