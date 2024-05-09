import random as r
from namegen import finalName
functionalGroups = [ "carboxylic acid","sulfonic acid","ester","acid halide","amide","nitrile","aldehyde","ketone","alcohol", "amine",  "acid anhydride", "ether", "halide", "nitro", "isonitrile", "alkene", "alkyne", "methyl", "ethyl"]
secondaryNames = ['carboxy', 'sulpho','oxycarbonyl','halocarbonyl', 'carbamoyl', 'cyano', 'formyl', 'oxo', 'hydroxy','amino', 'acid anhydride', 'ether', 'halide', 'nitro', 'isocyano', 'alkene', 'alkyne', 'methyl', 'ethyl' ]
#utility functions 
def alkaneGen(no):
    if no == 1: 
        return "ethan"; 
    elif no == 2: 
        return "ethan";
    elif no == 3: 
        return "propan";
    elif no == 4: 
        return "butan";
    elif no == 5: 
        return "pentan";
    elif no == 6: 
        return "hexan";

def noconvertor(name):
    if name == "ethan":
        return 2;
    elif name == "propan":
        return 2;
    elif name == "butan": 
        return 3; 
    elif name == "pentan":
        return 4; 
    elif name == "hexan":
        return 5; 

def locant(alkane):
    #carboxylic acids, amides, acid anhydrides, nitrile, acid halides, isonitrile dont have locants
    #alcohols, amines, ethers, halides, aldehydes, nitro can have any locant 
    #ketone has intermediate locant 
    if alkane == "methan": 
        return '1';
    elif alkane == "ethan":
        return '1';
    elif alkane == "propan": 
        return str(r.randint(1,2));
    elif alkane == "butan": 
        return str(r.randint(1,2));
    elif alkane == "pentan": 
        return str(r.randint(1,3));
    elif alkane == "hexan": 
        return str(r.randint(1,3));
def secondaryLocant(alkane):
    if alkane =="methan":
        return '1';
    elif alkane == "ethan":
        return '2';
    elif alkane == "propan":
        return '3';
    elif alkane == "butan":
        return str(r.randint(3,4));
    elif alkane == "pentan":
        return str(r.randint(3,5));
    elif alkane == "hexan":
        return str(r.randint(3,6))    

