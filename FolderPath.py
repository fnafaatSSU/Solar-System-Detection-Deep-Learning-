base_path = "/content/drive/MyDrive/mass/IDC_regular/"
folder = listdir(base_path)
len(folder)
#///////////////////////////////////////////////
total_images = 0
for n in range(len(folder)):
    patient_id = folder[n]
    for c in [0, 1]:
        patient_path = base_path + patient_id 
        class_path = patient_path + "/" + str(c) + "/"
        subfiles = listdir(class_path)
        total_images += len(subfiles)
total_images
///////////////////////////////////////////////////////
      
