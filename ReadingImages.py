import rasterio
from rasterio.plot import show

indata = '/content/drive/MyDrive/Test_Nove/Boston/0/0_Boston_class0.jpg'

# Note that eample uses 4 band NAIP imagery
with rasterio.open(indata) as src:
    arr = src.read([1,2,3], masked=True)
    show(arr)
