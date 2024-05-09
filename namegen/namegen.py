import pubchempy as pcp 
import random as r
functionalGroups = ["alcohol", "amine", "amide", "carboxylic acid", "acid anhydride", "ether", "halide", "aldehyde", "ketone", "ester", "acid halide", "nitrile", "nitro", "isonitrile"]
def alkaneGen(no):
    if no == 1: 
        return "methane"; 
    elif no == 2: 
        return "ethane";
    elif no == 3: 
        return "propane";
    elif no == 4: 
        return "butane";
    elif no == 5: 
        return "pentane";
    elif no == 6: 
        return "hexane";
def locant(alkane):
    #carboxylic acids, amides, acid anhydrides, nitrile, acid halides, isonitrile dont have locants
    #alcohols, amines, ethers, halides, aldehydes, nitro can have any locant 
    #ketone has intermediate locant 
    if alkane == "methane": 
        return 1;
    elif alkane == "ethane":
        return r.randint(1,2);
    elif alkane == "propane": 
        return r.randint(1,3);
    elif alkane == "butane": 
        return r.randint(1,4);
    elif alkane == "pentane": 
        return r.randint(1,5);
    elif alkane == "hexane": 
        return r.randint(1,6);
    elif alkane == "heptane": 
        return r.randint(1,7);
    elif alkane == "octane": 
        return r.randint(1,8);
    elif alkane == "nonane": 
        return r.randint(1,9);
    elif alkane == "decane": 
        return r.randint(1,6);
def finalName(): 
    #general functional groups: alcohol, amine, amide, aldehyde, ketone, 
    clientGroup = functionalGroups[r.randint(0,len(functionalGroups)-1)]
    alkanGroup = alkaneGen(r.randint(1,6))
    if(clientGroup == 'alcohol'): 
        return alkanGroup.rstrip("e")+"-"+str(locant(alkanGroup))+"-"+"ol"; 
    elif(clientGroup == 'amine'):
        return alkanGroup.rstrip("e")+"-"+str(locant(alkanGroup))+"-"+"amine";
    elif(clientGroup == 'amide'): 
        return alkanGroup.rstrip("e")+"amide"; 
    elif(clientGroup == 'aldehyde'):
        return alkanGroup.rstrip("e")+"-"+str(locant(alkanGroup))+"-"+"al"; 
    elif(clientGroup == 'ketone'): 
        return alkanGroup.rstrip("e")+"one";
    #carboxylic acid derivatives
    if(clientGroup == 'carboxylic acid'): 
        return alkanGroup.rstrip("e")+"oic acid"; 
    elif(clientGroup == 'acid anhydride'):
        return alkanGroup.rstrip("e")+"oic anhydride";
    elif(clientGroup == 'ether'):
        return str(locant(alkanGroup))+"-"+alkanGroup.rstrip("ane")+"oxy "+ alkanGroup
    #halocompounds
    if(clientGroup == 'halide'): 
        halides = ['fluoro', 'bromo', 'chloro', 'iodo']
        return str(locant(alkanGroup))+"-"+halides[r.randint(0,3)]+alkanGroup;
    #ester
    if(clientGroup == 'ester'): 
        return str(locant(alkanGroup))+"-"+alkanGroup.rstrip("ane")+"yl "+ alkanGroup.rstrip("e")+"oate"
    #misc
    elif(clientGroup == 'nitro'):
        return str(locant(alkanGroup))+"-"+"nitro"+alkanGroup
    elif(clientGroup == 'acid halide'): 
        halides = ['fluoride', 'bromide', 'chloride', 'iodide']
        return alkanGroup.rstrip("e")+"oyl " + halides[r.randint(0,3)]
    elif(clientGroup == "nitrile"):
        return alkanGroup+"nitrile";
    elif(clientGroup == 'isonitrile'):
        return alkanGroup + " isonitrile";
