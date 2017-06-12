'''
Created on 2017429

@author: dell
'''

from PIL import Image
import os.path
import re
import glob


def convertjpg(jpgfile,outdir,width=92,height=112):
    img=Image.open(jpgfile)   
    new_img=img.resize((width,height),Image.BILINEAR)
    img.close()
    filename = re.sub(r'([\d]+)','',jpgfile)
    fn = filename.split(".")
    fq = fn[-2][:-1].split("\\")[-1]
    fg = fq.split("_")
    c = 0
    if fg[1] == "是" and fg[3] == "是" and fg[5] == "是":
        c = 7
    elif fg[1] == "是" and fg[3] == "是":
        c = 6
    elif fg[3] == "是" and fg[5] == "是":
        c = 5
    elif fg[1] == "是" and fg[5] == "是":    
        c = 4
    elif fg[3] == "是":
        c = 3
    elif fg[1] == "是":
        c = 2
    elif fg[5] == "是":
        c = 1
    
    print(fn)
    idx[c] += 1

    new_img.save(os.path.join(outdir + str(c) + "/",os.path.basename(str(idx[c]) + "." + fn[-1])))
    #new_img.save(os.path.join(outdir,os.path.basename("男_否_无_否_无_否_无_" + str(i) + ".jpeg")))

idx = [0 for i in range(8)]
for jpgfile in glob.glob("D:/我的/比赛/自己的数据/标签图片/*.jpeg"):    
    convertjpg(jpgfile,"D:/我的/比赛/自己的数据/方案1/")
    
#[-2][:-1]+ "." + fn[-1]