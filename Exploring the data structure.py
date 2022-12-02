base_path = '/content/drive/MyDrive/Test_Nove/IDC_regular_ps50_idx5/'
Image_ids = listdir(base_path)
print(Image_ids)

#//////////////////////////////
class_0_total = 0
class_1_total = 0
from pprint import pprint
for image_id in Image_ids:
    class_0_files = listdir(base_path + image_id + '/0')
    class_1_files = listdir(base_path + image_id + '/1')

    class_0_total += len(class_0_files)
    class_1_total += len(class_1_files) 

total_images = class_0_total + class_1_total
    
print(f'Number of solar in Class 0: {class_0_total}')
print(f'Number of solar in Class 1: {class_1_total}')
print(f'Total number of solar: {total_images}')
#//////////////////////////////////////////////////
