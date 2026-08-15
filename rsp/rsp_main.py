import rsp_function as rsp_function


def main():
    while True:
        try:
            game_input = int(input(
                "\n원하는 게임을 입력하세요 :\n"
                "1 : 가위바위보\n"
                "2 : 하나빼기\n"
                "3 : 묵찌빠\n"
                "4 : 종료\n"
                ">> "
            ))
        except ValueError:
            print("숫자만 입력해주세요.")
            continue

        if game_input == 1:
            rsp_user_input = input(">> 가위, 바위, 보 중에 입력하세요 : ").strip()
            rsp_function.game_rsp(rsp_user_input)


        elif game_input == 2:
            hana_user_input = [
                value.strip()
                for value in input(">> 가위, 바위, 보 중 두 개를 입력하세요 (예: 가위, 바위) : ")
                .split(",")
            ]
            rsp_function.game_hana(hana_user_input)

        elif game_input == 3:
            rsp_function.game_mjb()

        elif game_input == 4:
            print("게임을 종료합니다.")
            break

        else:
            print("1~4 중에서 입력해주세요.")


if __name__ == "__main__":
    main()
