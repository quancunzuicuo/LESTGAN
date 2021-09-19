# LESTGAN
## Preparation

- **pre-trained model**
    - download the LESTGAN model from [Google Drive](https://drive.google.com/file/d/1-U-Rb4hIG1mTsUbtVKPPH9oVBxgsPp21/view?usp=sharing), and unzip the files to ***DATAROOT/pretrained_model/***

- **Dataset**
    - [CelebA](http://openaccess.thecvf.com/content_iccv_2015/papers/Liu_Deep_Learning_Face_ICCV_2015_paper.pdf) dataset
        - [Images](https://drive.google.com/open?id=0B7EVK8r0v71pZjFTYXZWM3FlRnM) should be placed in ***DATAROOT/data/img_align_celeba/\*.jpg***
        - [Attribute labels](https://drive.google.com/open?id=0B7EVK8r0v71pblRyaVFSWGxPY0U) should be placed in ***DATAROOT/data/list_attr_celeba.txt***
        - You can download the data from [Google Drive](https://drive.google.com/file/d/1vBCgfJfeMRWp-6qS-gwlLKNqg-GVswar/view?usp=sharing)
    - We follow the settings of STGAN, kindly refer to [STGAN](https://github.com/csmliu/STGAN) for more dataset preparation details


- **Prerequisites**
    - Tensorflow (r1.4 - r1.12 should work fine)
    - Python 3.x with matplotlib, numpy and scipy


### Testing

- Example of testing ***single*** attribute

    ```console
    python test.py --experiment_name 128 --dataroot data
    ```

- Example of testing ***multiple*** attributes

    ```console
    python test.py --experiment_name 128 --test_atts Pale_Skin Male --dataroot data
    ```
    
- To test PSNR score and SSIM score

    ```console 
    python test.py --experiment_name 128 --dataroot data
    ```
        
    ```console 
    python test_psnr_ssim.py
    ```
    
- To test the attribute generation accuracy of the model

    - download the classifier from [Google Drive](https://drive.google.com/file/d/1ARuyjm0vH7LP_4RIOY96TjU5tX1lbxe6/view?usp=sharing), and unzip the files to ***DATAROOT/***

    ```console 
    python test.py --experiment_name 128 --test_int 2 --dataroot data
    ```
    
    ```console 
    cd att_classification
    ```
    
    ```console 
    python test.py --img_dir ../output/128/sample_testing
    ```

- You can specify which image(s) to test by adding `--img num` (e.g., `--img 182638`, `--img 200000 200001 200002`), where the number should be no larger than 202599 and is suggested to be no smaller than 182638 as our test set starts at 182638.png.


- Our training code has not been cleaned up yet, we will upload it as soon as it is cleaned up


## Acknowledgement
The code is heavily borrowed from [STGAN](https://github.com/csmliu/STGAN), thanks for their excellent work!
