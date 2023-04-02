import tkinter as tk
import random
from time import sleep


class Human:

    def __init__(self, p, s, l):
        self.p = p
        self.s = s
        self.l = l
        self.infected = False


def create_gui():
    def create_grid(p, s1, s2, s3, s4, l):
        root = tk.Tk()
        root.geometry("1000x1000")
        root.title("Simulation")
        canvas = tk.Canvas(root, width=700, height=700, bg='white')
        canvas.pack()
        cell_size = 5

        grid0 = [[None for j in range(100)] for i in range(100)]
        grid1 = [[None for j in range(100)] for i in range(100)]
        flag = 1
        for i in range(100):
            for j in range(100):
                if random.random() < p:
                    rand = random.random()
                    s = 0
                    if rand < s1:
                        s = s1
                    elif rand < s1 + s2:
                        s = s2
                    elif rand < s1 + s2 + s3:
                        s = s3
                    else:
                        s = s4

                    human = Human(p, s, l)
                    grid1[i][j] = human
                    canvas.create_rectangle(i * cell_size + 50, j * cell_size + 50, (i + 1) * cell_size + 50, (j + 1) * cell_size + 50, fill='blue')
                else:
                    grid1[i][j] = None
                    canvas.create_rectangle(i * cell_size + 50, j * cell_size + 50, (i + 1) * cell_size + 50, (j + 1) * cell_size + 50, fill='white')

        human = None
        while human is None:
            i = random.randint(0, 99)
            j = random.randint(0, 99)
            human = grid1[i][j]

        human.infected = True
        canvas.create_rectangle(i * cell_size + 50, j * cell_size + 50, (i + 1) * cell_size + 50, (j + 1) * cell_size + 50, fill='red')

        def update_grid():
            prev_grid = None
            new_grid = None

            # we need to update grid 0

            if flag:
                new_grid = grid0
                prev_grid = grid1

            #update grid1
            else:
                new_grid = grid1
                prev_grid = grid0


            for i in range(100):
                for j in range(100):
                    human = prev_grid[i][j]
                    if human:
                        if not human.infected:
                            pass



            #canvas.create_rectangle(i * cell_size + 50, j * cell_size + 50, (i + 1) * cell_size + 50,(j + 1) * cell_size + 50, fill='red')
            root.after(100, update_grid) # update the canvas
            #canvas.update()

        root.after(1, update_grid)
        root.mainloop()


    def next_screen():
        #p = float(p_entry.get())
       # s1 = float(s1_entry.get())
        #s2 = float(s2_entry.get())
        #s3 = float(s3_entry.get())
       # s4 = float(s4_entry.get())
        #        l = float(l_entry.get())

        p = 0.1
        s1 = 0.1
        s2 = 0.1
        s3 = 0.1
        s4 = 0.1
        l = 5


        root.destroy()
        create_grid(p, s1, s2, s3, s4, l)

    root = tk.Tk()
    root.geometry("510x510")
    root.title("Simulation")
    p_label = tk.Label(root, text="Enter probability p:")
    p_label.pack()
    p_entry = tk.Entry(root)
    p_entry.pack()
    s1_label = tk.Label(root, text="Enter probability s1:")
    s1_label.pack()
    s1_entry = tk.Entry(root)
    s1_entry.pack()
    s2_label = tk.Label(root, text="Enter probability s2:")
    s2_label.pack()
    s2_entry = tk.Entry(root)
    s2_entry.pack()
    s3_label = tk.Label(root, text="Enter probability s3:")
    s3_label.pack()
    s3_entry = tk.Entry(root)
    s3_entry.pack()
    s4_label = tk.Label(root, text="Enter probability s4:")
    s4_label.pack()
    s4_entry = tk.Entry(root)
    s4_entry.pack()
    l_label = tk.Label(root, text="Enter time l:")
    l_label.pack()
    l_entry = tk.Entry(root)
    l_entry.pack()
    button = tk.Button(root, text="Next", command=next_screen)
    button.pack()
    canvas = tk.Canvas(root, width=500, height=500, bg='white')
    root.mainloop()

def main():
    create_gui()


if __name__ == "__main__":
    main()