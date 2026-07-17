class Solution:
    def isPalindrome(self, s: str) -> bool:
        esquerda = 0
        direita = len(s) - 1

        while esquerda < direita:
            # Ignora caracteres não alfanuméricos pela esquerda
            while esquerda < direita and not s[esquerda].isalnum():
                esquerda += 1

            # Ignora caracteres não alfanuméricos pela direita
            while esquerda < direita and not s[direita].isalnum():
                direita -= 1

            # Compara ignorando maiúsculas e minúsculas
            if s[esquerda].lower() != s[direita].lower():
                return False

            esquerda += 1
            direita -= 1

        return True