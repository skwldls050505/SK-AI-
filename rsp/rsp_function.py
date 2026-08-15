import enum
import random


class rsp(enum.Enum): #
    가위 = 0
    바위 = 1
    보 = 2



def rsp_result(user: str, computer: str) -> int: # 결과는 따로 빼자 ! 하나빼기랑 가위바위보, 묵찌빠 공통으로 사용함
    result = (rsp[user].value - rsp[computer].value) % 3

    if result == 1: # 승
        return 1
    
    elif result == 0: # 무 
        return 0
    
    else:
        return -1 # ㅍㅐ


def game_rsp(user: str) -> str: # 가위바위보 게임

    assert user in rsp.__members__, "잘못 입력했습니다." # 오류 발생

    computer = random.choice(list(rsp.__members__)) # 컴퓨터 
    result = rsp_result(user, computer) # 결과 저장

    if result == 1:
        print(f"사용자 입력: {user}, 컴퓨터 입력: {computer} >> 사용자가 이겼습니다 !!")
        return "사용자 승"
    elif result == 0:
        print(f"사용자 입력: {user}, 컴퓨터 입력: {computer} >> 비겼습니다 !!")
        return "무승부"
    else:
        print(f"사용자 입력: {user}, 컴퓨터 입력: {computer} >> 사용자가 졌습니다 !!")
        return "사용자 패"


def game_hana(user: list[str] = ["가위", "바위"]) -> str: # 하나빼기

    assert len(user) == 2, "두 개를 입력해야 합니다."
    assert user[0] in rsp.__members__ and user[1] in rsp.__members__, "잘못 입력했습니다." # 오류 발생

    computer = [
        random.choice(list(rsp.__members__)),
        random.choice(list(rsp.__members__))
    ]

    print("사용자 :", user)
    print("컴퓨터 :", computer)

    while True:
        try:
            choice = int(input(f"남길 손(번호)을 선택하세요. 1 : ({user[0]}) / 2 : ({user[1]}) "))
            if choice in (1, 2):
                break
            print("1 또는 2만 입력해주세요.")
        except ValueError:
            print("숫자만 입력해주세요.")

    user_final = user[choice - 1] # 고른 리스트 인덱스 저장
    computer_final = random.choice(computer) # 컴퓨터도 랜덤으로 초이스

    result = rsp_result(user_final, computer_final) # 결과 가지고 다시 가위바위보

    print(f"최종 선택 >> 사용자: {user_final} / 컴퓨터: {computer_final}")

    if result == 1:
        print("사용자 승!")
        return "사용자 승"
    
    elif result == 0:
        print("무승부!")
        return "무승부"
    
    else:
        print("사용자 패!")
        return "사용자 패"


def game_mjb() -> dict: #묵찌빠


    mjb_to_rsp = {
        "묵": "바위",
        "찌": "가위",
        "빠": "보"
    }

    print("먼저 가위바위보 부터 !")

    # 1. 가위바위보로 첫 공격자 결정
    while True:
        first_user = input("가위, 바위, 보 중 하나를 입력하세요 : ").strip()

        if first_user not in rsp.__members__: # 입력 오류
            print("가위, 바위, 보 중에서 입력해주세요.")
            continue

        first_rsp = game_rsp(first_user) # 첫번째 가위바위보 실행

        if first_rsp == "무승부":
            continue

        # 1은 사용자 공격 / 0은 사용자 방어
        state = {
            "user_attack": first_rsp == "사용자 승",
            "game_over": False,
            "winner": None
        }
        break

    # 2. 묵찌빠 진행
    # 로직 생각 
    # 1 - 1차 가위바위보 , 2 - 결과에 따라 사용자가 공격인지/컴퓨터가 공격인지 상태
    # 사용자가 공격이면 user_attack 사용자로
    # 묵/찌/빠 중에 선택 (컴퓨터도 랜덤으로 묵/찌/빠 중에 초이스) - 다시 복원
    # 사용자, 컴퓨터 묵찌빠 가지고 다시 가위바위보 함수 돌려서 결과 
    # 이걸 while 문 안에 돌리자
    # game_over 상태값도 하나 만들어서 True면 break

    # 강사님이 상태는 딕셔너리로 생각
    # boolean 사용

    while not state["game_over"]:
        print()
        print(f"현재 상태값 : {state}")
        

        if state["user_attack"]:
            print("현재 사용자 공격입니다!")
        else:
            print("현재 사용자 방어입니다!")

        user_mjb = input("묵, 찌, 빠 중 하나를 입력하세요 : ").strip()

        if user_mjb not in mjb_to_rsp:
            print("묵, 찌, 빠 중에서 입력해주세요.")
            continue

        computer_mjb = random.choice(list(mjb_to_rsp.keys()))
        
        print(f"사용자 : {user_mjb} / 컴퓨터 : {computer_mjb}")

        # 같은 것을 냈다면 현재 공격자가 승리
        if user_mjb == computer_mjb:
            if state["user_attack"]:
                state["winner"] = "사용자"
            else:
                state["winner"] = "컴퓨터"

            state["game_over"] = True
            break

        # 서로 다르면 가위바위보 승자가 다음 공격자
        user_rsp = mjb_to_rsp[user_mjb]
        computer_rsp = mjb_to_rsp[computer_mjb]
        result = rsp_result(user_rsp, computer_rsp)

        if result == 1:
            state["user_attack"] = True
            print("사용자가 이겼으므로 사용자 공격으로 변경!")
        else:
            state["user_attack"] = False
            print("컴퓨터가 이겼으므로 사용자 방어로 변경!")


    print(f"승자 : {state['winner']}")
    print(f"최종 상태값 : {state}")

    return state
