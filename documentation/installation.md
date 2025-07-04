# Installation

Bento requires Python version 3.6 or above, and can be run on Windows, MacOS, or Linux.

**Follow the instructions below to install Bento :** <br>

1. Download the Bento code.<br>
   a. Go to [Release](https://github.com/neuroethology/bento/releases) section.<br>
   b. Download source code corresponding to the release you want, probably the latest.<br>
   c. Unzip the source file to the folder of your choice. For best performance, choose a folder on your local machine.<br>

2. Install [Anaconda](https://www.anaconda.com/products/individual#macos). Install Anaconda or Miniconda based on your operating system (Mac, Windows or Linux) by following the prompts when you run the downloaded installation file.

3. Once installed, open an Anaconda Prompt window (for Windows) or Terminal window (for Mac or Linux). 

4. Find the location where Bento folder is located and execute the following command on the Anaconda Prompt or terminal window: 

```
cd path_to_bento_folder
```
 - Ex : cd /Users/KennedyLab/all_codes/bento

5. Execute the following command to install all the dependencies/packages required for Bento.<br>

```
conda env create -f bento.yml
```

6. Execute the following two commands to open the Bento User Interface:

```
conda activate bento
python src/bento.py
```
