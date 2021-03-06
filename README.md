# CS5103

My student id = fia088

Link of the GitHub repository is: https://github.com/Mayankp11/CS5103.git

**Running the Application:**

For running the application open the folder CS5103 then execute the python file named Mayank_fia088.py
The program can be executed in pycharm, Intellij IDEA or any other python compiler application.

a. After running the file the first requirement(Word count) will run, where user should give the input and it will show the word count. The number of words will be counted and their occurence count will be given as an output.

b. Then second requrement(word replacement) will run automatically, where  user should give the input and it will ask for a word which has to be replaced along with the word which has to be replaced with.

c. The third requirement will execute finally. In that a string is already given. An x variable is given, which has the findall() function which shows a word to be matched in the string. If the word matches, it will give the string as an output else no match.

**User Stories and Test Cases:**
1. First requirement- 
 Script : 
 Asks for a string as an input from user.
 Where you need to insert characters of words.
 
 val = input("Enter your Words: ")
print(word_count(val))   #word_count(val) will count the occurence of words in the string.

Expected result :
Enter your words: Today is is a sunny day
Output : {'Today':1,'is':2,'a':1,'sunny':1,'day':1}

2. Second requirement-
  Script :
  Ask for a string from the user.
  
  val = input("Enter your string : ")
  source = input("Enter the word to replace : ")
  final = input("Enter the word to replace with : ")
  +re.sub(source, final, val     # Regular expression will give the final output.
  
  Expected result:
  Enter your string: I live in San Antonio
  Enter the word to replace : live
  Enter the word to replace with : stay
  Your final sentence is : I stay in San Antonio.
  
3. Third requirement-
   It takes input from the code.
   
   txt = "The rain in Spain"



x = re.findall(r'\bRain\b', txt,flags=re.IGNORECASE)     #findall() regular expression is used.
print(x)

if (x):
    print("Yes, there is at least one match!")    #will be shown as an output if there is a match.
    print(txt)
else:
    print("No match")                             # will be shown as an output if there is no match.
    
    
 Expected result :
 
 # as Rain matches the string #
 
 [Rain}
 Yes, there is at least one match.
 The rain in Spain
 
 
 **For static clone detection**
 I used a tool called 'Pylint' which is used for Python static clone detection.
 And showed me the following output :
 
 ![pylint static clone](https://user-images.githubusercontent.com/100968519/167329708-c1c76429-58ba-4606-bac1-b6d351c883b0.png)
 
 
 
 ** Unit Testing**
 
 Testing was performed on the code, which gave the following output.
 
 For the third requirement, if boundries [\b_word_\b] was not inserted, it din't give correct output.
 
 ![UNit_testing](https://user-images.githubusercontent.com/100968519/167338470-b7ae022a-6736-43c9-9164-d0e9c7a7059f.png)
 
 
 ![unit_test](https://user-images.githubusercontent.com/100968519/167339253-11be18c9-e48c-4d1c-9c0f-40db334c9fb9.png)





*** Output *****
1st requirement.

![1st_req](https://user-images.githubusercontent.com/100968519/167338972-826ded91-56b8-43cc-afad-ec149e884aa8.png)


2nd requirement.

![@nd_req](https://user-images.githubusercontent.com/100968519/167339012-745dcc36-df35-449e-81f7-a76a74635076.png)


3rd requirement.

![3rd_req](https://user-images.githubusercontent.com/100968519/167339059-497e4da2-69a2-4d0d-a1f9-867aacc8cbee.png)













 
 
 
 
 
 
 


  
  

