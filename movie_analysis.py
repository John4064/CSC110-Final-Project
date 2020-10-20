#john parkhurst
#3/28/19
#Display the information of the movie data
def getData():
    #filename = movie.txt
    isTrue = True
    while isTrue == True:
        try:
            name = input("Please enter file name: ")
            mFile = open(name,'r')
            isTrue = False
        except IOError:
            print("Please Try Again Invalid File Name.")
    mFile.readline()
    titleL = []
    genreL = []
    timeL = []
    ratingL =[]
    studioL = []
    yearL = []
    for line in mFile:
        line = line.strip()
        title,genre,time,rating,studio,year = line.split(',')
        titleL.append(title)
        genreL.append(genre)
        timeL.append(int(time))
        ratingL.append(rating)
        studioL.append(studio)
        yearL.append(int(year))
    mFile.close()
    return genreL,titleL,timeL,ratingL,studioL,yearL
    
def mainScreen():
    correct = True
    while correct == True:
        print("Please choose one of the following options")
        print("1 -- Find all films of a certain genre")
        print("2 -- Find all films with a certain rating")
        print("3 -- Find the longest film made by a specific studio")
        print("4 -- Search for a film by title")
        print("5 -- Find average runtime of films made in a give year range")
        print("6 -- Sort all lists by runtime and write the results to a new file")
        print("7 -- Which studio produced the most films?")#extra credit
        print("8 -- Quit")
    #create an if statement with module to verify it is infact a integer
        choice = input("Choice ==> ")
        choice = float(choice)
        if choice % 1.0 == 0.0:#checks to make sure its a valid number =D
            correct == False
            return int(choice)
        else:
            print("Please enter a proper input!")
    return

#all movies by genre
def specGenre(specific,genreL,titleL,timeL,ratingL,studioL,yearL):
    temp = []
    for x in range(len(genreL)):
        if specific == genreL[x]:
            temp.append(x)
    print("These are movies that fit your criteria")
    if len(temp)>0:
        print("TITLE".ljust(40),"GENRE".ljust(14),"TIME".ljust(8), "RATING".ljust(8), "STUDIO".ljust(25), "YEAR".ljust(8))
        for g in range(len(temp)):
            print(titleL[(temp[g])].ljust(40),genreL[(temp[g])].ljust(14),str(timeL[(temp[g])]).ljust(8),ratingL[(temp[g])].ljust(8),studioL[(temp[g])].ljust(25),str(yearL[(temp[g])]).ljust(8))
    else:
        print("")
        print("No titles were found at this rating, Please check spelling.")
        print("")
    return

def specRating(rating,genreL,titleL,timeL,ratingL,studioL,yearL):
    temp = []
    for r in range(len(genreL)):
        if rating == ratingL[r]:
            temp.append(r)
    print("These are movies that fit your criteria")
    if len(temp)>0:
        print("TITLE".ljust(40),"GENRE".ljust(14),"TIME".ljust(8), "RATING".ljust(8), "STUDIO".ljust(25), "YEAR".ljust(8))
        for g in range(len(temp)):
            print(titleL[(temp[g])].ljust(40),genreL[(temp[g])].ljust(14),str(timeL[(temp[g])]).ljust(8),ratingL[(temp[g])].ljust(8),studioL[(temp[g])].ljust(25),str(yearL[(temp[g])]).ljust(8))
    else:
        print("")
        print("No titles were found at this rating, Please check spelling.")
        print("")
    return
#search for longest movie by studio and length
def specStudio(studio,genreL,titleL,timeL,ratingL,studioL,yearL):
    temp = []
    for t in range(len(genreL)):
        if studio == studioL[t]:
            temp.append(t)
    long = 0
    ind = 0
    for x in range(len(temp)):
        if timeL[temp[x]]> long:
            long = timeL[temp[x]]
            ind = x
    print("These are movies that fit your criteria")
    if(len(temp)>0):
        print("TITLE".ljust(40),"GENRE".ljust(14),"TIME".ljust(8), "RATING".ljust(8), "STUDIO".ljust(25), "YEAR".ljust(8))
        print(titleL[(temp[ind])].ljust(40),genreL[(temp[ind])].ljust(14),str(timeL[(temp[ind])]).ljust(8),ratingL[(temp[ind])].ljust(8),studioL[(temp[ind])].ljust(25),str(yearL[(temp[ind])]).ljust(8))
    else:
        print("")
        print("No titles were found by this studio, Please check spelling.")
        print("")
    return

#simple search for movie by title
def specMovie(title,genreL,titleL,timeL,ratingL,studioL,yearL):
    temp = []
    for d in range(len(genreL)):
        if title == titleL[d]:
            temp.append(d)
    print("These are movies that fit your criteria")
    if len(temp)>0:
        print("TITLE".ljust(40),"GENRE".ljust(14),"TIME".ljust(8), "RATING".ljust(8), "STUDIO".ljust(25), "YEAR".ljust(8))
        for g in range(len(temp)):
            print(titleL[(temp[g])].ljust(40),genreL[(temp[g])].ljust(14),str(timeL[(temp[g])]).ljust(8),ratingL[(temp[g])].ljust(8),studioL[(temp[g])].ljust(25),str(yearL[(temp[g])]).ljust(8))
    else:
        print("")
        print("No titles were found, Please check spelling.")
        print("")
    return

