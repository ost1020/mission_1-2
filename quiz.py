class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display_quiz(self):
        print(f"\nQ. {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

def main():
    quiz_list = [
        Quiz("'이번에는 조지가 씻을 차례다를 영어로 하면?'", ["조지 워싱턴", "조지 클루니", "폴 조지", "조지아"], 1),
        Quiz("자기 전에 먹는 과자는?", ["맛동산", "포카칩", "눈을 감자", "허니버터칩"], 3),
        Quiz("공이 굴러가면서 하는 말은?", ["공감", "안뇽?", "왔나", "온나~"], 1),
        Quiz("무가 자기소개를 할 때 하는 말은?", ["무서운 이야기", "나무", "무소고기국", "무지렁이"], 2),
        Quiz("쇼핑카트에 만두만 넣으면?", ["왕만두", "군만두", "만두튀김", "카트만두"], 4)
    ]
    best_score = 0

    while True:
        print("\n=== 🤯 넌센스 퀴즈 게임 ===")
        print("1. 퀴즈를 풀어볼래용!")
        print("2. 퀴즈를 추가할래용!")
        print("3. 퀴즈 목록을 확인할래용!")
        print("4. 점수를 알려줘용!")
        print("5. 종료할래용!")
        
        try:
            # 1. 입력 앞뒤 공백 제거
            choice_input = input("메뉴를 선택해 줘용 (1~5): ").strip()
            
            # 2. 빈 입력(그냥 Enter) 처리
            if not choice_input:
                print("안내: 값이 입력되지 않았어용. 다시 선택해 줘용!")
                continue
                
            # 3. 숫자 변환 시도 (문자 입력 시 여기서 ValueError 발생)
            choice = int(choice_input)
            
            # 4. 허용 범위(1~5) 처리 및 기능 분기
            if choice == 1:
                print("\n--- [퀴즈 게임 시작!] ---")
                score = 0  # 이번 판의 점수 기록장
                
                # quiz_list 바구니에서 붕어빵(퀴즈)을 하나씩 꺼내기
                for quiz in quiz_list:
                    quiz.display_quiz()  # 아까 만든 화면 출력 리모컨 찰칵!
                    
                    # 번호를 똑바로 입력할 때까지 못 빠져나가는 '미니 무한 루프'
                    while True:
                        try:
                            ans_input = input("정답 번호를 입력해 주세용 (1-4): ").strip()
                            if not ans_input:
                                print("안내: 정답을 입력해 줘용!")
                                continue
                                
                            user_answer = int(ans_input)
                            
                            # 보기가 4개면 1~4 사이인지 확인
                            if 1 <= user_answer <= len(quiz.choices):
                                break  # 올바른 번호면 미니 루프 탈출! (다음 단계로)
                            else:
                                print(f"안내: 1에서 {len(quiz.choices)} 사이의 번호만 골라주세용.")
                        except ValueError:
                            print("안내: 숫자가 아니에용! 번호로 입력해 줘용.")
                            
                    # 루프를 탈출했으니 이제 정답을 채점할 시간!
                    if user_answer == quiz.answer:
                        print("정답이에용! 🎉")
                        score += 10  # 정답이면 10점 추가
                    else:
                        print(f"땡! 틀렸어용. 정답은 {quiz.answer}번이에용. 😅")
                        
                # for문이 다 끝나서 퀴즈 5개를 다 풀고 나면 실행됨
                print(f"\n게임 끝! 이번 판의 점수는 {score}점이에용!")
                
                # 최고 점수(best_score) 갱신
                if score > best_score:
                    best_score = score
                    print("축하해용! 최고 점수를 갱신했어용! 🏆")
            elif choice == 2:
                print("\n--- [나만의 퀴즈 추가하기!] ---")
                
                # 1. 문제 입력받기
                new_q = input("새로운 넌센스 문제를 입력해 주세용: ").strip()
                if not new_q:
                    print("안내: 문제가 비어있어용! 추가가 취소되었어용.")
                    continue
                
                # 2. 보기 4개 입력받기 (리스트 바구니에 차곡차곡 넣기)
                new_choices = []
                for i in range(1, 5):
                    c = input(f"{i}번 보기를 입력해 주세용: ").strip()
                    # 만약 보기를 안 적으면 기본값으로 대체 (에러 방지)
                    if not c:
                        c = f"기본 보기 {i}"
                    new_choices.append(c)
                
                # 3. 정답 번호 입력받기 (미니 방어막)
                while True:
                    try:
                        new_ans_input = input("정답 번호를 입력해 주세용 (1-4): ").strip()
                        if not new_ans_input:
                            continue
                            
                        new_ans = int(new_ans_input)
                        
                        if 1 <= new_ans <= 4:
                            break
                        else:
                            print("안내: 1에서 4 사이의 번호만 정답이 될 수 있어용.")
                    except ValueError:
                        print("안내: 숫자가 아니에용! 번호로 입력해 줘용.")
                
                # 4. 새로운 붕어빵(Quiz 객체)을 구워서 기존 바구니(quiz_list)에 밀어 넣기!
                quiz_list.append(Quiz(new_q, new_choices, new_ans))
                print("\n성공적으로 퀴즈가 추가되었어용! 👏")
            elif choice == 3:
                print("\n--- [현재 퀴즈 목록이에용!] ---")
                if not quiz_list:
                    print("안내: 퀴즈가 하나도 없어용! 먼저 추가해 주세용.")
                else:
                    # quiz_list 바구니에서 문제(question)만 번호표 달아서 뽑아내기
                    for i, quiz in enumerate(quiz_list, 1):
                        print(f"{i}. {quiz.question}")
                        
            elif choice == 4:
                # 명예의 전당 전광판(best_score) 그대로 띄워주기
                print(f"\n현재까지의 최고 점수는 {best_score}점이에용! 🏆")

            elif choice == 5:
                print("\n게임을 종료할게용. 수고했어용!")
                break
            else:
                print("안내: 1에서 5 사이의 숫자만 입력할 수 있어용.")
                
        # 5. 숫자 변환 실패(예: abc) 예외 처리
        except ValueError:
            print("안내: 숫자가 아니에용! 정확한 메뉴 번호를 입력해 줘용.")
            
        # 6. 강제 종료(Ctrl+C 등) 예외 처리
        except (KeyboardInterrupt, EOFError):
            print("\n\n안내: 비정상 종료 감지! 데이터를 안전하게 저장하고 종료할게용. (저장 기능 구현 예정)")
            break

if __name__ == "__main__":
    main()
