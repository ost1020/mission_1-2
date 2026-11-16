import json
import os
import random
import sys
import signal
import shutil

# 1. 순수 데이터 모델: 개별 퀴즈를 담당
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer
        
    def display_quiz(self):
        print(f"\nQ. {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

# 2. 컨트롤러: 게임 전체 흐름과 데이터 저장 담당
class QuizGame:
    def __init__(self):
        self.best_score = 0
        self.quiz_list = []
        self.load_data()

    # 데이터가 없을 때 기본 퀴즈를 세팅해주는 메서드 추가
    def set_default_quizzes(self):
        self.quiz_list = [
            Quiz("이번에는 조지가 씻을 차례다를 영어로 하면?", ["조지 워싱턴", "조지 클루니", "폴 조지", "조지아"], 1),
            Quiz("자기 전에 먹는 과자는?", ["맛동산", "포카칩", "눈을 감자", "허니버터칩"], 3),
            Quiz("공이 굴러가면서 하는 말은?", ["공감", "안뇽?", "왔나", "온나~"], 1),
            Quiz("무가 자기소개를 할 때 하는 말은?", ["무서운 이야기", "나무", "무소고기국", "무지렁이"], 2),
            Quiz("쇼핑카트에 만두만 넣으면?", ["왕만두", "군만두", "만두튀김", "카트만두"], 4)
        ]

    def load_data(self):
        if not os.path.exists("state.json"):
            self.set_default_quizzes()
            print("\n안내: 저장된 파일이 없어 기본 퀴즈로 시작해용!")
            return
        
        try:
            with open("state.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.best_score = data.get("best_score", 0)
                
                self.quiz_list = []
                for q in data.get("quizzes", []):
                    self.quiz_list.append(Quiz(q["question"], q["choices"], q["answer"]))
            print("\n📂 저장된 데이터를 성공적으로 불러왔어용!")
            
        except (json.JSONDecodeError, IOError):
            print("원본 데이터가 손상되었습니다. 백업 파일(state_backup.json)에서 복구를 시도합니다...")
            # 백업 파일 존재 시 복구 시도
            if os.path.exists("state_backup.json"):
                try:
                    with open("state_backup.json", "r", encoding="utf-8") as f:
                        data = json.load(f)
                        self.best_score = data.get("best_score", 0)
                        self.quiz_list = []
                        for q in data.get("quizzes", []):
                            self.quiz_list.append(Quiz(q["question"], q["choices"], q["answer"]))
                    # 복구 성공 시 다시 원본으로 덮어써서 완전 복구
                    shutil.copy("state_backup.json", "state.json")
                    print("\n📂 백업 데이터로 성공적으로 복구했어용!")
                    return
                except (json.JSONDecodeError, IOError):
                    print("백업 데이터도 손상되었습니다.")
                    
            # 백업도 없거나 손상되었을 때 최후의 수단
            print("기본 퀴즈로 초기화합니다.")
            self.best_score = 0
            self.set_default_quizzes()

    def save_data(self):
        # 1. 기존 정상 데이터가 있다면 먼저 백업 파일로 복사(보존)해둠
        if os.path.exists("state.json"):
            shutil.copy("state.json", "state_backup.json")
            
        temp_file = "state_temp.json"
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
        
        try:
            # 2. 임시 파일에 쓰기
            with open(temp_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            # 3. 쓰기 완료 후 원본 파일 덮어쓰기 (원자적 저장)
            os.replace(temp_file, "state.json")
        except IOError as e:
            print(f"데이터 저장 중 오류 발생: {e}")

    # 기능 1: 퀴즈 풀기
    def play_quiz(self):
        print("\n--- [퀴즈 게임 시작!] ---")
        if not self.quiz_list:
            print("안내: 풀 수 있는 퀴즈가 없어용! 먼저 퀴즈를 추가해 주세용.")
            return
            
        max_q = len(self.quiz_list) 
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
        
        if score > self.best_score:
            self.best_score = score
            self.save_data()
            print("축하해용! 최고 점수를 갱신했어용! 🏆")

    # 기능 2: 퀴즈 추가
    def add_quiz(self):
        print("\n--- [나만의 퀴즈 추가하기!] ---")
        new_q = input("새로운 넌센스 문제를 입력해 주세용: ").strip()
        if not new_q:
            print("안내: 문제가 비어있어용! 추가가 취소되었어용.")
            return
        
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
        if not self.quiz_list:
            print("안내: 퀴즈가 하나도 없어용! 먼저 추가해 주세용.")
        else:
            for i, quiz in enumerate(self.quiz_list, 1):
                print(f"{i}. {quiz.question}")
        input("\n목록을 다 확인했으면 엔터(Enter)를 눌러서 돌아가세용! ↵")

    # 기능 4: 퀴즈 삭제
    def delete_quiz(self):
        print("\n--- [퀴즈 삭제하기 🗑️] ---")
        if not self.quiz_list:
            print("안내: 삭제할 퀴즈가 하나도 없어용!")
            return
            
        for i, quiz in enumerate(self.quiz_list, 1):
            print(f"{i}. {quiz.question}")
            
        while True:
            try:
                del_input = input("\n삭제할 퀴즈 번호를 입력해 주세용 (취소는 0): ").strip()
                if not del_input:
                    continue
                del_num = int(del_input)
                
                if del_num == 0:
                    print("삭제를 취소했어용.")
                    break
                    
                if 1 <= del_num <= len(self.quiz_list):
                    deleted_quiz = self.quiz_list.pop(del_num - 1)
                    self.save_data()
                    print(f"'{deleted_quiz.question}' 문제가 성공적으로 삭제되었어용! 👏")
                    break
                else:
                    print(f"안내: 1에서 {len(self.quiz_list)} 사이의 번호를 골라주세용.")
            except ValueError:
                print("안내: 숫자가 아니에용! 정확한 번호를 입력해 줘용.")

    # 기능 5: 최고 점수 확인
    def show_score(self):
        print(f"\n현재까지의 최고 점수는 {self.best_score}점이에용! 🏆")
        input("\n목록을 다 확인했으면 엔터(Enter)를 눌러서 돌아가세용! ↵")
    
    # 게임 메인 루프
    def run(self):
        while True:
            print("\n=== 🤯 넌센스 퀴즈 게임 ===")
            print("1. 퀴즈를 풀어볼래용!")
            print("2. 퀴즈를 추가할래용!")
            print("3. 퀴즈 목록을 확인할래용!")
            print("4. 퀴즈를 삭제할래용! 🗑️")
            print("5. 점수를 알려줘용!")
            print("6. 종료할래용!")
            
            try:
                choice = int(input("메뉴를 선택해 줘용 (1~6): ").strip())
                
                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_list()
                elif choice == 4:
                    self.delete_quiz()
                elif choice == 5:
                    self.show_score()
                elif choice == 6:
                    self.save_data()
                    print("\n게임을 종료할게용. 수고했어용!")
                    break
                else:
                    print("안내: 1에서 6 사이의 숫자만 입력할 수 있어용.")
            except ValueError:
                print("안내: 숫자가 아니에용! 정확한 메뉴 번호를 입력해 줘용.")

# 3. 프로그램 실행 스위치
if __name__ == "__main__":
    game = QuizGame()
    
    # FAIL #11 보완: SIGINT(Ctrl+C)/SIGTERM 인터럽트 발생 시 안전 종료 처리
    def signal_handler(sig, frame):
        print("\n프로그램을 강제 종료합니다. 데이터를 안전하게 저장 중...")
        game.save_data()
        sys.exit(0)
        
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    game.run()