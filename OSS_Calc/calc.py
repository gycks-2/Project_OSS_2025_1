import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""
        self.result_displayed = False  # To track if a result is currently shown

        # Input display
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # Buttons
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', 'SUM']  # Added 'SUM' button here
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
                # Evaluate the expression
                result = str(eval(self.expression))
                self.expression = result
                self.result_displayed = True
            except ZeroDivisionError:
                self.expression = "0으로 나눌 수 없음"
                self.result_displayed = True
            except SyntaxError:
                self.expression = "잘못된 수식"
                self.result_displayed = True
            except Exception:  # Catch any other general errors
                self.expression = "에러"
                self.result_displayed = True
        elif char == 'SUM':
            try:
                # Convert the current expression to an integer
                # Use float first to handle cases like "5.0"
                num = int(float(self.expression))
                if num < 1:
                    self.expression = "1 이상의 정수"
                else:
                    # Calculate the sum from 1 to num using Gauss's formula
                    # N * (N + 1) / 2
                    total_sum = num * (num + 1) // 2
                    self.expression = str(total_sum)
                self.result_displayed = True
            except ValueError:
                self.expression = "정수 입력 에러" # Error if input is not a valid number
                self.result_displayed = True
            except Exception:
                self.expression = "에러"
                self.result_displayed = True
        else:
            # If a result was displayed, start a new expression when a number or decimal is pressed
            if self.result_displayed and (char.isdigit() or char == '.'):
                self.expression = str(char)
                self.result_displayed = False
            # If a result was displayed, and an operator is pressed, continue the calculation
            elif self.result_displayed and (char in ['+', '-', '*', '/']):
                self.expression += str(char)
                self.result_displayed = False
            else:
                self.expression += str(char)
                self.result_displayed = False

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)


# Main application entry point
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
