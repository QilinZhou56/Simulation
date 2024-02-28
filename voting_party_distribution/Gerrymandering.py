import tkinter as Tk
import random
import math
from PIL import ImageGrab
random.seed(42)
# Major Principles
"""
Equal Population: Striving for equal numbers of constituents in each district.
Contiguity: Ensuring all parts of a district are connected.
Compactness: Avoiding oddly shaped districts.
"""
class Gerrymandering:
    def __init__(self, n, num_districts):
        self.n = n
        self.num_districts = num_districts
        self.root = Tk.Tk()
        self.C = Tk.Canvas(self.root, width=500, height=500)
        self.rects = []

        district_colors = self.random_distribution(n)
        self.draw_districts(district_colors)
        self.C.pack()
        self.button = Tk.Button(self.root, text="Save Canvas", command=self.save_canvas)
        self.button.pack()

    def random_distribution(self, n):
        light_red = '#FF9999'  
        light_blue = '#9999FF'  
        # Equal Population
        return [[light_red if random.random() < 0.5 else light_blue for _ in range(n)] for _ in range(n)]

    def draw_districts(self, district_colors):
        """
        Draw districts based on a defined redistribution policy
        Here adopt a simplified redistribution method: 
        assume districts are approximately square
        """
        total_cells = self.n * self.n
        cells_per_district = total_cells // self.num_districts

        district_width = int(self.n // math.sqrt(self.num_districts))
        district_height = int(self.n // math.sqrt(self.num_districts))

        # Adjust if the exact division is not possible
        if district_width * district_height < self.num_districts:
            district_width += 1

        district_count = 0
        for i in range(0, self.n, district_height):
            for j in range(0, self.n, district_width):
                if district_count >= self.num_districts:
                    break

                # Calculate the boundary of the current district
                top_left_x = (500 // self.n) * j
                top_left_y = (500 // self.n) * i
                bottom_right_x = top_left_x + (500 // self.n) * min(district_width, self.n - j)
                bottom_right_y = top_left_y + (500 // self.n) * min(district_height, self.n - i)

                for di in range(district_height):
                    if i + di >= self.n:
                        break
                    for dj in range(district_width):
                        if j + dj >= self.n:
                            break
                        row, col = i + di, j + dj
                        color = district_colors[row][col]

                        self.C.create_rectangle((500 // self.n) * col, (500 // self.n) * row,
                                                (500 // self.n) * (col + 1), (500 // self.n) * (row + 1),
                                                fill=color, outline=color)

                # Draw the boundary for this district
                self.C.create_rectangle(top_left_x, top_left_y, 
                                        bottom_right_x, bottom_right_y, 
                                        outline='black', width=2)

                district_count += 1
        
    def save_canvas(self):
        self.root.update_idletasks()  # Ensure the window is fully updated
        self.root.update()

        # Use the geometry of the window plus the canvas position to get the correct bounding box
        x = self.root.winfo_rootx() + self.C.winfo_x()
        y = self.root.winfo_rooty() + self.C.winfo_y()
        x1 = x + self.C.winfo_width()
        y1 = y + self.C.winfo_height()

        # Grab the specified region and save the image
        ImageGrab.grab(bbox=(x, y, x1, y1)).save("Equal_Distribution.png")

def district_party(n, num_districts):
    map = Gerrymandering(n, num_districts)
    return map

if __name__ == '__main__':
    map = district_party(10, 4) 
    map.root.mainloop()
