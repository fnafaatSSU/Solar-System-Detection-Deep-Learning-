import os
collection = "/content/drive/MyDrive/Test_Nove/IDC_regular_ps50_idx5/Salem/0/"
image_name = os.listdir(collection)
print("Image names are :", image_name)
//////////////////////////////////////////////////////////////////////////////
import os
path = "/content/drive/MyDrive/Test_Nove/IDC_regular_ps50_idx5/Salem/0"

files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '_Salem_class0.jpg'])))
