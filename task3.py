import random
replies={
        'wifi' : 'WiFi is excellent across the campus.',
        'library': 'The library is closed today',
        'deadline': 'Your deadline has been extended by two days',
        'teacher':'teacher will be there soon',
        'results':'results will be out by next month',
        'lab':'lab is closed today',
        'food':'Cafeteria is on 1st floor and Canteen is on 2nd floor'
    
    }
random_replies = ['Hmm','Oh, yes, I see','Tell me more']

def email_checker(email_address,domain): 
    """validates an email passed when called"""
    if email_address.count('@')==1 and email_address.index('@')>=2 and domain in email_address:  #it checks the email
        return True
    elif domain not in email_address:
        return False
    else:
        return False

def get_reply(question):
    """it receives question and print the answers"""
    val= replies.values()
    replies_list = list(val)
    if 'wifi' in question:
        print(replies_list[0])
    elif 'library' in question:
        print(replies_list[1])
    elif 'deadline' in question:
        print(replies_list[2])
    elif 'teacher' in question:
        print(replies_list[3])
    elif 'results' in question:
        print(replies_list[4]) 
    elif 'lab' in question:
        print(replies_list[5])
    elif 'food' in question:
        print(replies_list[6])       
    elif 'bye' in question or 'exit' in question:
        return 0
    else:
        print(random.choice(random_replies))

def main():
    """the main program begins from here"""
    print("Welcome to pop chat\nOne of our operators will be pleased to help you today.")
    operator_names = ["Janice","Candice","Karen","Jennifer","Florence"]
    email_address = input("Please enter your Poppleton email address:")

    if email_checker(email_address,domain="@pop.ac.uk") == True: #it pass the value and check the condition
        username = email_address[0:email_address.index('@')]
        print(f"\nHello,{username}! Thank you, and welcome to Pop Chat !")
        print(f"My name is {random.choice(operator_names)}, and it will be my pleasure to help you.")
        
        while True:
                question = input("---->")
                if random.randint(0,10)==0: #it checks the number if number is 0 then network error
                    print("Network Error")
                    break
                if get_reply(question) == 0: #it pass the value and check the result
                    break 
        print(f"Thank {username}, for using popchat.See you soon!\n")     
    else:
        print("Invalid email id")

main()
