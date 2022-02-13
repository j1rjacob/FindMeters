import os
import os.path
import pandas as pd
import openpyxl 

class GetCoordinates:

    def __init__(self, folderPath, filePath) -> None:
        self.folderPath = folderPath
        self.filePath = filePath
    
    def get_result(self):
        try:
            gtwPath =  os.path.join("C:\\"+os.environ["HOMEPATH"], "Desktop")+"\\gtwXY\\"
            resultGtwPath = os.path.isdir(gtwPath)
            if not resultGtwPath:
                path = os.path.join("C:\\"+os.environ["HOMEPATH"], "Desktop")
                os.chdir(path)
                folderName = "gtwXY"
                os.makedirs(folderName)

            destinationPath =  os.path.join("C:\\"+os.environ["HOMEPATH"], "Desktop")+"\\gtwXY\\"
            gtwRAW = pd.DataFrame()
            gtwOMS = pd.DataFrame()
            for root, subdirs, files in os.walk(self.folderPath):
                for d in subdirs:
                    for file in os.listdir(self.folderPath +"\\"+d):        
                        df = pd.read_csv(self.folderPath +"\\"+d+"\\"+file,sep=",", dtype={"METER_ADDRESS": str})           
                        df = df.drop(df.columns[[1,2]], axis=1)
                        df = df.replace('-','', regex=True)
                        gtwRAW = df.drop_duplicates()
                        if "GTW_OMS" in str(file):
                            df1 = gtwRAW
                            df2 = '101' + gtwRAW.astype(str)
                            frames = [df1, df2] 
                            gtwOMS=pd.concat(frames)                                           
                    frames2 = [gtwRAW, gtwOMS]
                    result = pd.concat(frames2)
                    filename = os.listdir(self.folderPath +"\\"+ d)
                    gtwName = filename[0].split("_")
                    result = result.drop_duplicates()
                    rcbu = pd.read_csv(self.filePath,sep=",", dtype={"METER_ADDRESS": str, "ACCOUNT_ID": str, "HCN": str, "X": str, "Y": str}).drop(columns = ['ACCOUNT_ID', 'HCN'])
                    result = pd.merge(result,rcbu,on='METER_ADDRESS',how='left')                
                    result = result.dropna(subset = ["X"])
                    result.to_csv(destinationPath+"GTW_XY_"+gtwName[3]+"_"+gtwName[5], index=False)  
            return("Done.")
        except BaseException as err:
            return(f"Unexpected {err=}, {type(err)=}")
            #raise

        