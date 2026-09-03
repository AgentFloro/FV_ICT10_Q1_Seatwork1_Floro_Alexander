from pyscript import document, display
#part 1
#Variables for sale (99$ each)
fishing = "Alex" #stringy cheese
Lake = 15 #integer
FishFarm = "173.70cm" #string
Super_shop = ["Japan, USA, Prabil"]  #list
student_type = False #boolean
Library_of_my_everything = {
    "car_brand" : "Mitsubishi l300",
    "shoe_size" : "4 plus more than my best friend",
    "best_friend" : "Non exsistent. I treat everone equally. "
}  #dictionary
fruits = {"orange", "banana", "apple", "kiwi", "radioactive explosive banana that is different from the other banana"} #set variable
I_Couldnt_afford_an_expensive_tuple_so_I_got_one_From_the_Sari_Sari_store = ("mondays", "tuesday", "wednesday", "thursdingday", "friesday", "saturn", "sunday") #tuple



#time to bring them out to life
display((fishing), target="TonyHawk")
display((Lake), target="TonyHawk")
display((FishFarm), target="TonyHawk")
display((Super_shop), target="TonyHawk")
display((student_type), target="TonyHawk")
display((Library_of_my_everything), target="TonyHawk")
display((fruits), target="TonyHawk")
display((I_Couldnt_afford_an_expensive_tuple_so_I_got_one_From_the_Sari_Sari_store), target="TonyHawk")




#part 2
def addnum(e):# put e for the event handler
        document.getElementById("output1").innerHTML="" #clears previous result

        num1 = float(document.getElementById("input1").value) #get input value
        num2 = float(document.getElementById("input2").value) #get input value
        result = num1 + num2
        display(result, target="output1") #add

def subnum(e):# put e for the event handler
        document.getElementById("output1").innerHTML="" #clears previous result

        num1 = float(document.getElementById("input1").value) #get input value
        num2 = float(document.getElementById("input2").value) #get input value
        result = num1 - num2
        display(result, target="output1") #Subtract

def mulnum(e):# put e for the event handler
        document.getElementById("output1").innerHTML="" #clears previous result

        num1 = float(document.getElementById("input1").value) #get input value
        num2 = float(document.getElementById("input2").value) #get input value
        result = num1 * num2
        display(result, target="output1") #Multiply

def divnum(e):# put e for the event handler
        document.getElementById("output1").innerHTML="" #clears previous result

        num1 = float(document.getElementById("input1").value) #get input value
        num2 = float(document.getElementById("input2").value) #get input value
        result = num1 / num2
        display(result, target="output1") #Divide

def OhioFinalBoss(e):# put e for the event handler
        document.getElementById("output1").innerHTML="" #clears previous result

        num1 = float(document.getElementById("input1").value) #get input value
        num2 = float(document.getElementById("input2").value) #get input value
        result = num1 ** num2 + 2110369723766300 * 2 
        display(result, target="output1") #Go ham
def Sweeperrrr(e):
        document.getElementById("output1").innerHTML="" #Just a clear incase something bad happens
