from tqdm import tqdm
import os


dirs = os.listdir("labeladSmall")
# print(dirs)



for di in tqdm(dirs):
    files = os.listdir(di)
    # print(files)
    for file in files:
        if "0" in file or "1" in file or "2" in file or "3" in file or "4" in file or "5" in file or "6" in file or "7" in file or "8" in file or "9" in file:
            if "A" in file or "B" in file:
                pass
            else:
                # print("{}/{}".format(di,file))
                os.remove("{}/{}".format(di,file))