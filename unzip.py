import zipfile
DATA_IN_PATH ='/content/gdrive/My Drive/Colab Notebooks/competition data/frenz_s2/'
file_list = ['train.zip', 'test.zip']

for file in file_list:
  zipRef = zipfile.ZipFile(DATA_IN_PATH + file, 'r')
  zipRef.extractall(DATA_IN_PATH + file)
  zipRef.close()
