import csv
import os
import random  # 랜덤 순서로 퀴즈를 출제하기 위해 추가

# 파일 경로 설정
FILE_PATH = 'words.csv'

# 파일 초기화
def init_file():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['word', 'meaning', 'attempts', 'correct_attempts'])

# 단어 추가
def add_word(word, meaning):
    with open(FILE_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([word, meaning, 0, 0])

# 단어 목록 불러오기
def list_words():
    words = []
    with open(FILE_PATH, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # 헤더 스킵
        for row in reader:
            words.append(row)
    return words

# 텍스트 아트로 축하 메시지 출력
def show_congratulations():
    print("""
  ##    ##   #  #   ##   ###    ##  #####  #  #  #      ##  #####  ###    ##   #  #   ##  
 #  #  #  #  ## #  #  #  #  #  #  #   #    #  #  #     #  #   #     #    #  #  ## #  #  # 
 #     #  #  ## #  #     #  #  #  #   #    #  #  #     #  #   #     #    #  #  ## #  #    
 #     #  #  # ##  # ##  ###   ####   #    #  #  #     ####   #     #    #  #  # ##   ##  
 #     #  #  # ##  #  #  # #   #  #   #    #  #  #     #  #   #     #    #  #  # ##     # 
 #  #  #  #  #  #  #  #  #  #  #  #   #    #  #  #     #  #   #     #    #  #  #  #  #  # 
  ##    ##   #  #   ###  #  #  #  #   #     ##   ####  #  #   #    ###    ##   #  #   ##  
    """)

# 랜덤 순서로 전체 단어 퀴즈
def quiz_random():
    words = list_words()
    if not words:
        print("저장된 단어가 없습니다. 단어를 추가해 주세요.")
        return
    
    all_correct = True  # 모든 단어를 맞췄는지 추적

    random.shuffle(words)  # 단어 목록을 랜덤하게 섞기
    
    for word_data in words:
        word, meaning, attempts, correct_attempts = word_data
        attempts = int(attempts)
        correct_attempts = int(correct_attempts)

        print(f"\n단어: {word}")
        user_answer = input("뜻을 입력하세요: ")
        
        if user_answer.strip().lower() == meaning.lower():
            print("정답입니다!")
            correct_attempts += 1
        else:
            print(f"틀렸습니다. 정답은: {meaning}")
            all_correct = False  # 틀린 단어가 있을 경우 False로 설정
        
        attempts += 1
        update_word(word, attempts, correct_attempts)
    
    # 모든 단어를 맞춘 경우 축하 메시지 출력
    if all_correct:
        show_congratulations()

# 단어 업데이트
def update_word(target_word, attempts, correct_attempts):
    words = list_words()
    with open(FILE_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['word', 'meaning', 'attempts', 'correct_attempts'])
        for word, meaning, prev_attempts, prev_correct_attempts in words:
            if word == target_word:
                writer.writerow([word, meaning, attempts, correct_attempts])
            else:
                writer.writerow([word, meaning, prev_attempts, prev_correct_attempts])

# 프로그램 실행
def main():
    init_file()
    
    while True:
        print("\n단어 암기 프로그램")
        print("1. 단어 추가")
        print("2. 단어 목록 보기")
        print("3. 모든 단어 퀴즈")
        print("4. 랜덤 순서 퀴즈")
        print("5. 복습할 단어 추천")
        print("6. 단어 수정")
        print("7. 종료")
        
        choice = input("선택하세요: ")
        
        if choice == '1':
            word = input("단어를 입력하세요: ")
            meaning = input("뜻을 입력하세요: ")
            add_word(word, meaning)
            print("단어가 추가되었습니다.")
        
        elif choice == '2':
            words = list_words()
            if words:
                print("\n단어 목록:")
                for word, meaning, attempts, correct_attempts in words:
                    print(f"- {word}: {meaning} (시도 횟수: {attempts}, 정답 횟수: {correct_attempts})")
            else:
                print("저장된 단어가 없습니다.")
        
        elif choice == '3':
            quiz_all()
        
        elif choice == '4':
            quiz_random()
        
        elif choice == '5':
            review()
        
        elif choice == '6':
            target_word = input("수정할 단어를 입력하세요: ")
            new_word = input("새 단어를 입력하세요: ")
            new_meaning = input("새 뜻을 입력하세요: ")
            edit_word(target_word, new_word, new_meaning)
        
        elif choice == '7':
            print("프로그램을 종료합니다.")
            break
        
        else:
            print("잘못된 입력입니다. 다시 선택해 주세요.")

if __name__ == '__main__':
    main()
