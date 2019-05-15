from tkinter import *
from math import cos, sin, pi


class Circle:

    def __init__(self, center, radius, theta, velocity):
        self.radius = radius
        self.center = center
        self.theta = theta
        self.velocity = velocity
        self.angle = self.theta*self.velocity - pi/2
        self.x = round(self.center[0] + self.radius * cos(self.angle))
        self.y = round(self.center[1] + self.radius * sin(self.angle))

    def update(self, theta):
        self.angle = theta*self.velocity - pi/2
        self.x = round(self.center[0] + self.radius * cos(self.angle))
        self.y = round(self.center[1] + self.radius * sin(self.angle))


class Lissajous:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Draw:

    def __init__(self, n):
        self.n = n
        self.root = Tk()
        self.frame = Frame(self.root)
        self.root.tk.call('tk', 'scaling', 10)
        canvas_size = 800
        self.width = canvas_size
        self.height = canvas_size
        self.root.title('Lissajous Curves')
        self.root.geometry(f'{self.width}x{self.height}')
        self.radians = pi/180
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.frame.pack()
        self.canvas = Canvas(self.frame, width=self.width, height=self.height, bg='black',
                             offset='0,0', highlightthickness=0)
        self.canvas.pack()
        self.lj_matrix()

    def on_closing(self):
        self.root.destroy()

    def lj_matrix(self):
        try:
            c0 = []
            c1 = []
            for i in range(self.n):
                c0.append(Circle(center=(round(self.width*(3+2*i)/(2*(self.n+1))), round(self.height/(2*(self.n+1)))),
                                 radius=round(self.height*0.9/(2*(self.n+1))), theta=0, velocity=i+1))
                c1.append(Circle(center=(round(self.width/(2*(self.n+1))), round(self.height*(3+2*i)/(2*(self.n+1)))),
                                 radius=round(self.height*0.9/(2*(self.n+1))), theta=0, velocity=i+1))

            while c0[0].theta <= 2*pi:
                self.canvas.delete('pointer')  # always on
                # self.canvas.delete('lj')       # clear lj curves
                # self.canvas.delete('circles')       # clear circles
                c0_prev = []
                c1_prev = []
                c0_active = []
                c1_active = []
                for i in range(self.n):
                    c0_prev.append((c0[i].x, c0[i].y))
                    c1_prev.append((c1[i].x, c1[i].y))
                lj_prev = [[Lissajous(x=c0[i].x, y=c1[j].y) for j in range(self.n)] for i in range(self.n)]
                for i in range(self.n):
                    c0[i].theta += 0.05
                    c1[i].theta += 0.05
                    c0_active.append((c0[i].theta <= 2*pi))
                    c1_active.append((c1[i].theta <= 2*pi))
                    c0[i].update(theta=c0[i].theta)
                    c1[i].update(theta=c1[i].theta)
                lj = [[Lissajous(x=c0[i].x, y=c1[j].y) for j in range(self.n)] for i in range(self.n)]
                for i in range(self.n):
                    self.canvas.create_oval(c0[i].x - 3, c0[i].y - 3, c0[i].x + 3, c0[i].y + 3, fill='black',
                                            outline='white', tags=f'pointer')
                    self.canvas.create_oval(c1[i].x - 3, c1[i].y - 3, c1[i].x + 3, c1[i].y + 3, fill='black',
                                            outline='white', tags=f'pointer')
                    if c0_active[i]:
                        self.canvas.create_line(c0[i].x, c0[i].y, c0_prev[i][0], c0_prev[i][1], fill='white',
                                                smooth='true', tags=f'circles')
                    if c1_active[i]:
                        self.canvas.create_line(c1[i].x, c1[i].y, c1_prev[i][0], c1_prev[i][1], fill='white',
                                                smooth='true', tags=f'circles')
                for i in range(self.n):
                    for j in range(self.n):
                        self.canvas.create_oval(lj[i][j].x - 3, lj[i][j].y - 3, lj[i][j].x + 3, lj[i][j].y + 3,
                                                fill='black', outline='white', tags=f'pointer')
                        if c0_active[i] and c1_active[j]:
                            self.canvas.create_line(lj[i][j].x, lj[i][j].y, lj_prev[i][j].x, lj_prev[i][j].y,
                                                    fill='white', smooth='true', tags=f'lj')
                self.canvas.update()
            self.canvas.delete(ALL)
            self.lj_matrix()
        except TclError as err:
            if str(err) == 'invalid command name ".!frame.!canvas"':
                pass
            else:
                raise


if __name__ == '__main__':
    draw = Draw(8)
