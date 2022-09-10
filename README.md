# Low-Light Enhancement in Images

This Project has been created to adjust lightening like Natural Image Quality. I have used [GLADNet](https://ieeexplore.ieee.org/document/8373911) for bringing lightning like real images.GLADNet(GLobal illumination Aware and Detail-preserving Network), first calculate a global illumination estimation for the low-light input, then adjust the illumination under the guidance of the estimation and supplement the details using a concatenation with the original input. 

Low light imaging and low light image enhancement have wild applications in our daily life and different scientific research fields:

* Night Surveillance
* Automated Driving
* Fluorescence Microscopy
* High Speed Imaging and so on..
<br>
However, there is still a long way to go in dealing with these tasks, considering the great challenges in low photon counts, low SNR, complicated noise models, etc. 

This is a Tensorflow implantation of GLADNet

GLADNet: Low-Light Enhancement Network with Global 
[Paper](http://www.icst.pku.edu.cn/F/course/icb/Pub%20Files/2018/wwj_fg2018.pdf)

![Teaser Image](https://github.com/daooshee/fgworkshop18Gladnet/blob/master/images/fg-1478.jpg)

## Requirements ##
1. Python == 2.7
2. Tensorflow == 1.3.0
3. numpy, PIL

## Run the app locally

https://user-images.githubusercontent.com/54981696/189492666-b0faa652-bea1-4b3e-9d50-fdaedb86b520.mp4

Open a terminal and start by cloning the project repository

```bash
  https://github.com/Prasantkumar987/Low-Light_Enhancement.git
```

Go to the project directory

```bash
  cd Low-Light_Enhancement
```

To Create Virtual Environment
```
  pip install virtualenv
  virtualenv --python=python2.7 gladnetEnv 
```

Activate Environment in Linux
```
  source gladnetEnv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server (Linux / MacOS)

```bash
  streamlit run app.py
```

If the browser window does not open automatically when the ```streamlit run``` command is executed, you can manually navigate to ```localhost:8501```
To terminate the application, go back to the terminal and shutdown the server by pressing ```CTRL + C```.

## Testing  Usage ##
To quickly test your own images with our model, you can just run through
```shell
python main.py 
    --use_gpu=1 \                           # use gpu or not
    --gpu_idx=0 \
    --gpu_mem=0.5 \                         # gpu memory usage
    --phase=test \                          # testing phase
    --test_dir=/path/to/your/test/dir/ \    # input img dir for testing
    --save_dir=/path/to/save/results/ \     # output img dir to save outputs
```
## Training Usage ##
First, download training data set from [our project page](https://daooshee.github.io/fgworkshop18Gladnet/). Save training pairs of our LOL dataset under `./data/train/low/`, and synthetic pairs under `./data/train/normal/`.
Then, start training by 
```shell
python main.py
    --use_gpu=1 \                           # use gpu or not
    --gpu_idx=0 \
    --gpu_mem=0.8 \                         # gpu memory usage
    --phase=train \                         #
    --epoch=50 \                            # number of training epoches
    --batch_size=8 \
    --patch_size=384 \                      # size of training patches
    --base_lr=0.001 \                       # initial learning rate for adm
    --eval_every_epoch=10 \                  # evaluate and save checkpoints for every # epoches
    --checkpoint_dir=./checkpoint           # if it is not existed, automatically make dirs
    --sample_dir=./sample                   # dir for saving evaluation results during training
 ```
 #### Objective Results ####
[Naturalness Image Quality Evaluator (NIQE)](https://ieeexplore.ieee.org/document/6353522) is used for no-reference image quality score for quantitative comparison. NIQE compares images to a default model computed from images of natural scenes. A smaller score indicates better perceptual quality.
 
| Dataset | DICM | NPE | MEF | Average |
| ------ | ------ | ------ | ------ | ------ |
| MSRCR | 3.117 | 3.369 | 4.362 | 3.586 |
| LIME | 3.243 | 3.649 | 4.745 | 3.885 |
| DeHZ | 3.608 | 4.258 | 5.071 | 4.338 | 
| SRIE | 2.975 | <b>3.127</b> | 4.042 | 3.381 |
| <b>GLADNet</b> | <b>2.761</b> | 3.278 | <b>3.468</b> | <b>3.184</b> |