#checks the average length of movies by specified year range
def specYears(year1,year2,genreL,titleL,timeL,ratingL,studioL,yearL):
    temp = []
    year1 = int(year1)
    year2 = int(year2)
    #compare and set
    for g in range(len(genreL)):
        if(year1<=yearL[g])&(year2>=yearL[g]):
            temp.append(g)
    sum = 0
    #calculate the averages
    for x in range(len(temp)):
        sum = timeL[temp[x]]+sum
    sum = sum/len(temp)
    print("These are movies that fit your criteria")
    if len(temp)>0:
        
        print("TITLE".ljust(40),"GENRE".ljust(14),"TIME".ljust(8), "RATING".ljust(8), "STUDIO".ljust(25), "YEAR".ljust(8))
        for g in range(len(temp)):#This is here to print all the movies made in the range
            print(titleL[(temp[g])].ljust(40),genreL[(temp[g])].ljust(14),str(timeL[(temp[g])]).ljust(8),ratingL[(temp[g])].ljust(8),studioL[(temp[g])].ljust(25),str(yearL[(temp[g])]).ljust(8))
        print("The average runtime for films made between ",year1," and ",year2," is ",round(sum,1))
    else:
        print("")
        print("No titles were found in this range, Please check the years entered!")
        print("")
    return

def sortData(genreL,titleL,timeL,ratingL,studioL,yearL,name):
    sortF = open(name,'w')
    temp = []
    for i in range(len(timeL)):
        min = i
        for d in range(i+1,len(timeL)):
            if timeL[d]<timeL[min]:
                min = d
        #setting the order
        genreL[i], genreL[min] = genreL[min], genreL[i]
        titleL[i], titleL[min] = titleL[min], titleL[i]        
        timeL[i], timeL[min] = timeL[min], timeL[i] 
        ratingL[i], ratingL[min] = ratingL[min], ratingL[i] 
        studioL[i], studioL[min] = studioL[min], studioL[i]
        yearL[i], yearL[min] = yearL[min], yearL[i]
    #printing out the output
    for g in range(len(titleL)):
        sortF.write(titleL[(g)].ljust(40))
        sortF.write(genreL[(g)].ljust(14))
        sortF.write(str(timeL[(g)]).ljust(8))
        sortF.write(ratingL[(g)].ljust(8))
        sortF.write(studioL[(g)].ljust(25))
        sortF.write(str(yearL[(g)]).ljust(8))
        sortF.write("\n")
    sortF.close()
    return
#extra credit: gets the most movies by studio
def mostFilms(studiosL):
    temp = ''
    count=0
    high = 0
    oneStudio = []
    #removing multiple versions and making a copy
    for x in range(len(studiosL)):
        if studiosL[x] not in oneStudio:
            oneStudio.append(studiosL[x])
    #need two for loops one to account for one time one for amount of
    for v in range(len(oneStudio)):
        count = 0
        for g in range(len(studiosL)): 
            if oneStudio[v] == studiosL[g]:
                count = count+1
                if count>= high:
                    high = count
                    temp = oneStudio[v]
    print("The studio with the most films produced is ", temp," they produced ",high," films.")
    return
#main function where everything is called
# modify to change the choice to a seperate function
def main():
    #name = input("Enter name of file")
    genreL,titleL,timeL,ratingL,studioL,yearL = getData()
    #specGenre('Mystery',genreL)
    choice = 0
    while choice != 8:
        if(choice >8 & choice <0):
            #this is just to make sure a correct value is given between 8 and 0
            print("Incorrect choice please try again!")
            #will round if given decimal between 0 and 8
            choice = int(mainScreen())
        else:
            choice = int(mainScreen())
            if(choice == 1):
                inp = input("Enter name of Genre: ")
                specGenre(inp,genreL,titleL,timeL,ratingL,studioL,yearL)
            elif(choice == 2):
                inp = input("Enter the Rating: ")
                specRating(inp,genreL,titleL,timeL,ratingL,studioL,yearL)
            elif(choice ==3):
                inp = input("Find the longest film made by a specific studio: ")
                specStudio(inp,genreL,titleL,timeL,ratingL,studioL,yearL)
            elif(choice ==4):
                inp = input("Search for a film by a title: ")
                specMovie(inp,genreL,titleL,timeL,ratingL,studioL,yearL)
            elif(choice ==5):
                print("Enter year range to search earlier year first!")
                isTrue =True
                while isTrue == True:
                    year1 = input("Year1: ")
                    year2 = input("Year2: ")
                    if year1<year2:
                        specYears(year1,year2,genreL,titleL,timeL,ratingL,studioL,yearL)
                        isTrue = False
                    else:
                        print("Please make sure the second year comes second and that you entered proper years!")
            elif(choice == 6):
                name = input("Please enter a file name, make sure to include extension!  ")
                sortData(genreL,titleL,timeL,ratingL,studioL,yearL,name)
                print("Done on file ",name )
            elif(choice == 7):
                mostFilms(studioL)
            elif(choice == 8):
                print("Have a nice day!")
            else:
                print("Incorrect choice try again")
    return
