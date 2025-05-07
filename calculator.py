class Calculator:
    def evaluate_math_expression(self, expression: str) -> float:
        self.tokens = list(expression.replace(" ", ""))
        self.pos = 0
        return self._parse_expression()

    def _peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def _consume(self):
        self.pos += 1

    def _parse_expression(self):
        result = self._parse_term()
        while self._peek() in ('+', '-'):
            op = self._peek()
            self._consume()
            right = self._parse_term()
            if op == '+':
                result += right
            elif op == '-':
                result -= right
        return result

    def _parse_term(self):
        result = self._parse_factor()
        while self._peek() == '*':
            self._consume()
            result *= self._parse_factor()
        return result

    def _parse_factor(self):
        if self._peek() == '+':
            self._consume()
            return self._parse_factor()
        if self._peek() == '-':
            self._consume()
            return -self._parse_factor()

        if self._peek() == '(':
            self._consume()
            result = self._parse_expression()
            if self._peek() == ')':
                self._consume()
            else:
                raise ValueError("Missing closing parenthesis")
            return result

        return self._parse_number()

    def _parse_number(self):
        num_str = ''
        while self._peek() is not None and (self._peek().isdigit() or self._peek() == '.'):
            num_str += self._peek()
            self._consume()
        if not num_str:
            raise ValueError("Invalid number format")
        return float(num_str)
