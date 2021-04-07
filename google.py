import webbrowser,time,checkurl

url1 = input("Enter your web1: ")
url2 = input("Enter your web2: ")
url3 = input("Enter your web3: ")

if(checkurl.isValidURL(url1) == False or checkurl.isValidURL(url2) == False or checkurl.isValidURL(url3) == False ):
    print("dekh k type kr please")

webbrowser.open(url1)
time.sleep(3)
webbrowser.open_new_tab(url2)
time.sleep(3)
webbrowser.open_new_tab(url3)
time.sleep(3)




