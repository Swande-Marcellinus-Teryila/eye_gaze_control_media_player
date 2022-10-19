import cv2
import vlc
import easygui
import mediapipe as mp
import pyautogui
media= "video.mp4"
player = vlc.MediaPlayer(media)
image  = "image.jpg"

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
choice = easygui.buttonbox(title="Eye Gaze Media Player                                Developed by:MARCEL SWANDE(software Engineer)",
                           msg="Note:the media will automatically pause if it notices you are sleeping or loose gaze on the screen", image=image,
                           choices=["Play", "Pause", "Stop", "Select Media"])

if choice == "Play":
    player.play()
elif choice == "Pause":
    player.pause()
elif choice == "Stop":
    player.stop()
elif choice == "Select Media":
    media = easygui.fileopenbox(title="choose media to open")

    player = vlc.MediaPlayer(media)
    choice = easygui.buttonbox(
        title="Eye Gaze Media Player                                Developed by: Dr Adebayo Group B",
        msg="Note:the media will automatically pause if it notices you are sleeping or loose gaze on the screen",
        image=image,
        choices=["Play", "Pause", "Stop", "Select Media"])
while True:

    _, frame = cam.read()
    frame = cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _, = frame.shape

    if landmark_points:

        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x*frame_w)
            y = int(landmark.y*frame_h)
            cv2.circle(frame,(x,y),3,(0, 255,0))
            player.play()
            if id == 1:

                screen_x = screen_w/frame_w*x
                screen_y = screen_h/frame_h*y
                #pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145],landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 225))
        if left[0].y -left[1].y<0.02:
            pyautogui.click()
            pyautogui.sleep(1)
            player.set_pause(1)

    else:
        player.set_pause(1)
    cv2.imshow('eye controlled mouse', frame)
    cv2.waitKey(1)

    #contact 08186137570
    #for your Artificial Intelligence projects
    #web development
    #Data science
