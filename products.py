from tkinter import *
from PIL import Image, ImageTk
import os

class productclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("INVENTORY MANAGEMENT SYSTEM")
        self.root.config(bg="white")
        
        self.images = []

        self.product_names = [
            "Agbot", "See & Spray", "Tertill", "Robotti",
            "RIPPA", "Octinion's", "Ecorobotix's robot", "Vitirover",
            "Dino", "VIN Robot"
        ]

        self.product_texts = {
            "Agbot": "Agbot, short for Agricultural Robot, is a type of robotic technology designed and developed for use in agriculture. It represents a new approach to modern farming by incorporating automation and robotics into various aspects of agricultural processes. Agbots are equipped with advanced sensors, cameras, and other technologies that enable them to perform tasks such as planting, monitoring, and harvesting crops, as well as managing weeds and pests.",
            "See & Spray": "This robot utilizes computer vision and machine learning to identify and target weeds in real time. It can precisely apply herbicides only where needed, reducing the amount of chemicals used and minimizing environmental impact.",
            "Tertill": "Created by the makers of the Roomba vacuum cleaner, Tertill is a small, solar-powered robot designed to patrol gardens and eliminate weeds. It distinguishes between plants and weeds, cutting down unwanted growth while sparing cultivated plants.",
            "Robotti": "Robotti is an autonomous platform developed for planting and seeding tasks. It can navigate fields, prepare seedbeds, and plant crops with high accuracy and efficiency.",
            "RIPPA": " RIPPA is designed to detect and remove individual weeds among crops. It uses cameras and sensors to identify and target weeds, reducing the need for herbicides.",
            "Octinion's": " Rubion is a strawberry-picking robot equipped with soft grippers and advanced vision systems. It carefully picks ripe strawberries without damaging them, enhancing efficiency in berry harvesting.",
            "Ecorobotix's robot": "Ecorobotix's robot is designed to apply herbicides to weeds with precision. Its targeted approach reduces chemical usage and minimizes the impact on the environment.",
            "Vitirover": " Vitirover is a solar-powered grazing robot used in vineyards and orchards to manage vegetation and control weeds. It autonomously grazes and maintains the vegetation at desired levels.",
            "Dino": ": Dino is a vineyard robot that aids in tasks such as soil analysis, weeding, and spraying. It navigates between rows of vines, helping vineyard owners manage their crops more efficiently.",
            "VIN Robot": " Wall-Ye V.I.N. (Viticulture Intelligent Robot) is designed for wine grape vineyards. It can prune, de-bud, and perform other maintenance tasks, helping vineyard managers optimize grape quality."
        }

        image_dir = "Image"
        for i in range(1, 11):
            image_path = os.path.join(image_dir, f"product{i}.png")
            if os.path.exists(image_path):
                img = Image.open(image_path)
                img.thumbnail((200, 200))
                img = ImageTk.PhotoImage(img)
                self.images.append(img)
            else:
                self.images.append(None)

        self.create_image_widgets()

    def open_product_window(self, product_index):
        product_window = Toplevel(self.root)
        product_window.title(f"Product: {self.product_names[product_index]}")
        product_window.geometry("600x550")  # Set the window size

        # Add desired text
        text = self.product_texts.get(self.product_names[product_index], "No text available")
        text_label = Label(product_window, text=text, font=("Helvetica", 14), wraplength=300)
        text_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")

        # Load the image for the selected product
        img_label = Label(product_window, image=self.images[product_index])
        img_label.grid(row=0, column=1, padx=(0, 20), pady=(20, 0), sticky="ne")

        # Buy Now button
        buy_button = Button(product_window, text="Buy Now",bg="yellow", font=("Helvetica", 12, "bold"),
                            command=lambda idx=product_index: self.buy_product(idx))
        buy_button.grid(row=2, column=1, padx=(0, 20), pady=(0, 20), sticky="w")

    def buy_product(self, product_index):
        # Add your buy product logic here
        print(f"Buying {self.product_names[product_index]}")

    def create_image_widgets(self):
        rows = 2
        cols = 5
        image_index = 0

        title = Label(self.root, text="Products", font=("Arial", 20, "bold"), bg="#0f4d7d", fg="white")
        title.grid(row=0, column=0, columnspan=cols + 1, pady=(10, 20), padx=(20, 20), sticky="ew")

        for r in range(rows):
            for c in range(cols):
                if image_index < len(self.images) and self.images[image_index] is not None:
                    frame = Frame(self.root, bg="white")
                    frame.grid(row=r + 1, column=c, padx=20, pady=20)

                    button = Button(frame, image=self.images[image_index],
                                    command=lambda idx=image_index: self.open_product_window(idx))
                    button.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

                    label = Label(frame, text=self.product_names[image_index], bg="white",
                                  font=("Arial", 12, "bold"))
                    label.grid(row=1, column=0, padx=10, pady=(5, 0))

                image_index += 1

        # Add an empty frame to adjust layout
        empty_frame = Frame(self.root, bg="white")
        empty_frame.grid(row=rows + 1, columnspan=cols + 1, padx=0, pady=0)
        
    def database(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=database(self.new_win)

root = Tk()
obj = productclass(root)
root.mainloop()
