from ultralytics import YOLO
model = YOLO('yolo11n.pt')
bild = input()
results = model(bild)


for result in results:
    boxes = result.boxes       
    names = result.names        
    confidence = boxes.conf     

for box in boxes:
    x1, y1, x2, y2 = box.xyxy[0]  # Koordinaten der Box
    confidence = box.conf[0]       # Wie sicher? (0.0 bis 1.0)
    class_id = box.cls[0]          # Was wurde erkannt?
    print(f"Gefunden: {names[int(class_id)]} mit {confidence:.2f} Sicherheit")

results[0].show()