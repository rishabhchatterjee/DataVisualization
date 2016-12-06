# DataVisualization

# Proposal

Using turtle graphics, I wish to create a data visualization engine for rational and irrational numbers (like pi) as well as functions. I will visualize each digit of the real number using recursive division (as well as Chudnovsky's Alg for pi for extra precision since my recursive division gives precision upto 10^-6) using a circular web. The circle will have 10 parts, each part being a digit from 0-9 and color coded. As the digits are being calculated via recursive division, a network will be drawn from one digit to the next and so on. For functions I have two intentions -- first plotting digit by digit and second using Modular Arithemetic mod 10 to get the one's digit and plotting that (left to the choice of the user). This will yield a complex web of connections which looks really pretty. While the lines are being drawn there will also be a tone that is played (each digit having a distinct sound) as to create music with numbers. This will add a new dimension to 'visualizing' data. 

The program also makes a sound wheenever it encounters an integer solution to the function or a 0 in the decimal expansion and displays the solution/index value of the zero. 

The visualization is three parts -- a gradient, scatterplot, and a network.

This product can be used to teach people. Firstly, it is user-friendly since it creates art from numbers. This will make people love numbers instead of fearing them. Secondly, it is really helpful for those who prefer a visual learning method. 

# Modules

Modules I will be using are :
1) Turtle
2) PyAudio
3) Tkinter

# Competitive Analysis

While there are no direct competitors to my idea, there are websites and other programs which helps you draw graphs given a data set. These include Microsoft Excel, Dyagraphs, Tableau, etc. However, these softwares are not like mine in the sense that they are not built with the intention to visualize mathematical concepts the way I am doing it by integrating sound into it. Along with that, another difference is that the motivation to build the visualization machine in their cases is simply to allow the user to draw graphs etc but mine is to help teach, and moreover help like, numbers and data, with an additional feature for the visually impaired.
