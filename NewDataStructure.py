import pandas as pd
columns = ["Image_id","target","path"]
data_rows = []
i = 0
iss = 0
isss = 0

# note that we loop through the classes after looping through the 
# patient ids so that we avoid splitting our data into [all class 0 then all class 1]
for Image_id in Image_ids:
    for c in [0,1]:
        class_path = base_path + Image_id + '/' + str(c) + '/'
        imgs = listdir(class_path)
        
        # Extracting Image Paths
        img_paths = [class_path + img + '/' for img in imgs]
        
        # Extracting Image Coordinates
        img_coords = [img.split('_',2)[2:2] for img in imgs]
       # x_coords = [int(coords[0][1:]) for coords in img_coords]
        #y_coords = [int(coords[1][1:]) for coords in img_coords]

        for path in zip(img_paths):
            values = [Image_id,c,path]
            data_rows.append({k:v for (k,v) in zip(columns,values)})
# We create a new dataframe using the list of dicts that we generated above
data = pd.DataFrame(data_rows)
print(data.shape)
data.head(10)
///////////////////////////////////////////////////////////////////////////////////////////
