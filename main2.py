"""
Itay Shwartz 318528171
Noa Eitan 316222777

Running instructions:
1. Run the main2.py file

2. In the popping screen enter:
    p - probability for the density of the population.
    S1 - S4 - the percent of humans of each level of skepticism.
    L - number of generation that the person who spread the rumors not past another rumors

3.  In the next screen you will see grid with colors:
    White - represent empty cell (without humans)
    Blue - human that not spread the rumor in this generation.
    Red - human that spread the rumor in this generation.

4.  The running of the program will stop when the rumors will stop to spread. than you can close the screen - just
    press the close button.
"""




import tkinter as tk
import random
import copy

from time import sleep


class Human:

    def __init__(self, s, l):
        self.exposed = 0
        self.s = s
        self.l = l
        self.infected = False

def create_gui(p, s1, s2, s3, s4, l):
    def create_grid():

        generation = l
        root = tk.Tk()



        cell_size = 5

        padding_i = 100
        padding_j = 60


        global prev_grid
        global new_grid
        global human_exposed
        global max_index
        global humans
        global gen
        global sum_gen
        sum_gen = []

        humans = 0
        gen = 0
        max_index = 100
        human_exposed = 0

        prev_grid = [[None for j in range(max_index)] for i in range(max_index)]
        new_grid = [[None for j in range(max_index)] for i in range(max_index)]

        for i in range(max_index):
            for j in range(max_index):
                if random.random() < p:
                    humans += 1
                    rand = random.random()
                    s = 0
                    if rand < s1:
                        s = 1
                    elif rand < s1 + s2:
                        s = 2
                    elif rand < s1 + s2 + s3:
                        s = 3
                    else:
                        s = 4

                    human = Human(s, 0)
                    human.infected = False
                    prev_grid[i][j] = human
                else:
                    prev_grid[i][j] = None

        human = None
        while human is None:
            i = random.randint(0, max_index - 1)
            j = random.randint(0, max_index - 1)
            human = prev_grid[i][j]

        human_exposed += 1
        human.infected = True
        human.exposed += 1
        prev_grid[i][j] = copy.deepcopy(human)

        def update_grid():

            global new_grid
            global prev_grid
            global max_index
            global human_exposed
            global gen
            global sum_gen
            to_finish = True




            percentage = round( (human_exposed / humans), 5)
            sum_gen.append(percentage)

            if gen >= 129:
                print("P is: " + str(p) + " and L is: " + str(generation) + " percentage is: " + str(percentage))
                root.destroy()
                return


            gen += 1

            for i in range(0, max_index):
                for j in range(0, max_index):
                    human = copy.deepcopy(prev_grid[i][j])
                    new_grid[i][j] = copy.deepcopy(human)

                    if human:
                        tmp_s = human.s
                        # human is blue and l is 0
                        if not human.infected and human.l == 0:
                            count = 0

                            if i > 0 and j > 0 and prev_grid[i - 1][j - 1] and prev_grid[i - 1][j - 1].infected:
                                count += 1
                            if i > 0 and prev_grid[i - 1][j] and prev_grid[i - 1][j].infected:
                                count += 1
                            if i > 0 and j < max_index - 1 and prev_grid[i - 1][j + 1] and prev_grid[i - 1][j + 1].infected:
                                count += 1
                            if j > 0 and prev_grid[i][j - 1] and prev_grid[i][j - 1].infected:
                                count += 1
                            if j < max_index - 1 and prev_grid[i][j + 1] and prev_grid[i][j + 1].infected:
                                count += 1
                            if i < max_index - 1 and j > 0 and prev_grid[i + 1][j - 1] and prev_grid[i + 1][j - 1].infected:
                                count += 1
                            if i < max_index - 1 and prev_grid[i + 1][j] and prev_grid[i + 1][j].infected:
                                count += 1
                            if i < max_index - 1 and j < max_index - 1 and prev_grid[i + 1][j + 1] and prev_grid[i + 1][j + 1].infected:
                                count += 1

                            if count == 0:
                                new_grid[i][j].infected = False
                                continue

                            if count >= 2:
                               if tmp_s != 1:
                                   tmp_s -= 1


                            r = random.random()

                            if tmp_s == 1:
                                new_grid[i][j].infected = True
                            elif tmp_s == 2 and r < 2/3:
                                new_grid[i][j].infected = True
                            elif tmp_s == 3 and r < 1/3:
                                new_grid[i][j].infected = True
                            elif tmp_s == 4:
                                new_grid[i][j].infected = False
                            else:
                                new_grid[i][j].infected = False

                            if new_grid[i][j].infected:

                                if new_grid[i][j].exposed == 0:
                                    human_exposed += 1

                                new_grid[i][j].exposed += 1

                                to_finish = False

                        # human is red
                        elif human.infected:
                            # turning human red to blue
                            new_grid[i][j].infected = False
                            new_grid[i][j].l = generation

                            to_finish = False

                        # human is blue and l > 0
                        else:
                            new_grid[i][j].l -= 1

                    # the grid in the i j location is None
                    else:
                        new_grid[i][j] = None


            prev_grid = copy.deepcopy(new_grid)
            # need to do deep copy from the new bords to the grid 0 and 1

            if to_finish:
                root.destroy()
                print("P is: " + str(p) + " and L is: " + str(generation) + " percentage is: " + str(percentage))
                return

            root.after(0, update_grid) # update the canvas


        root.after(0, update_grid)
        root.mainloop()



    create_grid()

import numpy as np


def main():
    global sum_gen
    s1 = 0.5
    s2 = 0.5
    s3 = 0
    s4 = 0


    for s in [[1, 0, 0, 0], [0.25, 0.25, 0.25, 0.25], [0.5, 0.5, 0, 0]]:
        for l in [0, 2, 4]:
            for p in [0.3, 0.6, 0.9]:

                data_list = np.array([0.0] * 130)
                for n in range(10):
                    create_gui(p, s[0], s[1], s[2], s[3], l)
                    while len(sum_gen) < 130:
                        sum_gen.append(sum_gen[-1])
                    data_list += np.array(sum_gen)
                data_list /= 10
                draw_data(p, s[0], s[1], s[2], s[3], l, data_list)


global number
number = 0
import matplotlib.pyplot as plt
def draw_data(p, s1, s2, s3, s4, l, percentage_list):
    global number

    # create a figure and axis object
    fig, ax = plt.subplots()

    # plot the data
    ax.plot(percentage_list)
    ax.set(xlim=(0, 130), ylim=(0, 1))

    # add labels and title
    ax.set_xlabel('Generation')
    ax.set_ylabel('Percentage of humans that hear rumors')
    ax.set_title("P = " + str(p) + " s1 = " + str(s1) + " s2 = " + str(s2) + " s3 = " + str(s3) + " s4 = " + str(s4) + " L = " + str(l))

    # show the plot
    plt.savefig(str(number))
    number += 1


if __name__ == "__main__":
    main()