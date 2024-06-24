print("script by prasz19")

fileinput = input("input your file here:",   )

fileoutput = "stationfix.dat"

file = open(fileinput,"r")
row = file.readlines()
for i in range(len(row)):
    row[i] = row[i].split()
file.close()
file = open(fileoutput, "w")

# recording each line into the output file
i = 0

# recording each stations into the output file
while i < len(row):
        
    # recording the stations
    if len(row[i])>0 and row[i][0]=="sta":
        try:
            j=1
            while j <= 1:
                i +=1
                try:
                    idsta = row[i][0]
                    
                    # recording idsta into the file
                    file.write(idsta.rjust(5)+"\n")

                except:
                    break
        except:
            break
    i += 1
print("Check your result")
file.close()

# Opening station filter result file from list_detail20
input_sta = input("Please input your station list:",    )
list_sta = open(input_sta, "r+")

# Filtering the same words in the list data
list_sta = list(dict.fromkeys(list_sta))

# opening and creating output file
with open("filtered_sta.dat", "w+") as f:
    
    # recording each element in the list
    for items in list_sta:
        f.write("%s" %items)
 
print("Your file has been filtered")
        
# close file
f.close()
