from tkinter import *
import clipboard

###예제4) ft -> cm로 바꾸는 단위 변환기 만들기
# Entry: input과 비슷한 역할 (사용자가 입력한 내용 전달)
# get: Entry를 사용한 입력 내용 가져올 수 있다.
# delete: 사용자 입력 삭제
# Frame: 컨테이너, 창 안에 프레임 생성
# grid: 격자 배치
tk = Tk()
tk.title('Message Encrypter/Decrypter 1')
tk.configure()

def Encrypt():
    passwd = entry1.get()
    passwd_s = "" # 암호화한 비밀번호 저장
    passwd2 = "" # 복호화한 암호, 첫번째 비밀번호랑 같은지 확인할 것.
    c = '' # 문자 하나 따오기
    ac = 0 # ASCII code 로 변환
    for i in range(len(passwd)) :
        c = passwd[i]   # 개별 문자
        ac = ord(c)     # 개별 문자의 아스키 코드
        ac += 2         # 개별 아스키 코드 값 2 증가
        c = chr(ac)     # 아스키 코드를 문자로 변환
        passwd_s += c   # 변환된(암호화 한) 암호 저장
    entry2.delete(0,"end")
    entry2.insert(0, passwd_s)

def Copy():
    clipboard.copy(entry2.get())

label0 = Label(tk,text='Encrypt: ').grid(row=0, column=0)
label1 = Label(tk,text='Please enter your words here: ').grid(row=1, column=0)
label2 = Label(tk,text='This is your encrypted key: ').grid(row=2,column=0)

# 각 단위 입력받는 부분 만들기
entry1 = Entry(tk)
entry2 = Entry(tk)

btncopy01 = Button(tk, text='Copy',bg='black',fg='white',command=Copy).grid(row=2, column=2)

entry1.grid(row=1,column=1)
entry2.grid(row=2,column=1)

btn1 = Button(tk,text='Encrypt',bg='black',fg='white',command=Encrypt).grid(row=3,column=0)

def Decrypt():
    passwd = entry3.get()
    passwd_s = "" # 암호화한 비밀번호 저장
    passwd2 = "" # 복호화한 암호, 첫번째 비밀번호랑 같은지 확인할 것.
    c = '' # 문자 하나 따오기
    ac = 0 # ASCII code 로 변환
    for i in range(len(passwd)) :
        c = passwd[i] # 개별 문자
        ac = ord(c)     # 개별 문자의 아스키 코드
        ac -= 2         # 개별 아스키 코드 값 2 감소
        c = chr(ac)     # 아스키 코드를 문자로 변환
        passwd2 += c    # 변환된(복호화 한) 암호 저장
    entry4.delete(0,"end")
    entry4.insert(0, passwd2)

def Copy2():
    clipboard.copy(entry4.get())

labelq = Label(tk,text=' ').grid(row=4, column=0)
label3 = Label(tk,text='Decrypt: ').grid(row=5, column=0)
label4 = Label(tk,text='Please enter your encrypted key: ').grid(row=6, column=0)
label5 = Label(tk,text='Your decrypted key is: ').grid(row=7,column=0)

# 각 단위 입력받는 부분 만들기
entry3 = Entry(tk)
entry4 = Entry(tk)

btncopy02 = Button(tk, text='Copy',bg='black',fg='white',command=Copy2).grid(row=7, column=2)

entry3.grid(row=6,column=1)
entry4.grid(row=7,column=1)

btn1 = Button(tk,text='Decrypt',bg='black',fg='white',command=Decrypt).grid(row=8,column=0)
label6 = Label(tk,text=' ').grid(row=9,column=0)
label7 = Label(tk,text='You are using En/decrypter 1.').grid(row=10,column=0)

tk.mainloop()