import json
import os
import random

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
        self.load_data()

        # 기능 1: 퀴즈 풀기
    def play_quiz(self):
        print("\n--- [퀴즈 게임 시작!] ---")
        
        if not self.quiz_list:
            print("안내: 풀 수 있는 퀴즈가 없어용! 먼저 퀴즈를 추가해 주세용.")
            return
            
        # --- [새로 추가된 구역: 풀 문제 개수 입력받기 방어막] ---
        max_q = len(self.quiz_list) # 현재 바구니에 있는 총 문제 수
        while True:
            try:
                num_input = input(f"몇 문제를 풀래용? (1~{max_q}): ").strip()
                if not num_input:
                    continue
                num_q = int(num_input)
                if 1 <= num_q <= max_q:
                    break
                else:
                    print(f"안내: 1에서 {max_q} 사이의 숫자만 입력해주세용.")
            except ValueError:
                print("안내: 숫자가 아니에용! 숫자로 입력해 줘용.")
        # --------------------------------------------------------

        # 제비뽑기 기계: 전체 개수(len) 대신, 방금 입력받은 숫자(num_q)만큼만 뽑기!
        play_list = random.sample(self.quiz_list, num_q)
        
        score = 0 
        
        for quiz in play_list: 
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
            self.save_data()
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
        
        self.quiz_list.append(Quiz(new_q, new_choices, new_ans))
        self.save_data()
        print("\n성공적으로 퀴즈가 추가되었어용! 👏")

    # 기능 3: 퀴즈 목록
    def show_list(self):
        print("\n--- [현재 퀴즈 목록이에용!] ---")
        if not self.quiz_list: # self. 붙음!
            print("안내: 퀴즈가 하나도 없어용! 먼저 추가해 주세용.")
        else:
            for i, quiz in enumerate(self.quiz_list, 1): # self. 붙음!
                print(f"{i}. {quiz.question}")
        input("\n목록을 다 확인했으면 엔터(Enter)를 눌러서 돌아가세용! ↵")

    # 기능 4: 최고 점수 확인
    def show_score(self):
        print(f"\n현재까지의 최고 점수는 {self.best_score}점이에용! 🏆") # self. 붙음!
        input("\n목록을 다 확인했으면 엔터(Enter)를 눌러서 돌아가세용! ↵")
    
    # 기능 5: 데이터 불러오기 엔진
    def load_data(self):
        if os.path.exists("state.json"): # state.json 파일이 컴퓨터에 있는지 확인!
            with open("state.json", "r", encoding="utf-8") as f:
                data = json.load(f) # json 파일 안의 데이터를 파이썬 딕셔너리로 싹 변환해 줘.
                
                self.best_score = data.get("best_score", 0) # 명예의 전당 복구!
                
                # 기존 퀴즈 Ба구니 비우고 파일에 있는 걸로 다시 꽉 채우기
                self.quiz_list = []
                for q in data.get("quizzes", []):
                    self.quiz_list.append(Quiz(q["question"], q["choices"], q["answer"]))
            print("\n📂 저장된 데이터를 성공적으로 불러왔어용!")
        # 파일이 없으면 아무 일도 안 함 (기본 퀴즈 5개로 알아서 시작됨)

    # 기능 6: 데이터 파일로 저장하기 엔진
    def save_data(self):
        # json 파일에 넣기 좋게 딕셔너리 형태로 싹 다 정리해
        data = {
            "best_score": self.best_score,
            "quizzes": []
        }
        for quiz in self.quiz_list:
            data["quizzes"].append({
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer
            })
        
        # state.json 파일에 덮어쓰기 모드("w")로 콱 저장해버리기!
        with open("state.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # 게임 전체를 굴리는 메인 모터 (기존 while True 역할)
    def run(self):
        while True:
            print("\n=== 🤯 넌센스 퀴즈 게임 ===")
            print("1. 퀴즈를 풀어볼래용!")
            print("2. 퀴즈를 추가할래용!")
            print("3. 퀴즈 목록을 확인할래용!")
            print("4. 퀴즈를 삭제할래용! 🗑️")  # 새로 추가!
            print("5. 점수를 알려줘용!")
            print("6. 종료할래용!")
            
            try:
                choice = int(input("메뉴를 선택해 줘용 (1~6): ").strip())
                
                if choice == 1:
                    self.play_quiz()  # 자기가 가진 play_quiz 버튼을 누름!
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_list()
                elif choice == 4:
                    self.delete_quiz() # 방금 만든 삭제 리모컨 찰칵!
                elif choice == 5:
                    self.show_score()
                elif choice == 6:
                    self.save_data()  # <--- 이 줄 추가!
                    print("\n게임을 종료할게용. 수고했어용!")
                    break

                else:
                    print("안내: 1에서 6 사이의 숫자만 입력할 수 있어용.")
            except ValueError:
                print("안내: 숫자가 아니에용! 정확한 메뉴 번호를 입력해 줘용.")
        
    def delete_quiz(self):
        print("\n--- [퀴즈 삭제하기 🗑️] ---")
        # 1. Falsy 특성을 이용한 빈 바구니 검사
        if not self.quiz_list:
            print("안내: 삭제할 퀴즈가 하나도 없어용!")
            return
            
        # 2. enumerate로 번호표 달아서 보여주기
        for i, quiz in enumerate(self.quiz_list, 1):
            print(f"{i}. {quiz.question}")
            
        # 3. 좁게 설정한 안전 방어막 (지뢰 탐지기)
        while True:
            try:
                del_input = input("\n삭제할 퀴즈 번호를 입력해 주세용 (취소는 0): ").strip()
                if not del_input:
                    continue
                    
                del_num = int(del_input)
                
                # 취소 로직
                if del_num == 0:
                    print("삭제를 취소했어용.")
                    break
                    
                # 입력 번호가 유효한 인덱스 범위 안에 있는지 확인
                if 1 <= del_num <= len(self.quiz_list):
                    deleted_quiz = self.quiz_list.pop(del_num - 1)
                    self.save_data()  # <--- 메모리에서 지운 후 파일에도 덮어쓰기 완료!
                    print(f"'{deleted_quiz.question}' 문제가 성공적으로 삭제되었어용! 👏")
                    break
                else:
                    print(f"안내: 1에서 {len(self.quiz_list)} 사이의 번호를 골라주세용.")
                    
            except ValueError:
                print("안내: 숫자가 아니에용! 정확한 번호를 입력해 줘용.")

# ==========================================
# 3. 프로그램 실행 스위치
# ==========================================
if __name__ == "__main__":
    game = QuizGame()  # 게임 매니저 객체 생성!
    game.run()         # 매니저 일 시작해!