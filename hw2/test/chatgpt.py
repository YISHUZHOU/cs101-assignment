import random


# 定义一个函数，这个函数会输出一个趣味游戏
def funny_game():
    print("\n欢迎来到趣味游戏！")
    print("请选择你想玩的游戏：")
    print("1. 猜数字游戏")
    print("2. 猜字母游戏")
    print("3. 猜文字游戏")

    choice = input("请输入游戏序号：")
    if choice == "1":
        print("\n开始猜数字游戏，让我们来猜一个1~100的数字")
        number = random.randint(1, 100)
        guess = int(input("请输入你猜的数字："))
        while guess != number:
            if guess < number:
                print("你猜的数字太小了，请重新猜：")
            elif guess > number:
                print("你猜的数字太大了，请重新猜：")
            guess = int(input())
        print("恭喜你，答对了！")
    elif choice == "2":
        print("\n开始猜字母游戏，让我们来猜一个A~Z的字母")
        letter = chr(random.randint(ord("A"), ord("Z")))
        guess = input("请输入你猜的字母：")
        while guess != letter:
            print("你猜的字母不对，请重新猜：")
            guess = input()
        print("恭喜你，答对了！")
    elif choice == "3":
        print("\n开始猜文字游戏，让我们来猜一个字符串")
        words = "Hello World"
        guess = input("请输入你猜的字符串：")
        while guess != words:
            print("你猜的字符串不对，请重新猜：")
            guess = input()
            print("恭喜你，答对了！")

    # 调用函数


funny_game()
