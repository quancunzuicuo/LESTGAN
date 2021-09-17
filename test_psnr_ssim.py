import os
import os.path as path
from PIL import Image
import numpy as np
import math
from skimage.measure import compare_psnr as psnr
from skimage.measure import compare_ssim as ssim

root = './output/128/sample_testing'

sum_psnr = []
sum_ssim = []
cnt = 0
for im in os.listdir(root):
    if cnt % 1000 == 0:
        print(cnt)
    img = Image.open(path.join(root, im))
    src = np.array(img.crop((0, 0, 128, 128)))
    dst = np.array(img.crop((140, 0, 268, 128)))
    sum_psnr.append(psnr(src, dst))
    sum_ssim.append(ssim(src, dst, multichannel=True))
    cnt += 1
print(sum(sum_psnr) / float(cnt))
print(sum(sum_ssim) / float(cnt))
with open('psnr.txt', 'w') as f:
    f.write('%f\n%f\n'%(sum(sum_psnr) / float(cnt), sum(sum_ssim) / float(cnt)))
    f.write('\n'.join(['%f %f'%(sum_psnr[i], sum_ssim[i]) for i in range(cnt)]))
    f.close()