import os
import os.path
import pandas as pd
import openpyxl 

gtwFilePath = "C:\\Users\\Ivar\\Desktop\\gtw1"
destinationPath =  "C:\\Users\\Ivar\\Desktop\\gtwXY\\"
db = "C:\\Users\\Ivar\\Desktop\\RCBU_20211206_DB_.csv"

gtwRAW = pd.DataFrame()
gtwOMS = pd.DataFrame()
for root, subdirs, files in os.walk(gtwFilePath):
    for d in subdirs:
        for file in os.listdir(gtwFilePath +"\\"+d):        
            df = pd.read_csv(gtwFilePath +"\\"+d+"\\"+file,sep=",", dtype={"METER_ADDRESS": str})           
            df = df.drop(df.columns[[1,2]], axis=1)
            df = df.replace('-','', regex=True)
            gtwRAW = df.drop_duplicates()
            if "GTW_OMS" in str(file):
                df1 = gtwRAW
                df2 = '101' + gtwRAW.astype(str)
                frames = [df1, df2] 
                gtwOMS=pd.concat(frames)
            #print(result)
        frames2 = [gtwRAW, gtwOMS]
        result = pd.concat(frames2)
        filename = os.listdir(gtwFilePath +"\\"+ d)
        gtwName = filename[0].split("_")
        result = result.drop_duplicates()

        rcbu = pd.read_csv(db,sep=",", dtype={"METER_ADDRESS": str, "ACCOUNT_ID": str, "HCN": str, "X": str, "Y": str}).drop(columns = ['ACCOUNT_ID', 'HCN'])
        result = pd.merge(result,rcbu,on='METER_ADDRESS',how='left')
        #result = result.drop_duplicates()
        result = result.dropna(subset = ["X"])
        result.to_csv(destinationPath+"GTW_XY_"+gtwName[3]+"_"+gtwName[5], index=False)  

print("Done")         




