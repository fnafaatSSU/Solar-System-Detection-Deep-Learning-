data["path"]= data["path"].astype(str) 
data["path"]= data["path"].str.replace("(", "") 
data["path"]= data["path"].str.replace(")", "") 
data["path"]= data["path"].str.replace(",", "") 
data
