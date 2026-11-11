def main():
    while True:
        print("\n=== 🤯 넌센스 퀴즈 게임 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        
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
                print("\n[퀴즈 풀기 기능] - 아직 준비 중이에용!")
            elif choice == 2:
                print("\n[퀴즈 추가 기능] - 아직 준비 중에용!")
            elif choice == 3:
                print("\n[퀴즈 목록 기능] - 아직 준비 중에용!")
            elif choice == 4:
                print("\n[점수 확인 기능] - 아직 준비 중에용!")
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

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display_quiz(self):
        print(f"\nQ. {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")
