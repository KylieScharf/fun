from flask import Flask, render_template, request, redirect # if the post info checks out in the login we redirect to the URL for anotherr page
import requests
import random
import math
from random import seed
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # the app.route decorates the function so it says when this route is used go through this function
def index():
    num = random.random() * 1000000
    num2 = str(math.floor(num))
    print(type(num2))
    print(num2)
    return render_template("index.html", random=num2)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    return render_template("calculator.html")

@app.route('/probability', methods=['GET', 'POST'])
def probability():
    return render_template("probability.html")

@app.route('/love', methods=['GET', 'POST'])
def love():
    if request.form:
        user_name = request.form.get("userName2")
        partner_name = request.form.get("partnerName2")
        user_name_count = name_check(user_name)
        partner_name_count = name_check(partner_name)
        count = var("l", "o", "v", "e", "s", user_name_count, partner_name_count) # call the variable function that creates the variables l, o, v, e, and s anad stores the values of the previous 2 for user and partner added in each and returns a list of those totals
        #count = ""
        #for item in range(len(list)): # for every item in the list turn it into a string and add it to a string
            #count += str(list[item])
        count2 = []
        index = []
        index2 = 0
        new_index = []
        while len(count) > 2:
            print("original")
            for i in range(len(count) - 1):
                num = int(count[i]) + int(count[i+1])
                count[i] = num
                if i == len(count)-2:
                    #count = substring(count, 0, len(count)-1)
                    count.pop()
            print(count)
            for i in range(len(count)):
                if count[i] >= 10: #if the number is over 10 add it to a list that has all numbers over 10 and add the index to another list so you can add then new numbers back at the right index
                    count2.append(count[i])
                    index.append(int(i))
            length = len(count2)
            for i in range(len(count2)):
                print("tens")
                print(count2)
                print(index2)
                if count2[i] % 10 == 0: # if it is a mulitple of 10 like 10, 20, 30 etc.
                    tens = count2[i] / 10
                    ones = 0
                else:
                    ones = count2[i] % 10
                    tens = (count2[i] % 100) // 10
                if length > 1:
                    index2 = index[i]*2 # this is the starting index where the number is added
                else:
                    index2 = index[i]
                print("check")
                print(index2)
                print(count2)
                print(count)
                count[index2] = tens
                print("check2")
                count.insert(index2 + 1, ones) # this is the next index where the ones place is added
                print("check3")

            print("after")
            print(count)
            count2 = [] #reseting the count list after the numbers are taken care of
        count = "" + str(count[0]) + str(count[1])
        message = "The love percentage between " + user_name + " and " + partner_name + " is " + count + "%"
        return render_template("love.html", message=message)
    return render_template("love.html", message="Type the names of two people in the input fields on this page to see their love percentage pop up in an alert like the one you are seeing now!")

def name_check(name):
    l = 0
    o = 0
    v = 0
    e = 0
    s = 0
    for i in range(len(name)):
        if name[i] == "l" or name[i] == "L":
            l += 1
        if name[i] == "o":
            o += 1
        if name[i] == "v":
            v += 1
        if name[i] == "e":
            e += 1
        if name[i] == "s":
            s += 1
    list = [l, o, v, e, s]
    return list

def var(var1, var2, var3, var4, var5, user, partner):
    list = [var1, var2, var3, var4, var5]
    for i in range(len(list)):
        list[i] = user[i] + partner[i]
    return list


if __name__ == "__main__":
    app.run(debug=True)