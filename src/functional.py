class MathClassRoom1:
    
    def __init__(self, num_of_items=30):
        self.num_of_items = num_of_items
        self.num1 = 30
        self.num2 = 0
        self.diff = None
        self.list_of_correct = []
        self.list_of_wrong = []
        self.count_of_operation = 0
        
    def _set_correct(self):
        self.num2 = self.num_of_items - self.num1
        self.list_of_correct.append(self.num1)
        self.list_of_correct.append(self.num2)
            
    def _set_wrong(self, wrong):
        self.list_of_wrong.append(wrong)

    def add_(self):
        try:
            self.num1 = self.num1 + self.diff
            self._set_correct()
        except Exception as e:
            self._set_wrong(str(e))
        self.count_of_operation += 1

    def sub_(self):
        try:
            self.num1 = self.num1 - self.diff
            self._set_correct()
            return self.num1
        except Exception as e:
            self._set_wrong(str(e))
        self.count_of_operation += 1

    def mul_(self):
        try:
            self.num1 = self.num1 * self.diff
            self._set_correct()
        except Exception as e:
            self._set_wrong(str(e))
        self.count_of_operation += 1

    def div_(self):
        try:
            self.num1 = self.num1 / self.diff
            self._set_correct()
        except Exception as e:
            self._set_wrong(str(e))
        self.count_of_operation += 1

    def pow2_(self):
        try:
            self.num1 = self.num1 ** 2
            self._set_correct()
        except Exception as e:
            self._set_wrong(str(e))
        self.count_of_operation += 1

    def sqrt_(self):
        try:
            self.num1 = self.num1 ** 0.5
            self._set_correct()
        except Exception as e:
            self._set_wrong(str(e))
        self.count_of_operation += 1
