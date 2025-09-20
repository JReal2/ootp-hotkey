import keyboard
import pyautogui
import sys
import os

# --- 설정 ---
# 스크립트가 실행되는 폴더의 경로를 기준으로 이미지 파일 경로를 설정합니다.
# 이렇게 하면 어떤 컴퓨터에서든 스크립트가 작동합니다.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AUTOPLAY_BUTTON_PATH = os.path.join(SCRIPT_DIR, 'autoplay.png')
FILE_BUTTON_PATH = os.path.join(SCRIPT_DIR, 'file.png')
SAVE_BUTTON_PATH = os.path.join(SCRIPT_DIR, 'save.png')
YESTERDAY_IMAGE_PATH = os.path.join(SCRIPT_DIR, 'yesterday.png')

# Box Score 버튼 오프셋 설정 (yesterday.png 이미지의 중심에서부터의 거리)
# 사용자의 해상도나 UI 스케일에 맞춰 이 값을 조정해야 할 수 있습니다.
BOX_SCORE_OFFSET_X = 150 # X축으로 150픽셀 오른쪽으로 이동
BOX_SCORE_OFFSET_Y = 0   # Y축 이동은 없음

# 단축키 설정
AUTOPLAY_HOTKEY = 'f8'
SAVE_HOTKEY = 'f9'
BOX_SCORE_HOTKEY = 'f10'
EXIT_HOTKEY = 'ctrl+q'

# 이미지 인식 정확도
CONFIDENCE_LEVEL = 0.9

def perform_autoplay():
    print(f"'{AUTOPLAY_HOTKEY}' 키 입력: 자동 플레이 시도")
    try:
        pyautogui.moveTo(1, 1, duration=0.1)
        button_location = pyautogui.locateCenterOnScreen(AUTOPLAY_BUTTON_PATH, confidence=CONFIDENCE_LEVEL)
        if button_location:
            pyautogui.moveTo(button_location, duration=0.1)
            pyautogui.sleep(0.1)
            pyautogui.click()
            print("-> 자동 플레이 클릭 성공")
        else:
            print("-> 자동 플레이 버튼을 찾지 못했습니다.")
    except Exception as e:
        print(f"-> 오류 발생: {e}")

def save_game():
    print(f"'{SAVE_HOTKEY}' 키 입력: 게임 저장 시도")
    try:
        # 1. 'File' 버튼 찾기 및 클릭
        file_location = pyautogui.locateCenterOnScreen(FILE_BUTTON_PATH, confidence=CONFIDENCE_LEVEL)
        if not file_location:
            print("-> 'File' 버튼을 찾지 못했습니다.")
            return

        print("-> 'File' 버튼 클릭 중...")
        pyautogui.moveTo(file_location, duration=0.1)
        pyautogui.sleep(0.1)
        pyautogui.click()

        # 2. 1초 대기
        print("-> 1초 대기 중...")
        pyautogui.sleep(0.5)

        # 3. 'Save Game' 버튼 찾기 및 클릭
        search_region = (file_location.x - 100, file_location.y, 200, 300)
        save_location = pyautogui.locateCenterOnScreen(SAVE_BUTTON_PATH, confidence=CONFIDENCE_LEVEL, region=search_region)

        if not save_location:
            print("-> 'Save Game' 버튼을 찾지 못했습니다.")
            return
        
        print("-> 'Save Game' 버튼 클릭 중...")
        pyautogui.moveTo(save_location, duration=0.1)
        pyautogui.sleep(0.1)
        pyautogui.click()
        print("-> 저장 클릭 성공.")

    except Exception as e:
        print(f"-> 게임 저장 중 오류 발생: {e}")

def click_box_score():
    print(f"'{BOX_SCORE_HOTKEY}' 키 입력: Box Score 보기 시도")
    try:
        pyautogui.moveTo(1, 1, duration=0.1)
        # 'YESTERDAY' 이미지 찾기
        yesterday_location = pyautogui.locateCenterOnScreen(YESTERDAY_IMAGE_PATH, confidence=CONFIDENCE_LEVEL)
        if yesterday_location:
            # Box Score 버튼 위치 계산
            box_score_x = yesterday_location.x + BOX_SCORE_OFFSET_X
            box_score_y = yesterday_location.y + BOX_SCORE_OFFSET_Y
            
            print(f"-> 'YESTERDAY' 이미지를 {yesterday_location}에서 찾았습니다.")
            print(f"-> Box Score 버튼 위치를 {box_score_x, box_score_y}(으)로 계산하여 이동합니다.")

            pyautogui.moveTo(box_score_x, box_score_y, duration=0.1)
            pyautogui.sleep(0.1)
            pyautogui.click()
            print("-> Box Score 버튼 클릭 성공")
        else:
            print("-> 'YESTERDAY' 이미지를 찾지 못했습니다.")
    except Exception as e:
        print(f"-> 오류 발생: {e}")

def exit_script():
    print(f"'{EXIT_HOTKEY}' 키 입력: 스크립트를 종료합니다.")
    os._exit(0)

def main():
    print("--- OOTP 단축키 도우미 (v5-portable) ---")
    print(f"- '{AUTOPLAY_HOTKEY}' 키: 자동 플레이")
    print(f"- '{SAVE_HOTKEY}' 키: 게임 저장")
    print(f"- '{BOX_SCORE_HOTKEY}' 키: 어제 경기 Box Score 보기")
    print(f"- '{EXIT_HOTKEY}' 키: 스크립트 종료")
    print("-------------------------------------")
    print("단축키 입력을 기다리는 중...")

    keyboard.add_hotkey(AUTOPLAY_HOTKEY, perform_autoplay)
    keyboard.add_hotkey(SAVE_HOTKEY, save_game)
    keyboard.add_hotkey(BOX_SCORE_HOTKEY, click_box_score)
    keyboard.add_hotkey(EXIT_HOTKEY, exit_script)

    keyboard.wait()

if __name__ == "__main__":
    required_files = [AUTOPLAY_BUTTON_PATH, FILE_BUTTON_PATH, SAVE_BUTTON_PATH, YESTERDAY_IMAGE_PATH]
    missing_files = [f for f in required_files if not os.path.exists(f)]
    if missing_files:
        print("오류: 다음 스크린샷 파일이 없습니다. README.md 파일을 참고하여 이미지 파일을 설정해주세요:")
        for f in missing_files:
            print(f"- {f}")
    else:
        main()
