# -----------------------------------------------------------------------------------------------------------
# Akinator
# -----------------------------------------------------------------------------------------------------------

# Ответы на вопросы: Да / Нет

class TreeNode:

    # Инициализатор для создания узлов и вопросов в бинарном дереве
    def __init__(self, question):
        self.question = question
        self.left = None
        self.right = None

class QAkinator:

    # Метод для задания вопроса
    def yes(ques):
        while True:
            ans = input(ques)
            if ans == 'Да':
                return True
            if ans == 'Нет':
                return False

# Задание данных дерева
tree = TreeNode("человек?")
tree.left = TreeNode("животное?")
tree.right = TreeNode("ПРЕЗИДЕНТ?")
tree.left.left = TreeNode("МЫЛО?")
tree.left.right = TreeNode("летает?")
tree.left.right.left = TreeNode("СОБАКА?")
tree.left.right.right = TreeNode("ПТИЦА?")

# Здесь рофлан в том, что происходит бесконечный цикл до момента, пока не кончатся узлы в бинарном дереве.
# Как только они кончаются, акинатор предлагает свой ответ
def main():
    while True:
        p = tree
        while p.left != None:
            if QAkinator.yes("Ваш персонаж " + p.question + " "):
                p = p.right
            else:
                p = p.left
        if QAkinator.yes("Ваш персонаж " + p.question + " "):
            print("Ура! Я отгадал, я молодец!")
            break
        animal = input("Какого персонажа вы загадали? ")
        question = input("Какой вопрос различает персонажи КОШКА от СОБАКА? ")
        p.left = TreeNode(p.question)
        p.right = TreeNode(animal)
        p.question = question
        if not QAkinator.yes("Если персонаж кошка, то ответом на это вопрос будет Да или Нет? "):
            (p.right, p.left) = (p.left, p.right)

if __name__ == "__main__": main()