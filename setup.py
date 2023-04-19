import cx_Freeze

executables = [cx_Freeze.Executable('ia.py')]

cx_Freeze.setup(
    name="dino game",
    options={'build_exe': {'packages':['pygame','speech_recognition','cv2','pytesseract','pyttsx3','threading','pyautogui'],
                           'include_files':['images', 'audio','__pycache__','Tesseract-OCR']}},

    executables = executables
    
)