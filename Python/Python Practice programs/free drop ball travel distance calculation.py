"""
A ball drops from 100 meters above the ground, everytime it bounces back to half
of its last height. This goes on and on until the 10h drop, how many meters it
travels? What is the 10th height it bounces back into the sky?
"""
h = 200 
total = 100
for i in range(10):
    h /= 2
    total += h
print('The height of the 10th bounce up is: ',h/2)
print('The total meters the ball travelled is: ',total)

'''
The code is simple, but it took me a while to think about the math behind it:

A single repeating bounce up + drop down is one round, we know that:
1. the bounce up height is half of the last drop height;
2. the ball bounces up and then goes down, the two distances are the same;
3. travel distance of one round would be the sum of bounce up and drop down,
which is h/2 +h/2 = h (the height of last bounce up)

Below is the loop bouncing:
The first bounce up h is half of the initial height, initial height should be
100 meters as given, (so we assign h to 200 before the for loop) 100/2 = 50,
first round distance would be 50(bounce up) + 50 (drop down) = 100
The second bounce up h is half of the first height of 50 meters, 50/2 = 25, 2nd
round distance would be 25 + 25 = 50
.
.
.
Until the 10th bounce up, same situation as above.

Plus the first 100 meters of drop down, we set it as the initial total distance.
In every loop, we add the previous h (actually the two half h the ball travels)
to the total to get the total distance travelled.

'''