#main nomenclature generator 
def nomenProcessing():
    nomen = ''
    primaryIndex = r.randint(0,len(functionalGroups)-1);
    secondaryIndex = r.randint(primaryIndex,len(functionalGroups)-1);
    primaryClientGroup = functionalGroups[primaryIndex]
    secondaryClientGroup = secondaryNames[secondaryIndex]
    alkanGroup = alkaneGen(r.randint(1,6))
    if primaryIndex < secondaryIndex: 
        #primary processing
         # generates a new alkane 
        #processing all functional groups 
        if primaryClientGroup == 'carboxylic acid': 
            nomen += alkanGroup + "oic acid"
        elif primaryClientGroup == 'sulfonic acid':
            nomen += alkanGroup+"e" + 'sulfonic acid'
        elif primaryClientGroup == 'ester': 
            nomen += locant(alkanGroup) + "-" + alkaneGen(r.randint(1,6)).rstrip('an') + "yl " + alkanGroup + "oate"
        elif primaryClientGroup == 'acid halide':
            halides = ['fluoride', 'chloride', 'bromide', 'iodide']
            nomen += alkanGroup + "oyl " + halides[r.randint(0,3)]
        elif primaryClientGroup == 'amide': 
            nomen += alkanGroup + "amide"
        elif primaryClientGroup == 'nitrile':
            nomen += alkanGroup + "e-" + locant(alkanGroup) + "-" + "nitrile"
        elif primaryClientGroup == 'aldehyde':
            nomen += alkanGroup + "-" + locant(alkanGroup) + '-al'
        elif primaryClientGroup == 'ketone':
            nomen += alkanGroup + "-" + locant(alkanGroup) + '-one'
        elif primaryClientGroup == 'alcohol': 
            nomen += alkanGroup + "-" + locant(alkanGroup) + "-ol"
        elif primaryClientGroup == 'amine': 
            nomen += alkanGroup + "-" + locant(alkanGroup) + "amine"
        elif primaryClientGroup == 'acid anhydride': 
            nomen += alkaneGen(r.randint(1,6)) + "oic " + alkanGroup + "oic anhydride"
        elif primaryClientGroup == 'ether': 
            nomen += locant(alkanGroup) + "-" + alkaneGen(r.randint(1,6)).rstrip("an") + "yl " + alkanGroup + "e" 
        elif primaryClientGroup == 'halide': 
            halides = ['fluoro', 'chloro', 'bromo', 'iodo']
            nomen += locant(alkanGroup) + "-" + halides[r.randint(0,3)] + alkanGroup + "e"
        elif primaryClientGroup == 'nitro': 
            nomen += locant(alkanGroup) + "-" + alkanGroup + "e"
        elif primaryClientGroup == 'isonitrile': 
            nomen += alkanGroup + "-" + locant(alkanGroup) + "-" + "isonitrile"
        elif primaryClientGroup == "alkene": 
            nomen += alkanGroup.rstrip("an") + "-" + locant(alkanGroup) + "-" + "ene"
        elif primaryClientGroup == 'alkyne':
            nomen += alkanGroup + '-' + locant(alkanGroup) + '-' + 'yne'
        elif primaryClientGroup == 'methyl': 
            nomen += locant(alkanGroup) + "-methyl" + alkanGroup + "e"
        elif primaryClientGroup == 'ethyl': 
            nomen += locant(alkanGroup) + "-ethyl" + alkanGroup + "e"
        #secondary substituent processing
        #specific cases
        if secondaryClientGroup == "oxycarbonyl": 
            nomen = secondaryLocant(alkanGroup) + "-" + alkaneGen(r.randint(1,6)).rstrip("an") + "oxycarbonyl" + nomen
        elif secondaryClientGroup == 'halocarbonyl':
            halides = ['fluoro', 'chloro', 'iodo', 'bromo'] 
            nomen = secondaryLocant(alkanGroup) + "-" + halides[r.randint(0,3)] + "carbonyl" + nomen
        elif secondaryClientGroup == 'acid anhydride':
             #idk wtf the nomenclature is 
             y=1
        elif secondaryClientGroup == 'ether': 
                y=1
        elif secondaryClientGroup == 'alkyne': 
            y=1
        elif secondaryClientGroup == 'alkene': 
            y=1
        elif secondaryClientGroup == 'halide': 
            halides = ['fluoro', 'chloro', 'iodo', 'bromo']
            nomen = secondaryLocant(alkanGroup) + "-" + halides[r.randint(0,3)] + nomen
        else: #general case 
            nomen = secondaryLocant(alkanGroup)+ "-" + secondaryNames[secondaryIndex]  + nomen
    if primaryIndex == secondaryIndex:
        diGroup = alkaneGen(r.randint(1,6))
        if(primaryClientGroup == 'carboxylic acid'): 
            nomen = diGroup + "e" + " dioic acid"
        elif(primaryClientGroup == 'sulfonic acid'):
           nomen = diGroup+ "e" + " disulfonic acid"
        elif(primaryClientGroup == 'acid halide'): 
            halides = ['fluoride', 'bromide', 'chloride', 'iodide']
            nomen = diGroup+ "e" + "dioyl " + halides[r.randint(0,3)]
        elif(primaryClientGroup == 'amide'): 
            nomen = diGroup+ "e" + "diamide";
        elif(primaryClientGroup == "nitrile"):
            nomen = diGroup+ "e" + "dinitrile";
        elif(primaryClientGroup == 'isonitrile'):
            nomen = diGroup+ "e" + "diisonitrile";
        elif(primaryClientGroup == 'aldehyde'):
            nomen = diGroup+ "e" + "dial";
        elif(primaryClientGroup == 'ketone' and noconvertor(alkanGroup) > 3): 
            nomen = diGroup+ "e" + "dione";
        elif(primaryClientGroup == 'alcohol'): 
            nomen = diGroup+ "e" + "diol";
        elif(primaryClientGroup == 'amine'):
            nomen = diGroup+ "e" + "diamine";
        elif(primaryClientGroup == 'acid anhydride'):
            nomen = str(secondaryLocant(diGroup)) + "-" + secondaryNames[secondaryIndex] + diGroup.rstrip("e")+"oic anhydride";
        elif(primaryClientGroup == 'ether'):
            nomen = str(secondaryLocant(diGroup)) + "-" + secondaryNames[secondaryIndex] + str(locant(diGroup))+"-"+diGroup.rstrip("ane")+"oxy "+ diGroup + "e"
        elif(primaryClientGroup == 'halide'): 
            halides = ['fluoro', 'bromo', 'chloro', 'iodo']
            nomen = "di" + halides[r.randint(0,3)] + diGroup + "e";
        elif(primaryClientGroup == 'nitro'):
            nomen = "dinitro" + diGroup + "e";
    return nomen

file = open("conversions.txt", "w")
print("How many conversions do you want?")
i = (int) (input())
place = 0 
while(place <= i): 
    firstOne = nomenProcessing();
    no = r.randint(1,100)
    secondparam = r.randint(1,100)
    thirdparam = r.randint(1,100)
    secondOne = nomenProcessing()
    if(no < 20):
        compounds = ['benzene diazonium chloride','aniline', 'benzene carbaldehyde', 'benzamide', 'carbolic acid','picric acid', 'benzoic acid', 'benzene sulfonic acid','nitrobenzene','chlorobenzene', 'fluorobenzene','iodobenzene', 'bromobenzene','salicylic acid','salicylaldehyde','acetophenone','TEL', 'phenolphthalein', 'benzoin', 'furoin', 'azo dye']
        secondOne = compounds[r.randint(0,len(compounds)-1)]
    if(secondparam < 50):
        firstOne = finalName();
    if(thirdparam < 50):
        secondOne = finalName()
    if(firstOne != "" and secondOne != "" and secondOne != " "):
        string = firstOne + " to " + secondOne
        a = file.write(string + "\n")
        place = place+1
   
file.close()
print("Completed!")