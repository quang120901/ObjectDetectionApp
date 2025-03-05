import cv2
import os
from tkinter import messagebox, filedialog

vdirf = 'VideoFrame'
pfile = None
vfile = None
os.makedirs(vdirf, exist_ok=True)

def Exit(wn): 
    answer = messagebox.askquestion("Confirm", "Do you want to exit (Y/N)?")
    if answer == "yes":
        wn.destroy()

def ShowImage():
    if not pfile:
        messagebox.showerror("Error", "Please select image file first.")
        return
    img = cv2.imread(pfile)  
    cv2.imshow('Original Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Rotate(angle_entry):
    if not pfile:
        messagebox.showerror("Error", "Please select image file first.")
        return
    try:
        angle = float(angle_entry.get())
        img = cv2.imread(pfile)  
        (h, w, d) = img.shape
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(img, M, (w, h))
        cv2.imshow(f'Photo rotated {angle} degrees', rotated)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the rotation angle.")

def Resize(width_entry, height_entry):
    if not pfile:
        messagebox.showerror("Error", "Please select image file first.")
        return
    try:
        new_width = int(width_entry.get())
        new_height = int(height_entry.get())
        if new_width <= 0 or new_height <= 0:
            raise ValueError("Size must be greater than 0")
        
        img = cv2.imread(pfile) 
        rd = cv2.resize(img, (new_width, new_height))
        cv2.imshow(f'New size {new_width}x{new_height}', rd)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except ValueError as e:
        messagebox.showerror("Error", str(e) if str(e) != "" else "Please enter a valid integer for size.")

def OpenFile(lblfileImage, lblfileVideo): 
    global pfile, vfile

    filepath = filedialog.askopenfilename(
        title="Choose file",
        filetypes=(
            ("Image File (.jpg, .jpeg, .png)", "*.jpg;*.jpeg;*.png"),
            ("Video File (.mp4, .mov)", "*.mp4;*.mov")
        )
    )

    if not filepath:
        return
    if filepath.endswith(('.jpg', '.jpeg', '.png')):
        pfile = filepath  
        lblfileImage.configure(text="File Image: %s" % pfile)
    elif filepath.endswith(('.mp4', '.mov')):
        vfile = filepath 
        lblfileVideo.configure(text="File Video: %s" % vfile)
    else:
        messagebox.showerror("Error", "Please select the correct image or video file type.")
        
def VideoFrame():
    if not vfile:
        messagebox.showerror("Error", "Please select video file first.")
        return

    cap = cv2.VideoCapture(vfile)
    if not cap.isOpened():
        messagebox.showerror("Error", "Cannot open video.")
        return

    c = 0   
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Press "q" to stop', frame)
        frame_path = os.path.join(vdirf, f"Frame{c}.jpg")
        cv2.imwrite(frame_path, frame)   
        c += 1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    messagebox.showinfo("Notification", f"Total frames: {c}")
