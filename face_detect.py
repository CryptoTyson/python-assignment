import pygame.camera
import face_recognition

pygame.init()
pygame.camera.init()
cam_list = pygame.camera.list_cameras()
cam = None
if cam_list:
    cam = pygame.camera.Camera(cam_list[0], (640, 480))
    cam.start()

window_surface = pygame.display.set_mode((640, 480))

color = (255,0,0) 
my_image = face_recognition.load_image_file("my_image.jpg")
my_face_encoding = face_recognition.face_encodings(my_image)[0]
known_face_encodings =[my_face_encoding]

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    if cam is not None:
        
        image = cam.get_image()
        pygame.image.save(image, "image.jpg")
        face_image = face_recognition.load_image_file("image.jpg")
        face_locations = face_recognition.face_locations(face_image)
        if len(face_locations) != 0:
            face_encodings = face_recognition.face_encodings(face_image, face_locations)
            matches = face_recognition.compare_faces(known_face_encodings, face_encodings[0])
            print((face_locations))
            window_surface.blit(image, (0,0))
            if matches[0]== True:
                window_surface.blit(pygame.font.Font('freesansbold.ttf', 32).render('My_face', True, color),window_surface.get_rect().topleft)
            else:
                window_surface.blit(pygame.font.Font('freesansbold.ttf', 32).render('Unknown', True, color),window_surface.get_rect().topleft)
                
            pygame.draw.rect(window_surface, color, pygame.Rect(face_locations[0][3], face_locations[0][0], face_locations[0][1], face_locations[0][2]), 2) 
        else:
            window_surface.blit(image, (0,0))

    pygame.display.update()