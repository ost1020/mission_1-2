import json  # 나중에 state.json 파일 저장을 위해 쓸 부품이야!

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display_quiz(self):
        print(f"\nQ. {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")
            
class QuizGame:
    def __init__(self):
        # 기존 main()에 있던 바구니와 명예의 전당이 이리로 이사 왔어!
        self.quiz_list = [
            Quiz("이번에는 조지가 씻을 차례다를 영어로 하면?", ["조지 워싱턴", "조지 클루니", "폴 조지", "조지아"], 1),
            Quiz("자기 전에 먹는 과자는?", ["맛동산", "포카칩", "눈을 감자", "허니버터칩"], 3),
            Quiz("공이 굴러가면서 하는 말은?", ["공감", "안뇽?", "왔나", "온나~"], 1),
            Quiz("무가 자기소개를 할 때 하는 말은?", ["무서운 이야기", "나무", "무소고기국", "무지렁이"], 2),
            Quiz("쇼핑카트에 만두만 넣으면?", ["왕만두", "군만두", "만두튀김", "카트만두"], 4)
        ]
        self.best_score = 0

        # 기능 1: 퀴즈 풀기
    def play_quiz(self):
        print("\n--- [퀴즈 게임 시작!] ---")
        score = 0 
        
        for quiz in self.quiz_list:  # self. 붙음!
            quiz.display_quiz() 
            
            while True:
                try:
                    ans_input = input("정답 번호를 입력해 주세용 (1-4): ").strip()
                    if not ans_input:
                        print("안내: 정답을 입력해 줘용!")
                        continue
                        
                    user_answer = int(ans_input)
                    
                    if 1 <= user_answer <= len(quiz.choices):
                        break  
                    else:
                        print(f"안내: 1에서 {len(quiz.choices)} 사이의 번호만 골라주세용.")
                except ValueError:
                    print("안내: 숫자가 아니에용! 번호로 입력해 줘용.")
                    
            if user_answer == quiz.answer:
                print("정답이에용! 🎉")
                score += 10  
            else:
                print(f"땡! 틀렸어용. 정답은 {quiz.answer}번이에용. 😅")
                
        print(f"\n게임 끝! 이번 판의 점수는 {score}점이에용!")
        
        if score > self.best_score:  # self. 붙음!
            self.best_score = score
            print("축하해용! 최고 점수를 갱신했어용! 🏆")

    # 기능 2: 퀴즈 추가
    def add_quiz(self):
        print("\n--- [나만의 퀴즈 추가하기!] ---")
        new_q = input("새로운 넌센스 문제를 입력해 주세용: ").strip()
        if not new_q:
            print("안내: 문제가 비어있어용! 추가가 취소되었어용.")
            return  # 루프 안이 아니라 함수 안이므로 continue 대신 return으로 빠져나감!
        
        new_choices = []
        for i in range(1, 5):
            c = input(f"{i}번 보기를 입력해 주세용: ").strip()
            if not c:
                c = f"기본 보기 {i}"
            new_choices.append(c)
        
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
        
        self.quiz_list.append(Quiz(new_q, new_choices, new_ans)) # self. 붙음!
        print("\n성공적으로 퀴즈가 추가되었어용! 👏")

    # 기능 3: 퀴즈 목록
    def show_list(self):
        print("\n--- [현재 퀴즈 목록이에용!] ---")
        if not self.quiz_list: # self. 붙음!
            print("안내: 퀴즈가 하나도 없어용! 먼저 추가해 주세용.")
        else:
            for i, quiz in enumerate(self.quiz_list, 1): # self. 붙음!
                print(f"{i}. {quiz.question}")

    # 기능 4: 점수 확인
    def show_score(self):
        print(f"\n현재까지의 최고 점수는 {self.best_score}점이에용! 🏆") # self. 붙음!

    # 게임 전체를 굴리는 메인 모터 (기존 while True 역할)
    def run(self):
        while True:
            print("\n=== 🤯 넌센스 퀴즈 게임 ===")
            print("1. 퀴즈를 풀어볼래용!")
            print("2. 퀴즈를 추가할래용!")
            print("3. 퀴즈 목록을 확인할래용!")
            print("4. 점수를 알려줘용!")
            print("5. 종료할래용!")
            
            try:
                choice = int(input("메뉴를 선택해 줘용 (1~5): ").strip())
                
                if choice == 1:
                    self.play_quiz()  # 자기가 가진 play_quiz 버튼을 누름!
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_list()
                elif choice == 4:
                    self.show_score()
                elif choice == 5:
                    print("\n게임을 종료할게용. 수고했어용!")
                    break
                else:
                    print("안내: 1에서 5 사이의 숫자만 입력할 수 있어용.")
            except ValueError:
                print("안내: 숫자가 아니에용! 정확한 메뉴 번호를 입력해 줘용.")

# ==========================================
# 3. 프로그램 실행 스위치
# ==========================================
if __name__ == "__main__":
    game = QuizGame()  # 게임 매니저 객체 생성!
    game.run()         # 매니저 일 시작해!