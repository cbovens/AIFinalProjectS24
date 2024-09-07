from ultralytics import YOLO

model = YOLO('MoldModel.pt')
inp = input("Select 'Webcam' or 'Image':")
match inp:
    case "Webcam":
        var = 0
    case "Image":
        var = 'image.jpg'
model.info()
results = model(source=var, show=True, conf=0.8, save=True)