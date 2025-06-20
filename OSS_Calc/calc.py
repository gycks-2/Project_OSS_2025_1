import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""
        self.result_displayed = False # 계산 결과가 화면에 표시되었는지 여부를 추적

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['%', '='] # '%' 버튼 유지
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            self.result_displayed = False
        elif char == '=':
            try:
                # '=' 버튼이 눌렸을 때는 일반적인 수식 계산 수행
                # % 버튼이 이미 값을 반환했으므로, 여기서는 % 처리를 하지 않습니다.
                result = str(eval(self.expression))
                self.expression = result
                self.result_displayed = True
            except ZeroDivisionError:
                self.expression = "0으로 나눌 수 없음"
                self.result_displayed = True
            except SyntaxError:
                self.expression = "잘못된 수식"
                self.result_displayed = True
            except Exception:
                self.expression = "에러"
                self.result_displayed = True
        elif char == '%':
            # '%' 버튼이 눌렸을 때 현재 표시된 값의 100분의 1을 계산
            try:
                # 현재 expression을 숫자로 변환하여 100으로 나눔
                value = float(self.expression)
                self.expression = str(value / 100)
                self.result_displayed = True # 계산 결과이므로 True로 설정
            except ValueError:
                self.expression = "숫자 에러" # 숫자로 변환할 수 없을 때
                self.result_displayed = True
            except Exception:
                self.expression = "에러"
                self.result_displayed = True
        else:
            # 결과가 표시된 상태에서 새 숫자/연산자를 누르면 새로운 계산 시작
            if self.result_displayed and (char.isdigit() or char == '.'):
                self.expression = str(char)
                self.result_displayed = False
            elif self.result_displayed and (char in ['+', '-', '*', '/']):
                # 결과에 이어서 연산자를 누르면 계속 계산
                self.expression += str(char)
                self.result_displayed = False
            else:
                self.expression += str(char)
                self.result_displayed = False

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

# 메인 애플리케이션 실행
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

