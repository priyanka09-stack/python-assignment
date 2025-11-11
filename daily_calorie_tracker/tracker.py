import datetime
#Priyanka Singh
#04-11-2025
#Daily Calorie Tracker CLI

print("Welcome all of you to our Daily Calorie Tracker - which helps you track your daily calorie intake and helps in your weight loss or gain plan.")

#asking number of meal user wants to input.
num_meals = int(input("How many meals you want to take?", ))       

meal_names = []                                     #blank lists.
meal_calories = []


for i in range(num_meals):                                   #use of for loop to ask user input for meal name and meal calories.
    name = input(f"Enter meal name.{i + 1}:")
    calories = int(input(f"Enter meal calories for {name}:"))
    meal_names.append(name)                                      #.append used to make lists.
    meal_calories.append(calories)


#for printing meal name and their calories in new line.
print("\nmeal names:" ,meal_names)                          
print("meal calories :",meal_calories)


total_cal = sum(meal_calories)                                               #calculating total calories
print(total_cal)                                                             #printing total calories
avg_cal_per_meal= total_cal / num_meals                                      #calculating average calorie per meal.
print(avg_cal_per_meal)                                                      #printing average calories
daily_calorie_limit = int(input("Enter yor daily calorie limit.",))          #asking user to input daily calorie limit.

#use of conditionals to compare total calorie and daily limit calorie and printing results.
if total_cal == daily_calorie_limit:
    status = "Daily calorie limit achieved."
elif total_cal > daily_calorie_limit:  
    status = "Daily Calorie Limit Exceeded."
else:
    status = "You are under your daily calorie limit."


#making table.

print("\nMeal Name  \tMeal Calories")
print("-------------------------------")
for i in range (num_meals):                                           #using for loop to print all meal name and calories.
    print(f"{meal_names[i]:<15}{meal_calories[i]:>15}")               

print(f"{'Total calories:':<15}{total_cal:>15}")                                    #printing total calories
print(f"{'Average calories:':<15}{avg_cal_per_meal:>15}")                           #printing average calories

#save session log to file
save_file = (input("Will you like to save your file? (yes / no)"))              #asking user to save file or not
if save_file == "yes":                                                          
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")           
    filename = f"calorie{timestamp}.txt"                                    #creating file.
    with open (filename,"w")as file:                                            
        file.write("Session Summary\n")
        file.write(f"date & time{datetime.datetime.now()}\n")                   #writing date and time in file.
        file.write("Meal Details:\n")                                            
        for i in range (num_meals):                                             #using for loop to write meal name and calories.
            file.write(f"{meal_names[i]}:{meal_calories[i]} calories\n")
        file.write("\n")                                                        #new line.
        #writing daily calorie limit ,total calorie and average calories .
        file.write(f"Daily calorie limit:{daily_calorie_limit}\n")                                                 
        file.write(f"Total Calories:{total_cal}\n")                              
        file.write(f"Average Calorie per meal:{avg_cal_per_meal}\n")
        file.write(f"Status:{status}\n")
        print(f"\nSession file saved successfully in {filename}")             #printing status

else:
    print("Report not saved.")                                                





    
