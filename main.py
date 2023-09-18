import os
if __name__ == '__main__':
    print("Welcome to Robospeaker 1.1 ")
    while (True):
        x = input("Enter what do you want me to pronounce : ")
        if x == "bye":
            os.system("say 'bye bye friend'") 
            break
        command = f"say {x}"
        os.system(command)