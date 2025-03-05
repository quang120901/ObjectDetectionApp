import customtkinter as ctk
from tkinter import filedialog, messagebox
import Function
import ObjectDetection

# Initialize Modern Tkinter Window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

wn = ctk.CTk()
wn.title("Object Detection App")
wn.geometry("850x550")
wn.resizable(False, False)

# Main Frame
frame = ctk.CTkFrame(wn)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Title Label
title_label = ctk.CTkLabel(frame, text="Object Detection App", font=("Arial", 22, "bold"))
title_label.pack(pady=10)

# File Selection Section
file_frame = ctk.CTkFrame(frame)
file_frame.pack(fill="x", pady=10)

lblfileImage = ctk.CTkLabel(file_frame, text="No image selected", width=300, fg_color="gray30", corner_radius=5)
lblfileImage.pack(pady=5)

lblfileVideo = ctk.CTkLabel(file_frame, text="No video selected", width=300, fg_color="gray30", corner_radius=5)
lblfileVideo.pack(pady=5)

open_file_button = ctk.CTkButton(file_frame, text="Browse File", command=lambda: Function.OpenFile(lblfileImage, lblfileVideo))
open_file_button.pack(pady=5)

# Input Frames for Rotate and Resize
input_frame = ctk.CTkFrame(frame)
input_frame.pack(pady=10, fill="x")

# Rotate Input
rotate_frame = ctk.CTkFrame(input_frame)
rotate_frame.pack(fill="x", pady=5)

ctk.CTkLabel(rotate_frame, text="Rotate Angle:", font=("Arial", 12)).pack(side="left", padx=5)
angle_entry = ctk.CTkEntry(rotate_frame, width=50, placeholder_text="45")
angle_entry.insert(0, "45")
angle_entry.pack(side="left", padx=5)

# Resize Input
resize_frame = ctk.CTkFrame(input_frame)
resize_frame.pack(fill="x", pady=5)

ctk.CTkLabel(resize_frame, text="Width:", font=("Arial", 12)).pack(side="left", padx=5)
width_entry = ctk.CTkEntry(resize_frame, width=50, placeholder_text="200")
width_entry.insert(0, "200")
width_entry.pack(side="left", padx=5)

ctk.CTkLabel(resize_frame, text="Height:", font=("Arial", 12)).pack(side="left", padx=5)
height_entry = ctk.CTkEntry(resize_frame, width=50, placeholder_text="200")
height_entry.insert(0, "200")
height_entry.pack(side="left", padx=5)

# Action Buttons
button_frame = ctk.CTkFrame(frame)
button_frame.pack(pady=20)

ctk.CTkButton(button_frame, text="Cut Frame", command=Function.VideoFrame, width=180).grid(row=0, column=0, padx=10, pady=5)
ctk.CTkButton(button_frame, text="Show Image", command=Function.ShowImage, width=180).grid(row=0, column=1, padx=10, pady=5)

ctk.CTkButton(button_frame, text="Rotate Image", command=lambda: Function.Rotate(angle_entry), width=180).grid(row=1, column=0, padx=10, pady=5)
ctk.CTkButton(button_frame, text="Resize Image", command=lambda: Function.Resize(width_entry, height_entry), width=180).grid(row=1, column=1, padx=10, pady=5)

ctk.CTkButton(button_frame, text="Object Detection", command=lambda: ObjectDetection.process_video_feed(2), width=180).grid(row=2, column=0, padx=10, pady=5)
ctk.CTkButton(button_frame, text="Object From Image", command=lambda: ObjectDetection.object_from_image(), width=180).grid(row=2, column=1, padx=10, pady=5)

exit_button = ctk.CTkButton(frame, text="Exit", command=lambda: Function.Exit(wn), width=200, fg_color="red")
exit_button.pack(pady=10)

wn.mainloop()
