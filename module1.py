import cv2
import os
import PythonApplication1 as of
import keyboard as kb
def capture_and_save_image():
    cam=cv2.VideoCapture(0)
    cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)
    while(True):
        ret, frame = cam.read()
        cv2.imshow("Computer Camera",frame)
        if(kb.is_pressed('c')):
         break
        cv2.waitKey(1)
    cam.release()
    label = input("Enter a label for the image: ")
    if not os.path.exists('known_faces_dir'):
        os.makedirs('known_faces_dir')
    image_path = os.path.join('known_faces_dir', f'{label}.jpg')
    cv2.imwrite(image_path, frame)
    print(f"Image saved successfully at: {image_path}")
if __name__ == "__main__":
    while(True):
        os.system("CLS")
        ch=input("Enter Your choice: \n1.Attendance\n2.New Face\n   -->> ")
        if ch=="1":
         of.Attendance()
        if ch=="2":
         capture_and_save_image()
        else:
         print("\nWrong Choice Try Again")
         break

