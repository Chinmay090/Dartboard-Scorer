# Automatic Dartboard Scoring System (Project ID - 26)

- [Automatic Dartboard Scoring System (Project ID - 26)](#automatic-dartboard-scoring-system-project-id---26)
  - [Brief Description](#brief-description)
  - [Setup and Installation](#setup-and-installation)
  - [Sample outputs](#sample-outputs)
  - [Team Information](#team-information)
  - [Biblography](#biblography)

## Brief Description

Our project ADSS is a dartboard scoring system that uses a camera to detect the position of the dart and then calculates the score based on the position of the dart. The system can then be further integrated into other computer vision applications.

Our project starts off by first analyzing a board with no dart. Using bitmap techniques we segment the image into various multiplier regions. These are the inner bullseye, outer bullseye, triple ring, double ring, and single region.

Then we segment the image into various sectors which are total 20 in number. This is done with the help of hough transform. The next task of the program is to find the sector in which a given point lies. We find perpendicular distance of the point from all the lines and the two smallest distances correspond to the lines between which the point lies.

Now we know the sector score and given the multiplier region, it is trivial to calculate the final score.

## Setup and Installation

Note: `pip3` and `python3` are used in the following commands. Given your python version you may have to use its variants such as `python`, `pip3.9`, `pip` etc.

- Project uses Python virtual environment. To setup the virtual environment, run the following commands:
  - To create a virtual environment, run `python3 -m venv dartProj`
  - Activate the kernel: `source dartProj/bin/activate`
  - Install ipykernel: `pip3 install ipykernel`
  - then: `ipython kernel install --user --name=dartProj`
- Install all requirements using `pip3 install -r requirements.txt`
- Open the notebook in vscode, select the virtual kernel and run all.

## Sample outputs

Inputs: https://drive.google.com/file/d/1UEsRjalwrHg0uJIZKwYiFZbre1PxvNTd/view?usp=share_link

Sample intermediary outputs: https://drive.google.com/file/d/1_ekP6IfwXruCJN6Ch6B03cJolEqfHToj/view?usp=share_link

## Team Information

Mentor - Eshan Gupta

Team - It’s Something

- Rahul Garg - 2020115006 (CHD)
- Chinmay Deshpande - 2020102069 (ECE)
- Sushil Kumar Yalla - 2020102071 (ECE)
- Geet Dassani - 2020102001 (ECE)

## Biblography

- [Main Paper: Delaney](https://web.stanford.edu/class/ee368/Project_Autumn_1516/Reports/Delaney.pdf)
- [OpenCV](https://opencv.org/)
- [SciPy](https://www.scipy.org/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [matplotlib](https://matplotlib.org/)
- [numpy](https://numpy.org/)
