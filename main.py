import cv2

# Carrega o classificador de Haar Cascade para detecção de faces
face_cascade = cv2.CascadeClassifier(r'C:\Users\adeni\PycharmProjects\reconhecimento_facial\.venv\haarcascade_frontalface_default.xml')

# Abre a webcam (normalmente a webcam padrão é o dispositivo 0)
cap = cv2.VideoCapture(0)

# Verifica se a webcam foi aberta corretamente
if not cap.isOpened():
    print('Erro ao abrir a webcam')
else:
    while True:

        # Defina a janela como redimensionável
        cv2.namedWindow('Webcam - Reconhecimento Facial', cv2.WINDOW_NORMAL)

        # Redimensione a janela para 800x600
        cv2.resizeWindow('Webcam - Reconhecimento Facial', 800, 600)

        # Captura frame a frame
        ret, frame = cap.read()

        # Verifica se o frame foi capturado corretamente
        if not ret:
            print('Erro ao capturar o frame')
            break

        # Converte o frame para escala de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detecta faces no frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Desenha um retângulo ao redor de cada face detectada
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Exibe o frame
        cv2.imshow('Webcam - Reconhecimento Facial', frame)

        # Aguarda por 1ms a tecla 'q' ser pressionada para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Libera o objeto da webcam e fecha todas as janelas abertas
cap.release()
cv2.destroyAllWindows()
