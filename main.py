import tkinter as tk
import cv2
from ultralytics import YOLO
import random
import keyboard
import yaml
from config import Config

model = YOLO('yolov8n.pt')
config = Config()

print(config.colors.dict)


class PunkteApp:
    cap = cv2.VideoCapture(config.camera_source)
    def __init__(self, master):
        self.master = master
        self.master.title("FLL LINE AI")
        
        # Größe der Fläche
        self.canvas_width = config.canvas.width
        self.canvas_height = config.canvas.height

        # Erstelle Canvas
        self.canvas = tk.Canvas(self.master, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        # Punkte-Liste
        self.punkte = []

        # Benutzer-Eingabe für Punkte
        self.neuer_punkt_input()

    def neuer_punkt_input(self):
        self.cap.read()
        self.display_camera_stream()

    def add_punkt(self, x, y, color):
        # Erstelle Punkt auf der Canvas
        fillColor = '#' + color;
        punkt = self.canvas.create_rectangle(x, y, x, y, fill=fillColor, outline=fillColor)
        # Füge Punkt zur Liste hinzu
        self.punkte.append(punkt)
        self.master.update()
        

    def display_camera_stream(self):
        while True:
            if cv2.waitKey(1) == ord('q'):
                break
            
            
            ret, frame = self.cap.read()
            
            if not ret:
                print("Fehler beim Lesen des Frames.")
                self.cap = cv2.VideoCapture(config.camera_source)
                continue
            cv2.imshow("Kamera-Stream", frame)
            
            #keyboard.wait(config.key)
            if(not keyboard.is_pressed(config.key)):
                continue
            
            print("shoot pic...")
            # Lese ein Frame von der Kamera
            # Führe YOLO-Objekterkennung durch
            results = model(frame)

            # Zeige das Frame an
            
            processed = [];
            # Durchlaufe erkannte Objekte und füge zufällige Punkte hinzu
            for box in results[0].boxes:
                if box.cls in processed:
                    print("skip")
                    continue
                processed.append(box.cls)
                xVar, yVar = (random.randint(config.canvas.border, config.canvas.width - config.canvas.border),
                              random.randint(config.canvas.border, config.canvas.height - config.canvas.border))
                length = random.randint(config.length.min,config.length.max)
                directionHor = random.choice([True, False])
                print(box.cls)
                if int(box.cls) in config.colors.dict:
                    color = config.colors.dict[int(box.cls)];
                else:
                    if config.colors.showDefault:
                        color = config.colors.default
                    else:
                        continue
                
                if(directionHor):
                    for i in range(length):
                        self.add_punkt(i+xVar, yVar, color)
                else:
                    for i in range(length):
                        self.add_punkt(xVar, i+yVar, color)
            
            # Warte auf das Drücken der Entertaste (13) für das nächste Frame
            
            

        # Freigabe der Kamera und Schließe das OpenCV-Fenster
        self.cap.release()
        cv2.destroyAllWindows()
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PunkteApp(root)
    root.mainloop()